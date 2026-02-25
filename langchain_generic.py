import getpass
import os
import langchain_core.messages

if not os.getenv("OPENAI_API_KEY"):
    print("OPENAI_API_KEY not found in environment. Please enter it now.")
    key = getpass.getpass("OPENAI_API_KEY: ")
    os.environ["OPENAI_API_KEY"] = key

from langchain.chat_models import init_chat_model

model_provider = "openai"

model = init_chat_model("gpt-4o-mini", temperature=0.7, max_tokens=100, model_provider= model_provider)
                        
print(f"Initialized model from provider: {model_provider}")

messages = [
    langchain_core.messages.SystemMessage(content="You are a helpful assistant."),
    langchain_core.messages.HumanMessage(content="What is the capital of France?"),
]
response = model.invoke(messages)
print(f"Response from {model_provider}: {response.content}")
