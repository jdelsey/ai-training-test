from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
import os

# -------------------------------------------------------------------
# LangChain + Hugging Face LLM Interface Example
#
# LangChain wraps the HuggingFace pipeline behind a standard LLM
# interface, making it easy to swap models or chain prompts together.
# -------------------------------------------------------------------

# 1. Build the underlying HuggingFace pipeline (same as before)
hf_pipeline = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=100,   # tokens to generate beyond the prompt
    do_sample=True,
    temperature=0.7,
)

# 2. Wrap it with LangChain's HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=hf_pipeline)

# 3. Invoke it directly — the simplest usage
prompt = "Explain what a neural network is in simple terms:"
print("=== Direct invoke ===")
response = llm.invoke(prompt)
print(response)
print()

# 4. Use a PromptTemplate to structure your inputs
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["topic"],
    template="Write a one-sentence definition of {topic}:",
)

# 5. Chain the prompt and the LLM together with the | operator
chain = template | llm

print("=== Chain with PromptTemplate ===")
result = chain.invoke({"topic": "machine learning"})
print(result)
