import getpass
import os

# -------------------------------------------------------------------
# PAL (Program-Aided Language Models) Example with LangChain
#
# Instead of asking the LLM to reason through a problem and answer
# directly, PAL asks the LLM to write Python code that solves the
# problem, then executes that code to get the answer.
#
# This reduces hallucination on math/logic problems because the
# computation is delegated to the Python interpreter.
# -------------------------------------------------------------------

# Ensure the API key is available before initializing the model
if not os.getenv("OPENAI_API_KEY"):
    print("OPENAI_API_KEY not found in environment. Please enter it now.")
    key = getpass.getpass("OPENAI_API_KEY: ")
    os.environ["OPENAI_API_KEY"] = key

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# The PAL prompt instructs the LLM to respond with executable Python
# that stores its final answer in a variable called `answer`
PAL_PROMPT = PromptTemplate(
    input_variables=["question"],
    template=(
        "Solve the following problem by writing Python code.\n"
        "Store the final numeric result in a variable called `answer`.\n"
        "Return ONLY the Python code, no explanation, no markdown fences.\n\n"
        "Problem: {question}\n\n"
        "Python code:"
    ),
)

# Initialize the LLM — low temperature for more deterministic code output
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Chain: prompt → LLM → strip the response to a plain string
chain = PAL_PROMPT | llm | StrOutputParser()


def pal_solve(question: str) -> str:
    """Generate Python code for the question, execute it, return the answer."""
    # Step 1: ask the LLM to produce Python code
    code = chain.invoke({"question": question})
    print(f"--- Generated code ---\n{code}\n----------------------")

    # Step 2: execute the generated code in an isolated namespace
    namespace = {}
    exec(code, namespace)  # noqa: S102

    # Step 3: retrieve the `answer` variable the LLM was instructed to set
    return namespace.get("answer", "No answer variable found in generated code.")


# --- Example problems ---

problems = [
    "If a train travels at 60 mph for 2.5 hours, how many miles does it travel?",
    "A store sells apples for $0.75 each. If I buy 13 apples and pay with a $20 bill, how much change do I get?",
    "What is the sum of all even numbers from 1 to 100?",
]

for problem in problems:
    print(f"\nQuestion: {problem}")
    answer = pal_solve(problem)
    print(f"Answer:   {answer}")
