from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os

# -------------------------------------------------------------------
# LangChain + OpenAI LLM Interface Example
#
# LangChain wraps the OpenAI API behind a standard LLM interface,
# making it easy to swap models or chain prompts together.
# -------------------------------------------------------------------

# Reads OPENAI_API_KEY from environment automatically
# Set it beforehand: export OPENAI_API_KEY="sk-..."

# 1. Create the LangChain ChatOpenAI LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=100,
)

# 2. Invoke it directly — the simplest usage
prompt = "Explain what a neural network is in simple terms:"
print("=== Direct invoke ===")
response = llm.invoke(prompt)
print(response.content)
print()

# 3. Use a PromptTemplate to structure your inputs
template = PromptTemplate(
    input_variables=["topic"],
    template="Write a one-sentence definition of {topic}:",
)

# 4. Chain the prompt and the LLM together with the | operator
chain = template | llm

print("=== Chain with PromptTemplate ===")
result = chain.invoke({"topic": "machine learning"})
print(result.content)
