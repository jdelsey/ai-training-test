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

### `langchain_openai_example.py`

Mirrors `langchain_hf_example.py` but uses OpenAI as the backend via `ChatOpenAI`. Covers:

- Initializing a `ChatOpenAI` model
- Invoking the LLM directly
- Using `PromptTemplate` to structure inputs
- Chaining a prompt and LLM together with the `|` operator

### `langchain_generic.py`

Uses LangChain's `init_chat_model()` for a provider-agnostic setup. Change `model_provider` to switch backends (e.g. `"anthropic"`, `"google-genai"`) without modifying the rest of the code. Prompts for the API key securely at runtime if not set in the environment.

### `langchain_pal_example.py`

Demonstrates **PAL (Program-Aided Language Models)**. Instead of asking the LLM to reason through a problem directly, PAL asks it to write Python code that solves the problem, then executes that code to get the answer. This reduces hallucination on math and logic problems because the computation is delegated to the Python interpreter.

#### PAL execution environment

The generated code runs in an isolated dictionary namespace:

```python
namespace = {}
exec(code, namespace)
```

- The code **cannot read or modify** the script's own local/global variables
- Each call gets a **clean slate** — no state leaks between problems
- Standard **built-ins are still available** (`range`, `sum`, `len`, etc.)

> **Note:** This is not a full sandbox. The generated code can still `import` modules, make network calls, or read/write files. For untrusted input, use a proper sandbox like `restrictedpython` or a subprocess with resource limits.

### `langchain_search_example.py`

Demonstrates **real-time internet search** using a LangChain ReAct agent equipped with the Tavily search tool. The agent decides when to search the web based on the question, fetches live results, and synthesizes them into a final answer.

Requires two API keys:

- `OPENAI_API_KEY` — [platform.openai.com](https://platform.openai.com)
- `TAVILY_API_KEY` — [app.tavily.com](https://app.tavily.com) (free tier available)

The agent follows a **Thought → Action → Observation** loop:

1. **Thought** — decides whether the question needs a web search
2. **Action** — calls the Tavily search tool if needed
3. **Observation** — reads the results and repeats or answers

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
| `langchain-core` | Core LangChain primitives (prompts, output parsers) |
| `langchain-huggingface` | LangChain adapter for Hugging Face pipelines |
| `langchain-openai` | LangChain adapter for OpenAI models |
| `langchain-tavily` | LangChain adapter for Tavily web search |
| `langgraph` | ReAct agent and graph-based orchestration |
| `openai` | OpenAI Python SDK |
