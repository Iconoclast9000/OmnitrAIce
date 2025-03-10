# OmnitrAIce Execution Methods

> Designed by **CraigFineTuned** - Optimized for small, efficient models

This document outlines all available methods for running the OmnitrAIce system, their advantages, and use cases.

## Primary Execution Methods

### 1. Universal Web UI Launcher (Recommended)

**Command:**
```bash
python run_web_ui.py
```

**Description:**
- Most reliable way to launch the web interface
- Handles path issues automatically
- Provides progressive fallbacks if one UI method fails
- Works regardless of current directory
- Detailed logging for troubleshooting

**Best for:**
- First-time users
- When you want to use the graphical interface
- When you need the most reliable approach

**Features:**
- Attempts multiple UI approaches with fallbacks
- Comprehensive error handling
- Clear console output
- Detailed logging for every step

### 2. Command Line Project Generation

**Command:**
```bash
python omnitrace/run.py --project "Project Name" --description "Description" [options]
```

**Description:**
- Direct project generation from command line
- Full access to all configuration options
- No web browser required
- Ideal for scripted or automated use

**Best for:**
- Batch processing
- Integration with scripts or other tools
- Server environments without UI
- When you know exactly what you want to generate

**Options:**
- `--project`: Project name
- `--description`: Project description
- `--model`: LLM model to use (default: deepseek-r1:1.5b)
- `--revolution-level`: Level of revolutionary thinking (moderate/high/maximum)
- `--constraint-elimination`: Level of constraint elimination (cautious/moderate/aggressive)
- `--code-gen`: Enable code generation
- `--no-code-gen`: Disable code generation
- `--config`: Path to configuration file (YAML/JSON)
- `--verbose`: Enable verbose logging

### 3. Main Launcher with Web UI Option

**Command:**
```bash
python omnitrace/run.py --web
```

**Description:**
- Launches web interface via the main entry point
- Uses the same launcher as command-line generation
- Good alternative if universal launcher has issues

**Best for:**
- When you prefer using the main entry point consistently
- As a fallback if the universal launcher fails

## Alternative Execution Methods

### 4. Python Module Execution

**Command:**
```bash
python -m omnitrace.run [options]
```

**Description:**
- Executes the system as a Python module
- Useful for certain development environments
- Same functionality as the main launcher

**Best for:**
- Development and testing
- When working within the Python package structure

### 5. Installed Package Execution (After pip install)

**Command:**
```bash
omnitrace [options]
```

**Description:**
- Runs OmnitrAIce as an installed package
- Available after installing via pip
- Shortest and simplest command

**Best for:**
- Regular users after installation
- Clean environments without the full repository
- Most portable approach

## Command Line Options Reference

All execution methods that use the core run.py support these options:

| Option | Description | Default | Example |
|--------|-------------|---------|---------|
| `--model` | LLM model to use | deepseek-r1:1.5b | `--model llama2:7b` |
| `--web` | Launch web interface | - | `--web` |
| `--project` | Project name to create | - | `--project "My App"` |
| `--description` | Project description | - | `--description "A revolutionary app"` |
| `--code-gen` | Enable code generation | - | `--code-gen` |
| `--no-code-gen` | Disable code generation | - | `--no-code-gen` |
| `--config` | Path to config file | - | `--config config/my_config.yaml` |
| `--revolution-level` | Level of revolutionary thinking | maximum | `--revolution-level moderate` |
| `--constraint-elimination` | Level of constraint elimination | aggressive | `--constraint-elimination cautious` |
| `--verbose` | Enable verbose logging | - | `--verbose` |

## Examples

### Create a Project with Maximum Revolution

```bash
python omnitrace/run.py --project "Quantum Communication App" --description "A revolutionary app that uses quantum entanglement for instant messaging across any distance" --revolution-level maximum --constraint-elimination aggressive
```

### Launch Web UI with Custom Model

```bash
python run_web_ui.py --model llama2:7b
```

### Use Configuration File

```bash
python omnitrace/run.py --project "AI Dashboard" --description "A dashboard for monitoring AI systems" --config config/config_files/custom_config.yaml
```

### Installed Package with Web UI

```bash
omnitrace --web --verbose
```

## Recommended Practices

1. **For general use**: Start with the Universal Web UI Launcher (`python run_web_ui.py`)
2. **For automation**: Use the Command Line Project Generation
3. **For development**: Use Python Module Execution
4. **For regular use after installation**: Use the Installed Package Execution

## Troubleshooting

If one execution method fails, try an alternative:

1. If `run_web_ui.py` fails, try `python omnitrace/run.py --web`
2. If the web UI doesn't load, try command-line generation
3. If all else fails, check the logs in the `logs/` directory

For detailed logs of any execution method, add the `--verbose` flag when available.
