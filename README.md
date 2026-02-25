# ai-training-test

A collection of Python examples for learning AI/ML integrations with Hugging Face and LangChain.

## Examples

### `huggingface_example.py`

Uses the `transformers` library directly to run text generation with the `gpt2` model via a `pipeline`. Good starting point for understanding how Hugging Face models work.

### `langchain_hf_example.py`

Demonstrates LangChain's LLM interface wrapping a Hugging Face model. Covers:

- Wrapping a `transformers` pipeline with `HuggingFacePipeline`
- Invoking the LLM directly
- Using `PromptTemplate` to structure inputs
- Chaining a prompt and LLM together with the `|` operator

## Setup

See [SETUP.md](SETUP.md) for full instructions on creating a virtual environment, installing dependencies, and setting your Hugging Face token.

### Quick start

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run an example
python huggingface_example.py
python langchain_hf_example.py
```

## Dependencies

| Package | Purpose |
| --- | --- |
| `transformers` | Hugging Face model pipelines |
| `torch` | PyTorch backend for model inference |
| `huggingface_hub` | Model downloads and authentication |
| `langchain` | LLM chaining and orchestration framework |
| `langchain-huggingface` | LangChain adapter for Hugging Face pipelines |
