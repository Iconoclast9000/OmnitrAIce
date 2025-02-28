# OmnitrAIce

> A multi-agent system for streamlined project generation using the DeepSeek LLM

## Overview

OmnitrAIce is an innovative multi-agent system designed to leverage the DeepSeek LLM (deepseek-r1:1.5b) to generate complete software projects through coordinated specialized AI agents. Each agent focuses on specific aspects of project development, collectively creating comprehensive project specifications, architecture, and implementation plans.

This project was developed as a brainchild utilizing the unique reasoning capabilities of the DeepSeek model, creating a framework that developers can easily build upon and customize to suit their specific needs.

## Features

- **Multi-Agent Architecture**: Coordinated agents working together with specialized roles
- **Agent Customization Interface**: Web-based UI for tweaking agent behaviors
- **Template Management**: Create, save, and reuse custom agent templates
- **Flexible Parameter System**: Fine-tune agent characteristics through intuitive controls
- **Project Generation**: Automatically generate comprehensive project documentation
- **DeepSeek LLM Integration**: Optimized for the DeepSeek-r1:1.5b model

## Key Components

- **OmniAgent**: Central coordinator that manages all specialized agents
- **Executive Agents**: CEO and CTO agents for high-level project planning
- **Technical Agents**: Architect, DBA, and DevOps agents for system design
- **Implementation Agents**: Developer and Filesystem agents for implementation details
- **Web Interface**: Intuitive UI for agent customization and project creation

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) with the DeepSeek model installed

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/OmnitrAIce.git
   cd OmnitrAIce
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Make sure you have the DeepSeek model installed in Ollama:
   ```bash
   ollama pull deepseek-r1:1.5b
   ```

### Usage

1. Launch the enhanced OmnitrAIce interface:
   ```bash
   python run_omnitrace.py
   ```

2. Access the web interface at http://127.0.0.1:7860 in your browser

3. Select an agent type from the dropdown to customize it:
   - Edit the template directly in the Template Editor tab
   - Or use the Parameter Editor tab to adjust focus areas, strategy level, and more

4. Create a new project:
   - Enter a name and description in the Project Creation section
   - Click Create Project
   - Review the generated project files in the projects directory

## Agent Customization

The web interface allows you to customize agent behaviors without modifying any code:

### Template Editor
Directly edit the template used by each agent to guide its responses. For example, you can make the CEO agent think like Elon Musk by emphasizing:
- First principles thinking
- Ambitious, moonshot goals
- Cross-disciplinary innovation
- Rapid iteration and willingness to fail

### Parameter Editor
Fine-tune agent behavior through intuitive controls:
- **Focus Areas**: Define what the agent prioritizes
- **Strategy Level**: Control high-level vs tactical thinking
- **Detail Level**: Adjust the depth of analysis
- **Additional Considerations**: Add custom instructions

## Project Structure

```
OmnitrAIce/
├── config/                 # Configuration files
│   └── templates/          # Saved agent templates
├── misc/                   # Miscellaneous resources
├── projects/               # Generated projects
├── .venv/                  # Virtual environment
├── GOALS_AND_IMPLEMENTATION.md  # Detailed implementation tracking
├── omniagent.py            # Main OmniAgent implementation
├── enhanced_omniagent.py   # Enhanced OmniAgent with UI
├── README.md               # This file
└── run_omnitrace.py        # Launcher script
```

## Sample Generated Projects

Each generated project includes:
- Project Vision (from CEO agent)
- Technical Architecture (from Architect agent)
- Implementation Plan (from Developer agent)
- Project History (timeline of development)
- README with project overview

## Why DeepSeek?

The DeepSeek-r1:1.5b model offers exceptional performance despite its compact size, making it ideal for local development and customization. This approach enables developers to build upon the framework without requiring massive computational resources.

The OmnitrAIce architecture is designed to maximize the strengths of the DeepSeek model by channeling its capabilities through specialized agents, each focused on a specific aspect of software development.

## For Developers

OmnitrAIce is designed with extensibility in mind. The architecture is modular and well-documented, making it straightforward to:

- Add new specialized agents
- Customize existing agent behaviors
- Integrate with additional tools and frameworks
- Enhance the project generation workflow

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The [DeepSeek AI](https://deepseek.ai/) team for creating the DeepSeek-r1:1.5b model
- The [LangChain](https://langchain.com/) and [Gradio](https://gradio.app/) communities for their excellent tools