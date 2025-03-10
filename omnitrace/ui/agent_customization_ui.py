"""
Agent Customization UI - Gradio interface for customizing OmnitrAIce agents
"""

import asyncio
import os
import logging
from typing import Dict, Any, List, Optional
import gradio as gr

# Try imports with fallbacks for compatibility
try:
    from omnitrace.core.enhanced_omniagent import EnhancedOmniAgent
except ImportError:
    try:
        from core.enhanced_omniagent import EnhancedOmniAgent
    except ImportError:
        from enhanced_omniagent import EnhancedOmniAgent

class AgentCustomizationUI:
    """Gradio UI for agent customization"""

    def __init__(self, agent: EnhancedOmniAgent):
        """Initialize the UI with an enhanced agent
        
        Args:
            agent: An instance of EnhancedOmniAgent
        """
        self.agent = agent
        self.app = None
        self.logger = logging.getLogger(__name__)

    def _get_agent_types(self) -> List[str]:
        """Get all available agent types"""
        return list(self.agent.agent_templates.keys())

    def load_agent_template(self, agent_type: str) -> str:
        """Load the template for the selected agent type"""
        template = self.agent.get_template(agent_type)
        if isinstance(template, dict):
            return template.get("template", "")
        return template

    def save_agent_template(self, agent_type: str, template: str) -> str:
        """Save the template for the selected agent type"""
        success = self.agent.save_custom_template(agent_type, template)
        return "Template saved successfully" if success else "Failed to save template"
    
    def create_project_wrapped(self, name: str, desc: str) -> Dict[str, Any]:
        """Wrapper for create_project to handle errors"""
        try:
            result = asyncio.run(self.agent.create_project(name, desc))
            return result
        except Exception as e:
            self.logger.error(f"Error creating project: {str(e)}")
            return {"status": "error", "error": str(e)}

    def create_ui(self):
        """Create and launch the Gradio UI"""
        with gr.Blocks(title="OmnitrAIce Agent Customization") as app:
            gr.Markdown("# OmnitrAIce Agent Customization")

            with gr.Row():
                with gr.Column(scale=1):
                    agent_types = self._get_agent_types()
                    agent_type = gr.Dropdown(
                        choices=agent_types,
                        label="Select Agent Type",
                        value=agent_types[0] if agent_types else None
                    )
                    template_editor = gr.Textbox(
                        label="Agent Template", 
                        placeholder="Agent template will appear here...", 
                        lines=15
                    )
                    save_template_btn = gr.Button("Save Template")
                    save_result = gr.Textbox(label="Save Result")

                    # Load template when agent type changes
                    agent_type.change(
                        fn=self.load_agent_template, 
                        inputs=[agent_type], 
                        outputs=[template_editor]
                    )

                    # Save template when button is clicked
                    save_template_btn.click(
                        fn=self.save_agent_template,
                        inputs=[agent_type, template_editor],
                        outputs=[save_result]
                    )

                with gr.Column(scale=1):
                    gr.Markdown("## Project Creation")
                    project_name = gr.Textbox(label="Project Name")
                    project_desc = gr.Textbox(label="Project Description", lines=5) 
                    create_btn = gr.Button("Create Project")
                    create_result = gr.JSON(label="Creation Result")

                    # Create project when button is clicked
                    create_btn.click(
                        fn=self.create_project_wrapped,
                        inputs=[project_name, project_desc],
                        outputs=[create_result]
                    )
            
            gr.Markdown("## Revolutionary Settings")
            
            with gr.Row():
                with gr.Column():
                    revolution_level = gr.Radio(
                        choices=["moderate", "high", "maximum"],
                        label="Revolution Level",
                        value="maximum"
                    )
                    
                    constraint_elimination = gr.Radio(
                        choices=["cautious", "moderate", "aggressive"],
                        label="Constraint Elimination",
                        value="aggressive"
                    )
                    
                    if hasattr(self.agent, "set_revolution_level"):
                        update_settings_btn = gr.Button("Update Settings")
                        update_result = gr.Textbox(label="Update Result")
                        
                        # Update settings when button is clicked
                        def update_settings(level, elimination):
                            try:
                                self.agent.set_revolution_level(level)
                                
                                if hasattr(self.agent, "set_constraint_elimination"):
                                    self.agent.set_constraint_elimination(elimination)
                                    
                                return "Settings updated successfully"
                            except Exception as e:
                                return f"Error updating settings: {str(e)}"
                        
                        update_settings_btn.click(
                            fn=update_settings,
                            inputs=[revolution_level, constraint_elimination],
                            outputs=[update_result]
                        )
            
            gr.Markdown("## Generated Projects")
            
            # List all generated projects
            def list_projects():
                projects_dir = os.path.join(os.getcwd(), "projects")
                if not os.path.exists(projects_dir):
                    return "No projects generated yet."

                projects = os.listdir(projects_dir)
                if not projects:
                    return "No projects generated yet."
                
                result = "### Generated Projects\n\n"
                for project in projects:
                    result += f"- {project}\n"
                return result

            projects_list = gr.Markdown(list_projects())
            refresh_btn = gr.Button("Refresh Projects List")
            refresh_btn.click(fn=list_projects, inputs=[], outputs=[projects_list])

            self.app = app

    def launch(self, **kwargs):
        """Launch the UI"""
        if not self.app:
            self.create_ui()
        self.app.launch(**kwargs)
