#!/usr/bin/env python3
"""
OmnitrAIce Web UI - Unified Revolutionary Project Generation Interface
"""

import asyncio
import os
import json
import logging
import traceback
from datetime import datetime
from typing import Dict, Any, List

import gradio as gr

# Import core agent system with fallbacks for compatibility
try:
    from omnitrace.core.revolutionary_omniagent import UnifiedOmniAgent
except ImportError:
    try:
        from core.revolutionary_omniagent import UnifiedOmniAgent
    except ImportError:
        try:
            from revolutionary_omniagent import UnifiedOmniAgent
        except ImportError:
            from enhanced_omniagent import EnhancedOmniAgent as UnifiedOmniAgent

class OmnitrAIceWebUI:
    """
    Comprehensive Web Interface for OmnitrAIce Project Generation System
    """

    def __init__(self, agent=None, model_name: str = "deepseek-r1:1.5b"):
        """
        Initialize the Web UI with the UnifiedOmniAgent
        
        Args:
            agent: Optional pre-initialized agent
            model_name (str): LLM model to use for project generation
        """
        self.logger = self._setup_logger()
        self.agent = agent if agent else UnifiedOmniAgent(model_name)
        self.app = None

    def _setup_logger(self) -> logging.Logger:
        """
        Set up logging for the Web UI
        
        Returns:
            logging.Logger: Configured logger instance
        """
        logger = logging.getLogger("OmnitrAIceWebUI")
        logger.setLevel(logging.INFO)
        
        # Ensure logs directory exists
        os.makedirs("logs", exist_ok=True)
        
        # File Handler
        file_handler = logging.FileHandler(
            f"logs/web_ui_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        file_handler.setLevel(logging.INFO)
        
        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger

    def create_ui(self):
        """
        Create the Gradio Web Interface for OmnitrAIce
        """
        with gr.Blocks(title="OmnitrAIce: Revolutionary Project Generation") as app:
            # Main Title and Description
            gr.Markdown("# 🚀 OmnitrAIce: AI-Powered Project Generation")
            gr.Markdown("## Revolutionary Software Development Framework")
            
            # Initialize output components first to avoid reference errors
            with gr.Row(visible=False) as status_row:
                self.output_status = gr.Textbox(label="Status", interactive=False)
                self.output_log = gr.Textbox(label="Detailed Log", interactive=False)
            
            # Tabbed Interface
            with gr.Tabs():
                # Project Creation Tab
                with gr.TabItem("Create Project"):
                    self._create_project_tab()
                
                # Agent Customization Tab
                with gr.TabItem("Agent Customization"):
                    self._agent_customization_tab()
                
                # Template Management Tab
                with gr.TabItem("Template Management"):
                    self._template_management_tab()
                    
                # Revolutionary Settings Tab
                with gr.TabItem("Revolutionary Settings"):
                    self._revolutionary_settings_tab()
            
            # Status and Output Section (now visible)
            status_row.visible = True
            
        self.app = app
        return app

    def _create_project_tab(self):
        """
        Create the Project Creation Tab UI Components
        """
        with gr.Row():
            with gr.Column():
                self.project_name = gr.Textbox(label="Project Name")
                self.project_desc = gr.Textbox(label="Project Description", lines=4)
                
                # Agent Selection
                available_agents = []
                try:
                    if hasattr(self.agent, "get_available_agents"):
                        available_agents = self.agent.get_available_agents()
                    else:
                        available_agents = ["ceo", "cto", "architect", "developer", "filesystem"]
                except Exception as e:
                    self.logger.error(f"Error getting available agents: {e}")
                
                with gr.Accordion("Agent Configuration", open=False):
                    self.agent_selection = gr.CheckboxGroup(
                        choices=available_agents,
                        label="Select Agents for Project Generation", 
                        value=available_agents
                    )
                
                # Output components that need to be defined first
                self.output_dir = gr.Textbox(label="Output Directory", interactive=False, visible=False)
                self.generated_files = gr.Dataframe(
                    headers=["File", "Path"],
                    label="Generated Project Files",
                    visible=False
                )
                
                self.create_btn = gr.Button("Generate Project", variant="primary")
                self.create_btn.click(fn=self._create_project, inputs=[self.project_name, self.project_desc], 
                                     outputs=[self.output_status, self.output_log, self.output_dir, self.generated_files])
            
            with gr.Column():
                # Make the output components visible in this column
                self.output_dir.visible = True
                self.generated_files.visible = True

    def _agent_customization_tab(self):
        """
        Create the Agent Customization Tab UI Components
        """
        with gr.Row():
            with gr.Column():
                self.agent_type = gr.Dropdown(
                    choices=self.agent.get_available_agents(),
                    label="Select Agent Type", 
                    value=self.agent.get_available_agents()[0] if self.agent.get_available_agents() else None
                )
                
                # Dynamic Agent Parameters
                self.focus_areas = gr.Dropdown(
                    multiselect=True,
                    label="Focus Areas",
                    choices=[
                        "First-principles analysis",
                        "Revolutionary design",
                        "10x improvement opportunities",
                        "Constraint elimination",
                        "Physics-based approach"
                    ]
                )
                self.strategy_level = gr.Dropdown(
                    choices=["low", "medium", "high"],
                    label="Strategy Level",
                    value="high"
                )
                self.detail_level = gr.Dropdown(
                    choices=["low", "medium", "high"],
                    label="Detail Level",
                    value="medium"
                )
                
                gr.Markdown("### Revolutionary Parameters")
                self.revolution_level = gr.Dropdown(
                    choices=["moderate", "high", "maximum"],
                    label="Revolution Level",
                    value="maximum"
                )
                self.constraint_elimination = gr.Dropdown(
                    choices=["cautious", "moderate", "aggressive"],
                    label="Constraint Elimination",
                    value="aggressive"
                )
                
                self.update_params_btn = gr.Button("Update Agent Parameters")
                self.update_params_btn.click(fn=self._update_agent_parameters, 
                                           inputs=[self.agent_type, self.revolution_level, 
                                                  self.constraint_elimination, self.strategy_level, 
                                                  self.detail_level, self.focus_areas],
                                           outputs=[self.output_status])

    def _template_management_tab(self):
        """
        Create the Template Management Tab UI Components
        """
        with gr.Row():
            with gr.Column():
                # Custom Template Creation
                self.custom_template_name = gr.Textbox(label="Custom Template Name")
                self.template_editor = gr.Textbox(label="Template Content", lines=10)
                self.save_template_btn = gr.Button("Save Custom Template")
                self.save_template_btn.click(fn=self._save_template, 
                                           inputs=[self.custom_template_name, self.template_editor],
                                           outputs=[self.output_status])
            
            with gr.Column():
                # Existing Templates Management
                self.existing_templates = gr.Dropdown(
                    choices=self._get_custom_templates(),
                    label="Existing Templates"
                )
                self.load_template_btn = gr.Button("Load Template")
                self.load_template_btn.click(fn=self._load_template, 
                                           inputs=[self.existing_templates],
                                           outputs=[self.template_editor])
                
                self.delete_template_btn = gr.Button("Delete Template")
                self.delete_template_btn.click(fn=self._delete_template, 
                                             inputs=[self.existing_templates],
                                             outputs=[self.output_status, self.existing_templates])

    def _revolutionary_settings_tab(self):
        """
        Create the Revolutionary Settings Tab UI Components
        """
        with gr.Row():
            with gr.Column():
                gr.Markdown("### Revolutionary Generation Options")
                
                # Code Generation Setting
                self.enable_code_gen = gr.Checkbox(
                    label="Enable Revolutionary Code Generation",
                    value=True
                )
                
                # File Structure Setting
                self.enable_file_structure = gr.Checkbox(
                    label="Enable Revolutionary File Structure Generation",
                    value=True
                )
                
                # Metrics Setting
                self.enable_metrics = gr.Checkbox(
                    label="Include Revolutionary Metrics Analysis",
                    value=True
                )
                
                self.update_settings_btn = gr.Button("Update Revolutionary Settings")
                self.update_settings_btn.click(fn=self._update_revolutionary_settings, 
                                             inputs=[self.enable_code_gen, self.enable_file_structure, self.enable_metrics],
                                             outputs=[self.output_status])

    # Implementation of UI action handlers
    def _create_project(self, name, description):
        """Create a new revolutionary project"""
        try:
            if not name or not description:
                return "Error: Project name and description are required", "Please provide both a project name and description", "", None
            
            self.logger.info(f"Creating revolutionary project: {name}")
            
            # Call the agent's create_project method
            result = asyncio.run(self.agent.create_project(name, description))
            
            if result.get("status") == "success":
                # Prepare the files list for the dataframe
                output_dir = result.get("output_dir", "")
                files_list = []
                
                if "generated_files" in result:
                    for file_path in result["generated_files"]:
                        file_name = os.path.basename(file_path)
                        files_list.append([file_name, file_path])
                else:
                    # If no explicit files list, use artifacts
                    for file_key, file_path in result.get("artifacts", {}).items():
                        full_path = os.path.join(output_dir, file_path)
                        files_list.append([file_key, full_path])
                
                return "Success: Project created successfully", f"Project created at: {output_dir}", output_dir, files_list
            else:
                return f"Error: {result.get('error', 'Unknown error')}", traceback.format_exc(), "", None
                
        except Exception as e:
            self.logger.error(f"Error creating project: {str(e)}")
            return f"Error: {str(e)}", traceback.format_exc(), "", None

    def _update_agent_parameters(self, agent_type, revolution_level, constraint_elimination, strategy_level, detail_level, focus_areas):
        """Update the agent parameters"""
        try:
            if hasattr(self.agent, "set_revolution_level"):
                self.agent.set_revolution_level(revolution_level)
                
            if hasattr(self.agent, "set_constraint_elimination"):
                self.agent.set_constraint_elimination(constraint_elimination)
                
            # You might need to implement these methods in the agent classes
            if hasattr(self.agent, "set_strategy_level"):
                self.agent.set_strategy_level(strategy_level)
                
            if hasattr(self.agent, "set_detail_level"):
                self.agent.set_detail_level(detail_level)
                
            return f"Successfully updated parameters for {agent_type} agent"
        except Exception as e:
            self.logger.error(f"Error updating agent parameters: {str(e)}")
            return f"Error: {str(e)}"

    def _save_template(self, template_name, template_content):
        """Save a custom template"""
        try:
            if not template_name or not template_content:
                return "Error: Template name and content are required"
            
            # You might need to implement this method
            if hasattr(self.agent, "save_custom_template"):
                success = self.agent.save_custom_template(template_name, template_content)
                if success:
                    return f"Successfully saved template: {template_name}"
                else:
                    return f"Failed to save template: {template_name}"
            else:
                return "Error: Agent does not support custom templates"
        except Exception as e:
            self.logger.error(f"Error saving template: {str(e)}")
            return f"Error: {str(e)}"

    def _load_template(self, template_name):
        """Load a custom template"""
        try:
            if not template_name:
                return ""
            
            # You might need to implement this method
            if hasattr(self.agent, "get_template"):
                template = self.agent.get_template(template_name)
                return template
            else:
                return ""
        except Exception as e:
            self.logger.error(f"Error loading template: {str(e)}")
            return f"Error: {str(e)}"

    def _delete_template(self, template_name):
        """Delete a custom template"""
        try:
            if not template_name:
                return "Error: No template selected", self._get_custom_templates()
            
            templates_dir = os.path.join("config", "templates")
            template_path = os.path.join(templates_dir, f"{template_name}_template.json")
            
            if os.path.exists(template_path):
                os.remove(template_path)
                return f"Successfully deleted template: {template_name}", self._get_custom_templates()
            else:
                return f"Template not found: {template_name}", self._get_custom_templates()
        except Exception as e:
            self.logger.error(f"Error deleting template: {str(e)}")
            return f"Error: {str(e)}", self._get_custom_templates()

    def _update_revolutionary_settings(self, enable_code_gen, enable_file_structure, enable_metrics):
        """Update revolutionary settings"""
        try:
            if hasattr(self.agent, "enable_code_generation"):
                self.agent.enable_code_generation(enable_code_gen)
                
            if hasattr(self.agent, "enable_file_structure_generation"):
                self.agent.enable_file_structure_generation(enable_file_structure)
                
            # You might need to implement this method
            if hasattr(self.agent, "enable_metrics"):
                self.agent.enable_metrics(enable_metrics)
                
            return "Successfully updated revolutionary settings"
        except Exception as e:
            self.logger.error(f"Error updating revolutionary settings: {str(e)}")
            return f"Error: {str(e)}"

    def _get_custom_templates(self):
        """Get a list of custom templates"""
        try:
            templates_dir = os.path.join("config", "templates")
            if not os.path.exists(templates_dir):
                return []
            
            templates = []
            for file_name in os.listdir(templates_dir):
                if file_name.endswith("_template.json"):
                    templates.append(file_name.split("_")[0])
            
            return templates
        except Exception:
            return []

    def launch(self, share=False, debug=False):
        """
        Launch the Web UI
        
        Args:
            share (bool): Whether to create a public share link
            debug (bool): Enable debug mode
        """
        if not self.app:
            self.create_ui()
        
        try:
            self.app.launch(share=share, debug=debug)
        except Exception as e:
            self.logger.error(f"Error launching Web UI: {e}")
            traceback.print_exc()

def main():
    """
    Main entry point for the OmnitrAIce Web UI
    """
    import argparse

    parser = argparse.ArgumentParser(description="OmnitrAIce Web Interface")
    parser.add_argument(
        "--model", 
        default="deepseek-r1:1.5b", 
        help="Specify the LLM model to use"
    )
    parser.add_argument(
        "--share", 
        action="store_true", 
        help="Create a publicly shareable link"
    )
    parser.add_argument(
        "--debug", 
        action="store_true", 
        help="Enable debug mode"
    )

    args = parser.parse_args()

    ui = OmnitrAIceWebUI(model_name=args.model)
    ui.launch(share=args.share, debug=args.debug)

if __name__ == "__main__":
    main()
