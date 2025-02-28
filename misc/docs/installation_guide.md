# OmnitrAIce Installation Guide

This guide will walk you through setting up OmnitrAIce on your local machine.

## Prerequisites

Before installing OmnitrAIce, make sure you have the following:

1. **Python 3.8+** - OmnitrAIce requires Python 3.8 or higher.
2. **Git** - For cloning the repository.
3. **Ollama** - To run the DeepSeek LLM locally.

## Step 1: Install Ollama

1. Visit [Ollama's official website](https://ollama.ai/) and download the installer for your operating system.
2. Follow the installation instructions.
3. After installation, pull the DeepSeek model by running:
   ```bash
   ollama pull deepseek-r1:1.5b
   ```

## Step 2: Clone the OmnitrAIce Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/OmnitrAIce.git
cd OmnitrAIce
```

## Step 3: Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate

# Activate on macOS/Linux
source .venv/bin/activate
```

## Step 4: Install Dependencies

Install all required dependencies:

```bash
pip install -r requirements.txt
```

## Step 5: Run the Setup Script

For first-time setup, run the setup script to ensure all necessary directories and configurations are created:

```bash
python setup.py
```

## Step 6: Launch OmnitrAIce

Start the OmnitrAIce system with the web-based user interface:

```bash
python run_omnitrace.py
```

This will launch the OmnitrAIce web interface, which you can access in your browser at http://127.0.0.1:7860.

## Troubleshooting

### Ollama Connection Issues

If OmnitrAIce fails to connect to Ollama, check if:
- Ollama is running (you should see it in your system tray or task manager)
- You have successfully pulled the DeepSeek model
- Your firewall isn't blocking the connection

### DeepSeek Model Issues

If you encounter issues with the DeepSeek model:
1. Check if the model is downloaded correctly:
   ```bash
   ollama list
   ```
2. Try re-pulling the model:
   ```bash
   ollama pull deepseek-r1:1.5b
   ```

### Python Environment Issues

If you encounter Python-related errors:
1. Verify your Python version:
   ```bash
   python --version
   ```
2. Ensure your virtual environment is activated
3. Try reinstalling the dependencies:
   ```bash
   pip install --upgrade --force-reinstall -r requirements.txt
   ```

## Next Steps

Once OmnitrAIce is up and running, explore the following:

1. **Agent Customization**: Modify agent templates to fit your needs
2. **Project Creation**: Generate your first project 
3. **Documentation**: Review the GOALS_AND_IMPLEMENTATION.md file for a deeper understanding
4. **Template Experimentation**: Try different parameter settings to see how they affect project generation

For more detailed information on using OmnitrAIce, refer to the documentation in the `misc/docs` directory.