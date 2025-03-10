# OmnitrAIce Migration Guide

This guide helps users migrate from previous versions of OmnitrAIce to the new unified system.

## Overview of Changes

The OmnitrAIce project has been unified into a single, cohesive system with:

1. A single entry point (`run.py`)
2. An integrated agent system (`revolutionary_omniagent.py`)
3. Comprehensive configuration options (CLI args and YAML/JSON files)
4. Enhanced revolutionary capabilities (code generation, file structure)

## Migration Steps

### From Basic OmniAgent

If you were using the basic `omniagent.py`:

```python
# Old approach
from omniagent import OmniAgent
agent = OmniAgent()
result = await agent.create_project("My Project", "Description")
```

New approach:

```python
# New approach
from revolutionary_omniagent import UnifiedOmniAgent
agent = UnifiedOmniAgent()
result = await agent.create_project("My Project", "Description")
```

Command line:

```bash
# Old approach
python omniagent.py

# New approach
python run.py
```

### From Enhanced OmniAgent

If you were using `enhanced_omniagent.py`:

```python
# Old approach
from enhanced_omniagent import EnhancedOmniAgent
agent = EnhancedOmniAgent()
```

New approach:

```python
# New approach
from revolutionary_omniagent import UnifiedOmniAgent
agent = UnifiedOmniAgent()
```

Command line:

```bash
# Old approach
python run_omnitrace.py

# New approach
python run.py
```

### From Revolutionary OmniAgent

If you were using the older revolutionary approach:

```bash
# Old approach
python run_revolutionaryce.py --project "Project" --description "Description"

# New approach
python run.py --project "Project" --description "Description"
```

## Configuration Changes

The unified system supports more comprehensive configuration:

### Command Line Arguments

New command line arguments:

```bash
python run.py --help
```

Key new options:
- `--revolution-level`: Control level of revolutionary thinking
- `--constraint-elimination`: Control constraint elimination aggressiveness
- `--config`: Specify configuration file
- `--verbose`: Enable detailed logging

### Configuration Files

You can now use YAML or JSON configuration files:

```bash
python run.py --config config/config_files/default_config.yaml
```

Example config:

```yaml
revolution_level: "maximum"
constraint_elimination: "aggressive"
generation:
  enable_code_gen: true
  enable_file_structure: true
```

## Web UI Changes

The web interface now has a unified approach:

```bash
# Launch web UI
python run.py --web
```

### New UI Features

- Tabbed interface with project creation, agent customization, and template management
- Advanced parameter configuration
- Revolutionary metrics display
- Config file management

## API Changes

### Revolutionary Metrics

New revolutionary metrics are available in the project creation result:

```python
result = await agent.create_project("Project", "Description")
metrics = result.get("revolutionary_metrics", {})
print(f"Innovation score: {metrics.get('first_principles_metrics', {}).get('innovation_score', 0)}")
```

### Enhanced Capabilities

You can check which enhanced capabilities were used:

```python
result = await agent.create_project("Project", "Description")
capabilities = result.get("enhanced_capabilities", {})
print(f"Used code generation: {capabilities.get('code_generation', False)}")
```

## Common Migration Issues

### Missing Dependencies

The unified system requires additional dependencies:

```
pip install pyyaml pytest-asyncio
```

### Template Compatibility

If you have custom templates, you may need to update them for the new system:

1. Review the template format in the `config/templates` directory
2. Ensure first-principles thinking sections are included
3. Update placeholder variables if necessary

### Legacy Files

The following files are now considered legacy:
- `run_omnitrace.py` (replaced by `run.py`)
- `run_revolutionaryce.py` (replaced by `run.py`)

These files have been moved to the `legacy` directory for reference but should not be used.

## Upgrading Projects

Projects generated with previous versions will still work, but you can enhance them with:

```bash
python run.py --project "Existing Project" --description "$(cat projects/ExistingProject/docs/vision.md)" --revolution-level maximum
```

This will regenerate the project with the unified system's revolutionary capabilities.

## Getting Help

If you encounter issues during migration:
1. Check the logs in the `logs` directory
2. Review the documentation in the `docs` directory
3. Examine the example configuration files in `config/config_files`
