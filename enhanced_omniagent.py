import asyncio
import os
import json
import logging
from typing import Dict, Any, List, Optional
import gradio as gr
from functools import partial

# Import existing OmniAgent
from omniagent import OmniAgent


class EnhancedOmniAgent(OmniAgent):
    """Enhanced OmniAgent with customizable agent interface"""

    def __init__(self, model_name: str = "deepseek-r1:1.5b"):
        super().__init__(model_name)

        # Store customizable agent templates
        self.custom_templates = {}

        # Load any saved custom templates
        self._load_custom_templates()

        # Agent parameters for customization
        self.agent_parameters = {
            "ceo": {
                "focus_areas": [
                    "Project requirements",
                    "Resource allocation",
                    "Timeline planning",
                    "Risk assessment",
                ],
                "strategy_level": "high",
                "detail_level": "medium",
                "considerations": [],
            },
            "architect": {
                "focus_areas": [
                    "System architecture",
                    "Component design",
                    "Technical patterns",
                    "Integration points",
                ],
                "strategy_level": "medium",
                "detail_level": "high",
                "considerations": [],
            },
            "developer": {
                "focus_areas": [
                    "Code structure",
                    "File organization",
                    "Implementation details",
                    "Best practices",
                ],
                "strategy_level": "low",
                "detail_level": "high",
                "considerations": [],
            },
        }

        # Default agent parameter options
        self.parameter_options = {
            "strategy_level": ["low", "medium", "high"],
            "detail_level": ["low", "medium", "high"],
        }

    def _load_custom_templates(self):
        """Load saved custom templates"""
        templates_dir = os.path.join("config", "templates")
        os.makedirs(templates_dir, exist_ok=True)

        # For each agent type, check if a custom template exists
        for agent_type in self.agent_templates.keys():
            template_path = os.path.join(templates_dir, f"{agent_type}_template.json")
            if os.path.exists(template_path):
                try:
                    with open(template_path, "r", encoding="utf-8") as f:
                        self.custom_templates[agent_type] = json.load(f)
                        # Update the main template
                        self.agent_templates[agent_type] = self.custom_templates[
                            agent_type
                        ]["template"]
                        # Update parameters if available
                        if "parameters" in self.custom_templates[agent_type]:
                            self.agent_parameters[agent_type] = self.custom_templates[
                                agent_type
                            ]["parameters"]
                except Exception as e:
                    self.logger.error(
                        f"Failed to load custom template for {agent_type}: {str(e)}"
                    )

    def save_custom_template(
        self, agent_type: str, template: str, parameters: Dict[str, Any] = None
    ):
        """Save a custom template for an agent type"""
        try:
            templates_dir = os.path.join("config", "templates")
            os.makedirs(templates_dir, exist_ok=True)

            template_path = os.path.join(templates_dir, f"{agent_type}_template.json")

            # Store both template and parameters
            template_data = {
                "template": template,
                "parameters": parameters or self.agent_parameters[agent_type],
            }

            with open(template_path, "w", encoding="utf-8") as f:
                json.dump(template_data, f, indent=2, ensure_ascii=False)

            # Update in memory
            self.custom_templates[agent_type] = template_data
            self.agent_templates[agent_type] = template

            # Update agent chain
            from langchain_core.prompts import ChatPromptTemplate

            self.agent_chains[agent_type] = (
                ChatPromptTemplate.from_template(template) | self.llm
            )

            return True
        except Exception as e:
            self.logger.error(
                f"Failed to save custom template for {agent_type}: {str(e)}"
            )
            return False

    def get_template(self, agent_type: str) -> str:
        """Get the current template for an agent type"""
        return self.agent_templates.get(agent_type, "")

    def get_agent_parameters(self, agent_type: str) -> Dict[str, Any]:
        """Get the current parameters for an agent type"""
        return self.agent_parameters.get(agent_type, {})

    def update_agent_parameters(self, agent_type: str, parameters: Dict[str, Any]):
        """Update the parameters for an agent type"""
        if agent_type in self.agent_parameters:
            self.agent_parameters[agent_type].update(parameters)
            return True
        return False

    def generate_template_from_parameters(self, agent_type: str) -> str:
        """Generate a template based on current parameters"""
        if agent_type not in self.agent_parameters:
            return self.agent_templates.get(agent_type, "")

        params = self.agent_parameters[agent_type]

        # Base template structure
        template = f"""
        You are the {agent_type.upper()} Agent responsible for {'high-level project vision' if agent_type == 'ceo' else 'technical design' if agent_type == 'architect' else 'implementation'}.
        Current Project Context: {{context}}
        Task: {{task}}
        """

        # Add agent-specific context
        if agent_type == "architect":
            template += "CEO's Vision: {vision}\n\n"
        elif agent_type == "developer":
            template += "Architecture Design: {design}\n\n"

        # Add focus areas
        template += "Focus on:\n"
        for i, focus in enumerate(params["focus_areas"], 1):
            template += f"{i}. {focus}\n"

        # Add strategy level context
        if params["strategy_level"] == "high":
            template += "\nFocus on strategic, high-level planning.\n"
        elif params["strategy_level"] == "medium":
            template += "\nBalance strategic planning with tactical considerations.\n"
        else:
            template += "\nFocus on detailed, tactical implementation.\n"

        # Add detail level context
        if params["detail_level"] == "high":
            template += "Provide comprehensive, detailed analysis.\n"
        elif params["detail_level"] == "medium":
            template += "Provide balanced analysis with key details.\n"
        else:
            template += "Provide concise, high-level analysis.\n"

        # Add additional considerations
        if params["considerations"]:
            template += "\nAdditional considerations:\n"
            for consideration in params["considerations"]:
                template += f"- {consideration}\n"

        # Add previous context
        if agent_type == "ceo":
            template += "\nPrevious Decisions: {decisions}\n"
        elif agent_type == "architect":
            template += "\nPrevious Designs: {designs}\n"
        elif agent_type == "developer":
            template += "\nPrevious Work: {work}\n"

        # Add closing instruction
        template += f"\nProvide your {'analysis and decisions' if agent_type == 'ceo' else 'technical design decisions' if agent_type == 'architect' else 'specific implementation details'}.\n"

        return template


class AgentCustomizationUI:
    """Gradio UI for agent customization"""

    def __init__(self, agent: EnhancedOmniAgent):
        self.agent = agent
        self.app = None

    def _get_agent_types(self) -> List[str]:
        """Get all available agent types"""
        return list(self.agent.agent_templates.keys())

    def load_agent_template(self, agent_type: str) -> str:
        """Load the template for the selected agent type"""
        return self.agent.get_template(agent_type)

    def load_agent_parameters(self, agent_type: str) -> Dict[str, Any]:
        """Load the parameters for the selected agent type"""
        return self.agent.get_agent_parameters(agent_type)

    def save_agent_template(self, agent_type: str, template: str) -> str:
        """Save the template for the selected agent type"""
        success = self.agent.save_custom_template(agent_type, template)
        return "Template saved successfully" if success else "Failed to save template"

    def update_focus_areas(self, agent_type: str, focus_areas: str) -> str:
        """Update focus areas for an agent"""
        areas = [area.strip() for area in focus_areas.split("\n") if area.strip()]
        self.agent.update_agent_parameters(agent_type, {"focus_areas": areas})
        return "Focus areas updated"

    def update_strategy_level(self, agent_type: str, level: str) -> str:
        """Update strategy level for an agent"""
        self.agent.update_agent_parameters(agent_type, {"strategy_level": level})
        return f"Strategy level set to {level}"

    def update_detail_level(self, agent_type: str, level: str) -> str:
        """Update detail level for an agent"""
        self.agent.update_agent_parameters(agent_type, {"detail_level": level})
        return f"Detail level set to {level}"

    def update_considerations(self, agent_type: str, considerations: str) -> str:
        """Update additional considerations for an agent"""
        items = [item.strip() for item in considerations.split("\n") if item.strip()]
        self.agent.update_agent_parameters(agent_type, {"considerations": items})
        return "Considerations updated"

    def generate_template(self, agent_type: str) -> str:
        """Generate a template based on current parameters"""
        template = self.agent.generate_template_from_parameters(agent_type)
        return template
    
    def create_project_wrapped(self, name: str, desc: str) -> Dict[str, Any]:
        """Wrapper for create_project to handle errors"""
        try:
            result = asyncio.run(self.agent.create_project(name, desc))
            return result
        except Exception as e:
            return {"status": "error", "error": str(e)}

    def create_ui(self):
        """Create and launch the Gradio UI"""
        with gr.Blocks(title="OmnitrAIce Agent Customization") as app:
            gr.Markdown("# OmnitrAIce Agent Customization")

            with gr.Row():
                with gr.Column(scale=1):
                    agent_type = gr.Dropdown(
                        choices=self._get_agent_types(),
                        label="Select Agent Type",
                        value=(
                            self._get_agent_types()[0]
                            if self._get_agent_types()
                            else None
                        ),
                    )

                    with gr.Tab("Template Editor"):
                        template_editor = gr.TextArea(
                            label="Agent Template",
                            placeholder="Agent template will appear here...",
                            lines=15,
                        )

                        save_template_btn = gr.Button("Save Template")
                        save_result = gr.Textbox(label="Save Result")

                        # Load template when agent type changes
                        agent_type.change(
                            fn=self.load_agent_template,
                            inputs=[agent_type],
                            outputs=[template_editor],
                        )

                        # Save template when button is clicked
                        save_template_btn.click(
                            fn=self.save_agent_template,
                            inputs=[agent_type, template_editor],
                            outputs=[save_result],
                        )

                    with gr.Tab("Parameter Editor"):
                        with gr.Accordion("Focus Areas"):
                            focus_areas = gr.TextArea(
                                label="Focus Areas (one per line)", lines=5
                            )
                            update_focus_btn = gr.Button("Update Focus Areas")
                            focus_result = gr.Textbox(label="Result")

                        with gr.Accordion("Strategy Level"):
                            strategy_level = gr.Radio(
                                choices=self.agent.parameter_options["strategy_level"],
                                label="Strategy Level",
                            )
                            update_strategy_btn = gr.Button("Update Strategy Level")
                            strategy_result = gr.Textbox(label="Result")

                        with gr.Accordion("Detail Level"):
                            detail_level = gr.Radio(
                                choices=self.agent.parameter_options["detail_level"],
                                label="Detail Level",
                            )
                            update_detail_btn = gr.Button("Update Detail Level")
                            detail_result = gr.Textbox(label="Result")

                        with gr.Accordion("Additional Considerations"):
                            considerations = gr.TextArea(
                                label="Additional Considerations (one per line)",
                                lines=5,
                            )
                            update_consid_btn = gr.Button("Update Considerations")
                            consid_result = gr.Textbox(label="Result")

                        generate_template_btn = gr.Button(
                            "Generate Template from Parameters"
                        )

                        # Update event handlers for parameters
                        update_focus_btn.click(
                            fn=self.update_focus_areas,
                            inputs=[agent_type, focus_areas],
                            outputs=[focus_result],
                        )

                        update_strategy_btn.click(
                            fn=self.update_strategy_level,
                            inputs=[agent_type, strategy_level],
                            outputs=[strategy_result],
                        )

                        update_detail_btn.click(
                            fn=self.update_detail_level,
                            inputs=[agent_type, detail_level],
                            outputs=[detail_result],
                        )

                        update_consid_btn.click(
                            fn=self.update_considerations,
                            inputs=[agent_type, considerations],
                            outputs=[consid_result],
                        )

                        generate_template_btn.click(
                            fn=self.generate_template,
                            inputs=[agent_type],
                            outputs=[template_editor],
                        )

                        # Load parameters when agent type changes
                        def format_params_for_ui(params):
                            # Convert parameters to UI format
                            focus_text = "\n".join(params.get("focus_areas", []))
                            strategy = params.get("strategy_level", "medium")
                            detail = params.get("detail_level", "medium")
                            consid_text = "\n".join(params.get("considerations", []))
                            return focus_text, strategy, detail, consid_text

                        agent_type.change(
                            fn=lambda x: format_params_for_ui(
                                self.load_agent_parameters(x)
                            ),
                            inputs=[agent_type],
                            outputs=[
                                focus_areas,
                                strategy_level,
                                detail_level,
                                considerations,
                            ],
                        )

                with gr.Column(scale=1):
                    gr.Markdown("## Project Creation")
                    project_name = gr.Textbox(label="Project Name")
                    project_desc = gr.TextArea(label="Project Description", lines=5)
                    create_btn = gr.Button("Create Project")
                    create_result = gr.JSON(label="Creation Result")

                    # Create project when button is clicked
                    create_btn.click(
                        fn=self.create_project_wrapped,
                        inputs=[project_name, project_desc],
                        outputs=[create_result],
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
                    project_path = os.path.join(projects_dir, project)
                    if os.path.isdir(project_path):
                        readme_path = os.path.join(project_path, "README.md")
                        description = "No description available."
                        if os.path.exists(readme_path):
                            try:
                                with open(readme_path, "r", encoding="utf-8") as f:
                                    content = f.read()
                                    desc_match = content.split("## Project Overview")
                                    if len(desc_match) > 1:
                                        description = (
                                            desc_match[1].split("##")[0].strip()
                                        )
                            except:
                                pass

                        result += f"- **{project}**: {description}\n"

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


def main():
    """Main entry point for the enhanced OmnitrAIce system"""
    try:
        # Initialize the enhanced agent
        agent = EnhancedOmniAgent()

        # Create and launch the UI
        ui = AgentCustomizationUI(agent)
        ui.launch(share=False)

    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()