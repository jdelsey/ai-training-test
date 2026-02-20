from transformers import pipeline
from huggingface_hub import login
import os

# Login with read-only token from environment variable
# Set HF_TOKEN environment variable with your read-only token
token = os.getenv('HF_TOKEN')
if token:
    login(token=token, add_to_git_credential=False)

# Create a text generation pipeline using a Hugging Face model
# This example uses the gpt2 model which provides better quality generation
generator = pipeline('text-generation', model='gpt2')

# Run a simple prompt
prompt = "Once upon a time"
result = generator(prompt, max_length=250, num_return_sequences=1)

# Print the generated text
print("Prompt:", prompt)
print("Generated text:", result[0]['generated_text'])
