# OmnitrAIce Installation Guide

> Created by **CraigFineTuned** - Demonstrating the power of small, efficient models

This guide provides step-by-step instructions for installing and setting up the OmnitrAIce revolutionary project generation system.

## System Requirements

- Python 3.9 or higher
- Ollama (for local LLM support)
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space

## Installation Options

There are two main ways to install OmnitrAIce:

1. **Direct use from repository** (recommended for development)
2. **Package installation** (recommended for regular use)

## Option 1: Direct Use from Repository

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/OmnitrAIce.git
cd OmnitrAIce
```

### 2. Create a Virtual Environment

```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

Run the system test script to verify all components are working:

```bash
python test_system.py
```

### 5. Launch the Web UI

```bash
python run_web_ui.py
```

## Option 2: Package Installation

### 1. Install via pip

```bash
pip install omnitrace
```

### 2. Run OmnitrAIce

```bash
# Launch the web UI
omnitrace --web

# Generate a project
omnitrace --project "My Project" --description "Description"
```

## Setting Up Ollama

OmnitrAIce requires an LLM to function. The default configuration uses Ollama with the Deepseek model.

### 1. Install Ollama

Follow the instructions at [ollama.ai](https://ollama.ai) to install Ollama for your platform.

### 2. Download Required Model

```bash
# Pull the deepseek-r1:1.5b model
ollama pull deepseek-r1:1.5b
```

### 3. Verify Ollama is Running

```bash
ollama list
```

## Configuration

### Basic Configuration

The default configuration works out of the box, but you can customize OmnitrAIce by:

1. Using command-line arguments:
   ```bash
   python omnitrace/run.py --model "deepseek-r1:1.5b" --revolution-level maximum
   ```

2. Using a configuration file:
   ```bash
   python omnitrace/run.py --config config/config_files/default_config.yaml
   ```

### Advanced Configuration

For advanced customization, you can:

1. Modify agent templates in `omnitrace/config/templates/`
2. Create custom templates via the Web UI
3. Adjust revolutionary parameters via command-line or configuration file

## Troubleshooting

### Common Issues

1. **Web UI fails to launch**
   - Ensure Gradio is installed: `pip install gradio>=3.40.0`
   - Use the universal launcher: `python run_web_ui.py`
   - Check logs in the `logs/` directory

2. **Package import errors**
   - Ensure you're running from the correct directory
   - Check that your Python environment is activated
   - Verify all dependencies are installed

3. **No LLM connection**
   - Ensure Ollama is running: `ollama serve`
   - Verify the model is downloaded: `ollama list`
   - Check network connectivity to Ollama service

### Getting Logs

For detailed error information, check the log files in the `logs/` directory:

- `omnitrace_YYYYMMDD_HHMMSS.log`: Main application logs
- `web_ui_YYYYMMDD_HHMMSS.log`: Web UI specific logs
- `system_test_YYYYMMDD_HHMMSS.log`: System test logs

## Support

For additional help:

1. Consult the documentation in the `omnitrace/docs/` directory
2. Check the [GitHub repository](https://github.com/yourusername/OmnitrAIce) for issues and discussions
