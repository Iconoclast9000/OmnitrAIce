# OmnitrAIce

An AI-driven multi-agent system for software project generation using DeepSeek LLM.

## Overview

OmnitrAIce streamlines the software development process by coordinating specialized AI agents to collectively generate complete software projects. The system leverages the DeepSeek-r1:1.5b LLM to power its multi-agent architecture.

## Features

- **Multi-agent Architecture**: Specialized agents for different aspects of software development
- **Collaborative Generation**: Agents work together to create cohesive projects
- **Streamlined Workflow**: From project vision to implementation details
- **Documentation Generation**: Automatic creation of project documentation

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Ollama with the DeepSeek LLM installed

### Installation

1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Unix/MacOS: `source .venv/bin/activate`
4. Install requirements: `pip install langchain-ollama langchain-core`

### Usage

Run the main script:

```
python omniagent.py
```

Commands:
- `help` - Show available commands
- `create ProjectName "Project Description"` - Generate a new project
- `exit` - Exit the system

## Project Structure

- `omniagent.py` - Main implementation of the OmniAgent system
- `GOALS_AND_IMPLEMENTATION.md` - Project goals and implementation tracking
- `projects/` - Directory containing generated projects

## Implementation Status

See `GOALS_AND_IMPLEMENTATION.md` for detailed status of all components.

## License

MIT

## Author

Craig