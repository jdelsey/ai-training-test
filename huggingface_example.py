from transformers import pipeline

# Create a text generation pipeline using a Hugging Face model
# This example uses the distilgpt2 model which is lightweight
generator = pipeline('text-generation', model='distilgpt2')

# Run a simple prompt
prompt = "Once upon a time"
result = generator(prompt, max_length=100, num_return_sequences=1)

# Print the generated text
print("Prompt:", prompt)
print("Generated text:", result[0]['generated_text'])
