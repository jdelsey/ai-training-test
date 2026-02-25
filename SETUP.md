# Setup Instructions

## Activate Virtual Environment

### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows (Command Prompt)

```cmd
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
source .venv/bin/activate
```

## Install Dependencies

Once the virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Scripts

With the virtual environment activated:

```bash
python huggingface_example.py
python langchain_hf_example.py
```

## Setting Hugging Face Token

Set your read-only Hugging Face token before running, then run the script normally.

```bash
# PowerShell
$env:HF_TOKEN="your_read_only_token_here"

# Command Prompt
set HF_TOKEN=your_read_only_token_here

# macOS / Linux
export HF_TOKEN="your_read_only_token_here"
```

## Deactivate Virtual Environment

When you're done, deactivate the virtual environment:

```bash
deactivate
```
