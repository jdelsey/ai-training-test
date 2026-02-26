import getpass
import os

# -------------------------------------------------------------------
# Real-Time Internet Search with LangChain + Tavily
#
# Uses a LangChain ReAct agent equipped with a Tavily search tool.
# The agent decides when to search the web based on the question,
# then synthesizes the results into a final answer.
#
# Prerequisites:
#   - OPENAI_API_KEY  (https://platform.openai.com)
#   - TAVILY_API_KEY  (https://app.tavily.com — free tier available)
# -------------------------------------------------------------------

# Prompt for API keys if not already set in the environment
for key_name in ("OPENAI_API_KEY", "TAVILY_API_KEY"):
    if not os.getenv(key_name):
        print(f"{key_name} not found in environment.")
        os.environ[key_name] = getpass.getpass(f"{key_name}: ")

from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents import create_react_agent

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Create the Tavily search tool
# max_results controls how many web results are passed to the LLM
search_tool = TavilySearch(max_results=3)

# Build a ReAct agent — it loops between:
#   Thought  → decide whether to search or answer
#   Action   → call the search tool if needed
#   Observation → read the search results
#   ... repeat until it has enough info to give a final answer
agent = create_react_agent(llm, tools=[search_tool])


def search_and_answer(question: str) -> str:
    """Run the agent on a question that may require a web search."""
    response = agent.invoke({"messages": [("human", question)]})
    # The final answer is the last message in the response
    return response["messages"][-1].content


# --- Example questions requiring up-to-date information ---

questions = [
    "What is the current version of Python?",
    "What were the headlines on the OpenAI blog this week?",
]

for question in questions:
    print(f"\nQuestion: {question}")
    print(f"Answer:   {search_and_answer(question)}")
