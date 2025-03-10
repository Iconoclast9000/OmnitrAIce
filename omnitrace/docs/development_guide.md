# OmnitrAIce Development Guide

This guide provides comprehensive instructions for developers who want to extend or modify the OmnitrAIce system. It covers all major components and provides examples for common extension scenarios.

## Table of Contents

1. [Environment Setup](#1-environment-setup)
2. [Project Structure](#2-project-structure)
3. [Core Components](#3-core-components)
4. [Agent System](#4-agent-system)
5. [Revolutionary First-Principles Approach](#5-revolutionary-first-principles-approach)
6. [User Interfaces](#6-user-interfaces)
7. [Generation Capabilities](#7-generation-capabilities)
8. [Configuration System](#8-configuration-system)
9. [Extension Examples](#9-extension-examples)
10. [Testing](#10-testing)
11. [Version Control](#11-version-control)
12. [Documentation](#12-documentation)

## 1. Environment Setup

### Requirements

- Python 3.9+
- LangChain and LangChain-Ollama
- Gradio for the Web UI
- Additional dependencies in requirements.txt

### Installation for Development

```bash
# Clone the repository
git clone https://github.com/yourusername/omnitrace.git
cd omnitrace

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .  # Install in development mode
pip install -r requirements.txt

# Run the application
python -m omnitrace.run
```

## 2. Project Structure

The OmnitrAIce project follows a modular structure for better organization and maintainability:

```
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
└── utils/                  # Utility modules
    ├── first_principles.py # First-principles thinking implementation
    └── template_manager.py # Template management utilities
```

## 3. Core Components

### Base OmniAgent (core/omniagent.py)

The foundation of the system, responsible for:
- Basic agent coordination
- Project state management
- Template handling
- Project generation workflow

```python
# Example: Basic usage of OmniAgent
from omnitrace.core.omniagent import OmniAgent

agent = OmniAgent(model_name="deepseek-r1:1.5b")
result = await agent.create_project("My Project", "A project description")
```

### Enhanced OmniAgent (core/enhanced_omniagent.py)

Extends the base agent with:
- Template customization
- Agent parameter adjustments
- Enhanced project generation features

```python
# Example: Using EnhancedOmniAgent with customization
from omnitrace.core.enhanced_omniagent import EnhancedOmniAgent

agent = EnhancedOmniAgent(model_name="deepseek-r1:1.5b")
agent.customize_agent_template("ceo", {"ambition_level": "moonshot"})
```

### Revolutionary OmniAgent (core/revolutionary_omniagent.py)

The unified agent with all revolutionary capabilities:
- First-principles thinking
- Revolutionary metrics
- Specialized agents integration
- Advanced generation capabilities

```python
# Example: Using Revolutionary OmniAgent with full capabilities
from omnitrace.core.revolutionary_omniagent import UnifiedOmniAgent

agent = UnifiedOmniAgent(model_name="deepseek-r1:1.5b")
agent.set_revolution_level("maximum")
agent.set_constraint_elimination("aggressive")
agent.enable_code_generation(True)
```

## 4. Agent System

### Agent Interface (agents/agent_interface.py)

Defines the protocol that all agents must follow:

```python
# Example: Agent interface implementation
from typing import Dict, Any, Optional
from langchain_core.language_models import BaseLLM

class MyAgent:
    def __init__(self, llm: BaseLLM, template: Optional[str] = None, 
                parameters: Optional[Dict[str, Any]] = None) -> None:
        self.llm = llm
        self.template = template or "Default template with {task} and {context}"
        self.parameters = parameters or {}
    
    async def process(self, task: str, context: Dict[str, Any]) -> str:
        # Process the task with the given context
        # ...
        return "Result"
    
    def set_revolution_level(self, level: str) -> None:
        self.parameters["revolution_level"] = level
    
    def set_constraint_elimination(self, level: str) -> None:
        self.parameters["constraint_elimination"] = level
```

### Adding a New Agent

1. Create a new agent file in the `agents/` directory
2. Implement the agent interface
3. Create a template in `config/templates/`
4. Register the agent in `revolutionary_omniagent.py`

```python
# Example: New Marketing Agent (agents/marketing_agent.py)
from typing import Dict, Any, Optional
from langchain_core.language_models import BaseLLM

class MarketingAgent:
    def __init__(self, llm: BaseLLM, template: Optional[str] = None, 
                parameters: Optional[Dict[str, Any]] = None) -> None:
        self.llm = llm
        self.template = template or "Default marketing template with {task} and {context}"
        self.parameters = parameters or {
            "focus_areas": ["Revolutionary marketing strategy", "10x engagement approaches"],
            "detail_level": "high"
        }
    
    async def process(self, task: str, context: Dict[str, Any]) -> str:
        # Process the marketing task
        # ...
        return "Marketing strategy result"
    
    def set_revolution_level(self, level: str) -> None:
        self.parameters["revolution_level"] = level
    
    def set_constraint_elimination(self, level: str) -> None:
        self.parameters["constraint_elimination"] = level

# Registration in revolutionary_omniagent.py:
# self.marketing_agent = MarketingAgent(self.llm)
```

## 5. Revolutionary First-Principles Approach

### First Principles Module (utils/first_principles.py)

Implements Elon Musk's first-principles thinking methodology:

```python
# Example: Using first-principles analysis
from omnitrace.utils.first_principles import FirstPrinciplesAnalyzer

analyzer = FirstPrinciplesAnalyzer()
analysis = analyzer.apply_first_principles("Project description here")
```

### Revolutionary Approach Parameters

- **Revolution Level**: Controls the intensity of revolutionary thinking
  - `moderate`: Balanced approach
  - `high`: Strong revolutionary focus
  - `maximum`: Extreme revolutionary focus

- **Constraint Elimination**: Controls how aggressively to eliminate constraints
  - `cautious`: Minimal constraint elimination
  - `moderate`: Balanced constraint elimination
  - `aggressive`: Maximum constraint elimination

## 6. User Interfaces

### Web UI (ui/web_ui.py)

The Gradio-based web interface with:
- Project creation tab
- Agent customization tab
- Template management tab
- Revolutionary settings tab

```python
# Example: Launching the Web UI
from omnitrace.ui.web_ui import OmnitrAIceWebUI
from omnitrace.core.revolutionary_omniagent import UnifiedOmniAgent

agent = UnifiedOmniAgent()
ui = OmnitrAIceWebUI(agent=agent)
ui.launch()
```

### CLI (ui/cli.py)

Command-line interface with comprehensive options:

```bash
# Example: Using the CLI
python -m omnitrace.run --project "My Project" --description "Description" --revolution-level maximum
```

### Adding a New UI Component

```python
# Example: Adding a new tab to the Web UI
def create_new_tab():
    with gr.Tab("My New Feature"):
        gr.Markdown("# My New Feature")
        input_text = gr.Textbox(label="Input")
        output_text = gr.Textbox(label="Output")
        process_btn = gr.Button("Process")
        
        def process_fn(text):
            # Process the input
            return "Processed: " + text
        
        process_btn.click(fn=process_fn, inputs=input_text, outputs=output_text)
    
    return tab

# Add to the tabs list in OmnitrAIceWebUI.__init__
self.tabs.append(create_new_tab())
```

## 7. Generation Capabilities

### Code Generator (generation/code_generator.py)

Generates revolutionary code for projects:

```python
# Example: Using the code generator
from omnitrace.generation.code_generator import RevolutionaryCodeGenerator
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="deepseek-r1:1.5b")
generator = RevolutionaryCodeGenerator(llm)
code = await generator.generate_file_code("file.py", "A utility file for...", {"vision": "..."})
```

### Structure Generator (generation/structure_generator.py)

Creates project directory structures:

```python
# Example: Using the structure generator
from omnitrace.generation.structure_generator import StructureGenerator
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="deepseek-r1:1.5b")
generator = StructureGenerator(llm)
structure = await generator.create_structure("My Project", "A project description", {"vision": "..."})
```

### Adding a New Generator

```python
# Example: Creating a new API Generator
from typing import Dict, Any, Optional, List
from langchain_core.language_models import BaseLLM

class ApiGenerator:
    def __init__(self, llm: BaseLLM) -> None:
        self.llm = llm
    
    async def generate_api_spec(self, project_name: str, context: Dict[str, Any]) -> Dict[str, Any]:
        # Generate API specification
        # ...
        return {
            "endpoints": [
                {"path": "/users", "method": "GET", "description": "List users"},
                # ...
            ]
        }
    
    async def generate_api_code(self, spec: Dict[str, Any], language: str) -> Dict[str, str]:
        # Generate code for the API based on the specification
        # ...
        return {
            "app.py": "from flask import Flask...",
            "routes/users.py": "def get_users():..."
        }
```

## 8. Configuration System

### Template Manager (utils/template_manager.py)

Manages agent templates across the system:

```python
# Example: Using the template manager
from omnitrace.utils.template_manager import TemplateManager

manager = TemplateManager()
template = manager.load_template("ceo")
custom_template = manager.customize_template("ceo", {"first_principles_level": "maximum"})
manager.save_custom_template("my_ceo_template", custom_template)
```

### Configuration Files

Configuration can be loaded from YAML or JSON files:

```yaml
# Example: config.yaml
model:
  name: "deepseek-r1:1.5b"
  parameters:
    temperature: 0.7

revolution_level: "maximum"
constraint_elimination: "aggressive"

agents:
  ceo:
    focus_areas:
      - "First-principles problem analysis"
      - "Revolutionary vision creation"
  cto:
    focus_areas:
      - "First-principles technical analysis"
      - "Revolutionary technology selection"
```

## 9. Extension Examples

### Creating a New Agent Type

```python
# 1. Create the agent class (agents/data_science_agent.py)
from typing import Dict, Any, Optional
from langchain_core.language_models import BaseLLM

class DataScienceAgent:
    def __init__(self, llm: BaseLLM, template: Optional[str] = None, 
                parameters: Optional[Dict[str, Any]] = None) -> None:
        self.llm = llm
        self.template = template or "You are a Data Science Agent inspired by first-principles thinking. Task: {task}, Context: {context}"
        self.parameters = parameters or {
            "focus_areas": ["Data analysis strategy", "Revolutionary insights discovery"],
            "revolution_level": "high"
        }
    
    async def process(self, task: str, context: Dict[str, Any]) -> str:
        # Process the data science task
        # Use self.llm to generate a response with the template
        processed_template = self.template.format(task=task, context=context)
        response = await self.llm.agenerate([processed_template])
        return response.generations[0][0].text
    
    def set_revolution_level(self, level: str) -> None:
        self.parameters["revolution_level"] = level
    
    def set_constraint_elimination(self, level: str) -> None:
        self.parameters["constraint_elimination"] = level

# 2. Create a template (config/templates/data_science_template.json)
{
  "template": "You are a Data Science Agent inspired by Elon Musk's first-principles thinking.\nTask: {task}\nContext: {context}\n\nApproach this data analysis by breaking down the problem to its fundamental components and reasoning up from there.",
  "parameters": {
    "focus_areas": [
      "First-principles data analysis",
      "Revolutionary insight discovery",
      "10x improvement identification"
    ],
    "revolution_level": "high",
    "constraint_elimination": "moderate"
  }
}

# 3. Register in revolutionary_omniagent.py
from agents.data_science_agent import DataScienceAgent

# In UnifiedOmniAgent.__init__:
self.data_science_agent = DataScienceAgent(self.llm)

# Add method to use the agent:
async def process_data_science(self, task: str, context: Dict[str, Any]) -> str:
    return await self.data_science_agent.process(task, context)
```

### Extending the Web UI

```python
# Example: Adding a data visualization tab to the Web UI
import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

def create_visualization_tab():
    with gr.Tab("Data Visualization"):
        gr.Markdown("# Revolutionary Data Visualization")
        
        with gr.Row():
            with gr.Column():
                data_input = gr.Textbox(
                    label="Input Data (CSV or JSON)",
                    lines=10,
                    placeholder="Paste your data here..."
                )
                viz_type = gr.Dropdown(
                    label="Visualization Type",
                    choices=["Bar Chart", "Line Chart", "Scatter Plot", "Heatmap"],
                    value="Bar Chart"
                )
                generate_btn = gr.Button("Generate Revolutionary Visualization")
            
            with gr.Column():
                plot_output = gr.Plot(label="Visualization Output")
                insights_output = gr.Textbox(label="Revolutionary Insights", lines=5)
        
        def generate_visualization(data, viz_type):
            # Parse data and create visualization
            # This is a simple example using random data
            fig, ax = plt.subplots()
            x = np.arange(10)
            y = np.random.rand(10) * 10
            
            if viz_type == "Bar Chart":
                ax.bar(x, y)
            elif viz_type == "Line Chart":
                ax.plot(x, y)
            elif viz_type == "Scatter Plot":
                ax.scatter(x, y)
            elif viz_type == "Heatmap":
                data = np.random.rand(10, 10)
                ax.imshow(data, cmap='viridis')
                
            ax.set_title("Revolutionary " + viz_type)
            
            # Generate insights
            insights = f"This {viz_type.lower()} reveals revolutionary patterns in your data."
            
            return fig, insights
        
        generate_btn.click(
            fn=generate_visualization,
            inputs=[data_input, viz_type],
            outputs=[plot_output, insights_output]
        )
    
    return tab

# Add to OmnitrAIceWebUI.__init__
self.tabs.append(create_visualization_tab())
```

## 10. Testing

### Unit Testing

```python
# Example: Unit test for an agent
import unittest
from unittest.mock import MagicMock, patch
import asyncio
from omnitrace.agents.cto_agent import CTOAgent

class TestCTOAgent(unittest.TestCase):
    def setUp(self):
        self.mock_llm = MagicMock()
        self.mock_llm.agenerate = MagicMock()
        self.agent = CTOAgent(llm=self.mock_llm)
    
    def test_initialization(self):
        self.assertIsNotNone(self.agent)
        self.assertEqual(self.agent.parameters["strategy_level"], "high")
    
    async def async_test_process(self):
        # Mock the LLM response
        mock_response = MagicMock()
        mock_response.generations = [[MagicMock(text="Test response")]]
        self.mock_llm.agenerate.return_value = mock_response
        
        # Test context
        context = {"context": "Test context", "vision": "Test vision"}
        
        # Call the process method
        result = await self.agent.process("Test task", context)
        
        # Check result
        self.assertEqual(result, "Test response")
        self.mock_llm.agenerate.assert_called_once()
    
    def test_process(self):
        # Run the async test
        asyncio.run(self.async_test_process())
    
    def test_set_revolution_level(self):
        self.agent.set_revolution_level("maximum")
        self.assertEqual(self.agent.parameters["revolution_level"], "maximum")
```

### Integration Testing

```python
# Example: Integration test for project creation
import unittest
import asyncio
import tempfile
import shutil
import os
from omnitrace.core.revolutionary_omniagent import UnifiedOmniAgent

class TestProjectCreation(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        os.chdir(self.temp_dir)
        
        # Create a projects directory for output
        os.makedirs("projects", exist_ok=True)
        
        # Initialize agent with test configuration
        self.agent = UnifiedOmniAgent(model_name="deepseek-r1:1.5b")
    
    def tearDown(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        shutil.rmtree(self.temp_dir)
    
    async def async_test_create_project(self):
        # Create a simple project
        result = await self.agent.create_project(
            "Test Project",
            "A test project for integration testing"
        )
        
        # Check result
        self.assertEqual(result["status"], "success")
        self.assertTrue(os.path.exists(result["output_dir"]))
        self.assertTrue(os.path.exists(os.path.join(result["output_dir"], "README.md")))
        self.assertTrue(os.path.exists(os.path.join(result["output_dir"], "docs")))
    
    def test_create_project(self):
        # Run the async test
        asyncio.run(self.async_test_create_project())
```

## 11. Version Control

### Branching Strategy

- `main`: Stable production version
- `develop`: Integration branch for features
- `feature/*`: Individual feature branches
- `release/*`: Release preparation branches
- `hotfix/*`: Urgent fixes for production

### Commit Conventions

- Use semantic commit messages: `feat: add code generation`
- Include issue numbers where applicable: `fix: resolve template loading (#42)`
- Keep commits focused on single logical changes

### Pull Request Process

1. Create a feature branch from `develop`
2. Implement and test your changes
3. Create a pull request to `develop`
4. Ensure tests pass and code review is complete
5. Merge the pull request

## 12. Documentation

### Code Documentation

```python
# Example: Well-documented function
def process_template(template: str, parameters: Dict[str, Any]) -> str:
    """
    Process a template string by replacing placeholders with parameter values.
    
    Args:
        template: Template string with {placeholder} syntax
        parameters: Dictionary mapping placeholder names to values
    
    Returns:
        Processed template with placeholders replaced by parameter values
    
    Raises:
        KeyError: If a placeholder in the template doesn't have a corresponding parameter
        
    Examples:
        >>> process_template("Hello, {name}!", {"name": "World"})
        "Hello, World!"
    """
    try:
        return template.format(**parameters)
    except KeyError as e:
        raise KeyError(f"Missing required parameter: {e}")
```

### Architecture Documentation

See [architecture.md](architecture.md) for comprehensive system architecture documentation.

### README Guidelines

- Clear project overview
- Installation instructions
- Usage examples
- Configuration options
- Extension points
- Contributing guidelines
- License information
