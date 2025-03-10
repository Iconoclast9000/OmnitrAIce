# OmnitrAIce Web UI Guide

## Overview

OmnitrAIce provides multiple web interface options for interacting with the system, each with different capabilities. This guide explains the available interfaces, their features, and how to use them.

## Launch Methods

### Universal Web UI Launcher (Recommended)

**Description**:
- Consolidated launcher that handles all path issues
- Tries multiple UI approaches with progressive fallbacks
- Works consistently regardless of current directory
- Provides detailed logging for troubleshooting

**Launch Method**:
```bash
# Universal Web UI launcher - most reliable method
python run_web_ui.py
```

### Alternative Launch Methods

**Via main launcher**:
```bash
# Launch through the main entry point
python omnitrace/run.py --web
```

## Interface Components

### Revolutionary Web UI Tabs

1. **Create Project**
   - Project name and description input
   - Agent selection for project generation
   - Output directory and file list display

2. **Agent Customization**
   - Agent type selection
   - Focus area configuration
   - Strategy and detail level settings
   - Revolutionary parameters adjustment

3. **Template Management**
   - Template creation and editing
   - Loading existing templates
   - Deleting templates

4. **Revolutionary Settings**
   - Code generation toggle
   - File structure generation toggle
   - Metrics analysis configuration

## Using the Web UI

### Creating a Project

1. Navigate to the "Create Project" tab
2. Enter a project name and description
3. (Optional) Configure which agents to use in the "Agent Configuration" accordion
4. Click "Generate Project"
5. View the generated files in the output panel

### Customizing Agents

1. Navigate to the "Agent Customization" tab
2. Select an agent type from the dropdown
3. Configure parameters:
   - Select focus areas
   - Set strategy and detail levels
   - Configure revolution level and constraint elimination
4. Click "Update Agent Parameters"

### Managing Templates

1. Navigate to the "Template Management" tab
2. To create a new template:
   - Enter a template name
   - Write or paste template content
   - Click "Save Custom Template"
3. To load an existing template:
   - Select from the dropdown
   - Click "Load Template"
4. To delete a template:
   - Select from the dropdown
   - Click "Delete Template"

### Configuring Revolutionary Settings

1. Navigate to the "Revolutionary Settings" tab
2. Toggle options:
   - Enable/disable code generation
   - Enable/disable file structure generation
   - Enable/disable metrics analysis
3. Click "Update Revolutionary Settings"

## Troubleshooting

If you encounter issues with the web interface, try these solutions:

1. **Web UI Fails to Launch**:
   - Always use the Universal Web UI Launcher: `python run_web_ui.py`
   - Check logs in the `logs/` directory for detailed error information
   - Ensure Gradio is properly installed: `pip install gradio>=3.40.0`

2. **Missing Functionality**:
   - Different UIs have different capabilities depending on which version is loaded
   - The Universal Launcher will try multiple approaches to ensure something works

3. **Component Reference Errors**:
   - These are fixed in v1.1.0 with improved component initialization
   - The Universal Launcher handles these errors automatically

## Version History

- **v1.0.0**: Initial web interface implementation
- **v1.1.0**: Enhanced web interface with improved error handling, component initialization, and backward compatibility
