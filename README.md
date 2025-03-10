# OmnitrAIce: Revolutionary Project Generation System

> Created by **CraigFineTuned** - Building revolutionary software with small, efficient models

## Purpose
OmnitrAIce demonstrates how small, efficient language models can produce exceptional results through first-principles thinking. By focusing on fundamental truths rather than model size, this system achieves high-quality outputs that rival much larger models while maintaining speed and accessibility.

## Features
- **First-Principles Thinking**: Break down problems to fundamental components and eliminate artificial constraints
- **Multi-Agent Collaboration**: Specialized agents work together (CEO, CTO, Architect, Developer, Filesystem)
- **Revolutionary Code Generation**: Generate actual implementation code using first-principles approach
- **File Structure Creation**: Create complete project structures optimized for revolutionary projects
- **Interactive Web UI**: Customize agents and generate projects through a user-friendly interface
- **Revolutionary Metrics**: Measure innovation score, disruption factor, and 10x improvement score
- **YAML/JSON Configuration**: Configure all aspects of the system through external configuration files

## Modular Architecture
OmnitrAIce follows a modular architecture with clear separation of concerns:

For all available execution methods, see [EXECUTION_METHODS.md](EXECUTION_METHODS.md).
omnitrace/
├── agents/                 # Specialized agent implementations
│   ├── agent_interface.py  # Protocol defining agent interface
│   ├── ceo_agent.py        # CEO agent for vision creation
│   ├── cto_agent.py        # CTO agent for technical strategy
│   ├── architect_agent.py  # Architect agent for system design
│   ├── developer_agent.py  # Developer agent for implementation
│   └── filesystem_agent.py # Filesystem agent for file structure
├── core/                   # Core system functionality
│   ├── omniagent.py        # Base agent implementation
│   ├── enhanced_omniagent.py # Extended agent with customization
│   └── revolutionary_omniagent.py # Unified agent with all capabilities
├── generation/             # Content generation capabilities
│   ├── code_generator.py   # Revolutionary code generation
│   ├── doc_generator.py    # Documentation generation
│   └── structure_generator.py # Project structure generation
├── ui/                     # User interfaces
│   ├── web_ui.py           # Web interface using Gradio
│   ├── agent_customization_ui.py # UI for agent customization
│   └── cli.py              # Command-line interface
├── utils/                  # Utility modules
│   ├── first_principles.py # First-principles thinking implementation
│   └── template_manager.py # Template management utilities
└── run.py                  # Main entry point
```

## Quick Start

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate it: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Unix)
4. Install dependencies: `pip install -r requirements.txt`
5. Launch the web UI: `python run_web_ui.py`

For detailed instructions, see [INSTALLATION.md](INSTALLATION.md).

## Usage

### Command Line

```bash
# Launch the web interface (Universal Launcher - Most Reliable)
python run_web_ui.py

# Alternative launch method via main launcher
python omnitrace/run.py --web

# Create a project from the command line
python omnitrace/run.py --project "Revolutionary App" --description "A revolutionary app that..." --revolution-level maximum

# Use a configuration file
python omnitrace/run.py --config config/config_files/default_config.yaml
```

For all available execution methods, see [EXECUTION_METHODS.md](EXECUTION_METHODS.md).

### Configuration Options
- `--model`: LLM model to use (default: deepseek-r1:1.5b)
- `--revolution-level`: Level of revolutionary thinking (moderate/high/maximum)
- `--constraint-elimination`: Level of constraint elimination (cautious/moderate/aggressive)
- `--code-gen`: Enable code generation
- `--no-code-gen`: Disable code generation
- `--verbose`: Enable verbose logging
- `--config`: Path to configuration file (YAML/JSON)

## Requirements
- Python 3.9+
- Ollama
- Gradio
- LangChain
- PyYAML (for configuration files)

## Agents

### CEO Agent
Creates revolutionary vision by breaking down problems to fundamentals, questioning all assumptions and industry standards, and focusing on 10x improvements.

### CTO Agent
Develops technical strategy that challenges conventional approaches, selects technologies based on fundamental capabilities, and designs infrastructure for exponential scaling.

### Architect Agent
Designs revolutionary system architecture from first principles, challenges traditional architecture patterns, and creates novel interaction patterns between system components.

### Developer Agent
Plans implementation with 10x improvement approach, questions conventional development practices, and identifies opportunities for extreme simplification.

### Filesystem Agent
Creates revolutionary file structures based on fundamental relationships, challenges conventional directory organization, and designs for exponential growth.

## Revolutionary First-Principles Thinking

OmnitrAIce applies Elon Musk's first-principles methodology throughout the project generation process:

1. **Breaking Down to Fundamentals**: Each problem is deconstructed to its basic components
2. **Distinguishing Constraints**: Separating physical limitations from artificial constraints
3. **10x Improvement Focus**: Targeting order-of-magnitude improvements rather than incremental gains
4. **Revolutionary Design**: Reimagining solutions from scratch without conventional limitations
5. **Constraint Elimination**: Aggressively identifying and eliminating artificial constraints

## Documentation

OmnitrAIce includes comprehensive documentation:

- [EXECUTION_METHODS.md](EXECUTION_METHODS.md): All available ways to run the system
- [INSTALLATION.md](INSTALLATION.md): Detailed installation instructions
- [ROADMAP.md](ROADMAP.md): Development roadmap and future plans
- [REORGANIZATION_SUMMARY.md](REORGANIZATION_SUMMARY.md): Overview of the project reorganization
- [CONFIG_MIGRATION.md](CONFIG_MIGRATION.md): Status of configuration file migration
- [CHANGE_LOG.md](omnitrace/CHANGE_LOG.md): Detailed change history
- [Architecture Documentation](omnitrace/docs/architecture.md): Detailed system architecture
- [Development Guide](omnitrace/docs/development_guide.md): Guide for developers extending the system
- [Web UI Guide](omnitrace/docs/web_ui_guide.md): Guide for using the Web UI interfaces

## Contributing

Contributions are welcome! Please follow standard GitHub flow (fork, branch, PR) and ensure your changes maintain the revolutionary first-principles approach.

For development guidelines, see the [Development Guide](omnitrace/docs/development_guide.md).
