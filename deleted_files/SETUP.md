# OmnitrAIce Project Setup Guide

## Prerequisites
- Python 3.9+
- pip
- Optional: Ollama installed and running

## Setup Steps

1. Clone the Repository
```bash
git clone https://github.com/YourUsername/OmnitrAIce.git
cd OmnitrAIce
```

2. Create a Virtual Environment
```bash
python -m venv .venv
```

3. Activate Virtual Environment
- Windows:
```powershell
.venv\Scripts\Activate
```
- macOS/Linux:
```bash
source .venv/bin/activate
```

4. Install Dependencies
```bash
pip install -r requirements.txt
```

5. Setup Ollama
- Install Ollama from: https://ollama.com/
- Pull DeepSeek model:
```bash
ollama pull deepseek-coder:6.7b
```

## Running the Project

### CLI Mode
```bash
python revolutionary_omniagent.py --cli
```

### Web UI Mode
```bash
python revolutionary_omniagent.py --ui
```

## Customization
- Modify `config/templates/` for agent templates
- Adjust model in the command line with `--model` flag

## Troubleshooting
- Ensure Ollama is running
- Check Python and pip versions
- Verify virtual environment activation
