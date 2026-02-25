import getpass
import os
import langchain_core.messages

# -------------------------------------------------------------------
# LangChain Generic Chat Model Example
#
# Uses LangChain's init_chat_model() to initialize a model in a
# provider-agnostic way. Swap model_provider to use a different
# backend (e.g. "anthropic", "google-genai") without changing the
# rest of the code.
# -------------------------------------------------------------------

# If the API key isn't already in the environment, prompt the user
# to enter it securely (input is hidden via getpass)
if not os.getenv("OPENAI_API_KEY"):
    print("OPENAI_API_KEY not found in environment. Please enter it now.")
    key = getpass.getpass("OPENAI_API_KEY: ")
    os.environ["OPENAI_API_KEY"] = key

# Import after the key is set so the library can pick it up
from langchain.chat_models import init_chat_model

# The provider string determines which backend is used
model_provider = "openai"

# Initialize the model — init_chat_model resolves the correct class
# based on model_provider, keeping the rest of the code provider-agnostic
model = init_chat_model("gpt-4o-mini", temperature=0.7, max_tokens=100, model_provider=model_provider)

print(f"Initialized model from provider: {model_provider}")

# Build a conversation as a list of typed messages:
#   SystemMessage  — sets the assistant's behavior/persona
#   HumanMessage   — represents the user's input
messages = [
    langchain_core.messages.SystemMessage(content="You are a helpful assistant."),
    langchain_core.messages.HumanMessage(content="What is the capital of France?"),
]

# Send the message list to the model and print the text response
response = model.invoke(messages)
print(f"Response from {model_provider}: {response.content}")
