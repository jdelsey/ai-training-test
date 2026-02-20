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

## Running the Script

With the virtual environment activated:

```bash
python huggingface_example.py
```

## Setting Hugging Face Token

Set your read-only Hugging Face token before running:

### PowerShell
```powershell
$env:HF_TOKEN="your_read_only_token_here"
```

### Command Prompt
```cmd
set HF_TOKEN=your_read_only_token_here
```

### macOS / Linux
```bash
export HF_TOKEN="your_read_only_token_here"
```

Then run the script normally.

## Deactivate Virtual Environment

When you're done, deactivate the virtual environment:

```bash
deactivate
```
