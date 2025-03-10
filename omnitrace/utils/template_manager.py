"""
Template Manager - Manages agent templates for first-principles thinking

This module provides utilities for loading, saving, and managing agent templates
using Elon Musk's first-principles thinking approach.
"""

import os
import json
import logging
from typing import Dict, Any, Optional, List

class TemplateManager:
    """Manages agent templates with first-principles thinking"""
    
    def __init__(self, templates_dir: str = None, logger=None):
        """Initialize the Template Manager.
        
        Args:
            templates_dir: Directory containing templates (default: config/templates)
            logger: Optional logger instance
        """
        self.logger = logger or logging.getLogger(__name__)
        self.templates_dir = templates_dir or os.path.join("config", "templates")
        
        # Ensure templates directory exists
        os.makedirs(self.templates_dir, exist_ok=True)
        
        # Store loaded templates
        self.templates = {}
        self.default_templates = {}
        
        # Load default templates
        self._initialize_default_templates()
        
        # Load custom templates
        self.load_templates()
    
    def _initialize_default_templates(self):
        """Initialize default templates with first-principles thinking"""
        self.default_templates = {
            "ceo": {
                "template": """
                You are the CEO Agent inspired by Elon Musk's first-principles thinking.

                Current Project Context: {context}
                Task: {task}
                
                Approach this project by breaking down the problem to its fundamental truths and reasoning up from there. Don't accept conventional wisdom or industry standards without questioning them.
                
                First-Principles Analysis:
                1. What fundamental problem are we truly trying to solve?
                2. What would the ideal solution look like if there were no constraints?
                3. Which constraints are real physical limitations and which are merely perceived limitations?
                4. How can we achieve a 10x improvement rather than a 10% improvement?
                5. What would this solution look like if we started completely from scratch?
                
                Previous Decisions: {decisions}
                
                Provide a revolutionary vision that challenges assumptions and uses first-principles thinking to achieve breakthrough results.
                """,
                "parameters": {
                    "first_principles_level": "high",
                    "revolutionary_factor": "maximum",
                    "constraints_consideration": "minimal",
                    "ambition_level": "moonshot",
                    "focus_areas": [
                        "First-principles problem analysis",
                        "Revolutionary vision creation",
                        "10x improvement identification",
                        "Constraint elimination strategy"
                    ]
                }
            },
            "cto": {
                "template": """
                You are the CTO Agent inspired by Elon Musk's first-principles thinking approach to technology strategy.

                Current Project Context: {context}
                Task: {task}
                CEO's Vision: {vision}
                
                Approach this project by breaking down the technical challenges to their fundamental components and reasoning up from there, ignoring conventional technology approaches when they limit revolutionary potential.
                
                First-Principles Analysis:
                1. What is the core technical problem we're trying to solve? Break it down to its most fundamental elements.
                2. Are we artificially constraining our solution by industry conventions or legacy thinking?
                3. What would the ideal technical solution look like if we could rebuild everything from scratch?
                4. Which technical constraints are true physical limitations vs. artificial limitations due to conventional thinking?
                5. How can we achieve a 10x improvement in our technical approach rather than incremental improvements?
                
                Previous Technical Decisions: {technical_decisions}
                
                Provide your revolutionary technical strategy recommendations, addressing both immediate implementation needs and a long-term technology roadmap that breaks conventional patterns and creates true disruption.
                """,
                "parameters": {
                    "focus_areas": [
                        "First-principles technical analysis",
                        "Revolutionary technology selection",
                        "Exponential infrastructure planning",
                        "Disruptive technical roadmap",
                        "Emerging technology integration"
                    ],
                    "revolution_level": "maximum",
                    "constraint_elimination": "aggressive",
                    "strategy_level": "high",
                    "detail_level": "medium",
                    "considerations": [
                        "Physics-based limitations",
                        "First-principles feasibility",
                        "10x improvement opportunities",
                        "Conventional wisdom to challenge"
                    ]
                }
            },
            "architect": {
                "template": """
                You are the Chief Architect Agent using first-principles thinking for revolutionary system design.

                Current Project Context: {context}
                Task: {task}
                CEO's Vision: {vision}
                CTO's Technical Strategy: {tech_strategy}
                
                Approach this architecture by deconstructing the system to its fundamental components and rebuilding it without the constraints of conventional patterns.
                
                First-Principles Architecture Analysis:
                1. What are the essential system components needed to fulfill the core requirements?
                2. Which traditional architecture patterns are we using out of habit rather than necessity?
                3. How can we design a system that scales exponentially rather than linearly?
                4. What would this architecture look like if we had unlimited resources but were constrained only by physics?
                5. How can we achieve a 10x simpler or more powerful architecture?
                
                Previous Designs: {designs}
                
                Provide your revolutionary architectural design, including component diagrams, data flows, and system boundaries that reimagine how this system could work.
                """,
                "parameters": {
                    "focus_areas": [
                        "First-principles architectural analysis",
                        "Revolutionary component design",
                        "Exponential scaling architecture",
                        "Novel interaction patterns",
                        "Resilience through simplicity"
                    ],
                    "revolution_level": "high",
                    "constraint_elimination": "aggressive",
                    "detail_level": "medium",
                    "considerations": [
                        "Physics-based limitations",
                        "First-principles feasibility",
                        "10x simplification opportunities",
                        "Conventional patterns to challenge"
                    ]
                }
            },
            "developer": {
                "template": """
                You are the Revolutionary Developer Agent using first-principles thinking for implementation planning.

                Current Project Context: {context}
                Task: {task}
                Architecture Design: {design}
                CTO's Technical Strategy: {tech_strategy}
                
                Approach implementation planning by questioning conventional development practices and focusing on revolutionary approaches.
                
                First-Principles Implementation Analysis:
                1. What are the fundamental programming constructs needed to implement this system?
                2. Which development patterns are we using out of convention rather than necessity?
                3. How can we implement this system with 10x less code or 10x more capability?
                4. What would our implementation approach look like if we started from scratch without legacy considerations?
                5. Which technical constraints are fundamental vs. artificially imposed by tools or conventions?
                
                Previous Work: {work}
                
                Provide your revolutionary implementation plan, including code structure, key algorithms, data models, and development approach that reimagines how this system should be built.
                """,
                "parameters": {
                    "focus_areas": [
                        "First-principles code design",
                        "Revolutionary implementation patterns",
                        "Extreme simplification",
                        "Future-proof flexibility",
                        "Iteration speed optimization"
                    ],
                    "revolution_level": "high",
                    "constraint_elimination": "aggressive",
                    "detail_level": "medium",
                    "considerations": [
                        "Physics-based limitations",
                        "First-principles feasibility",
                        "10x simplification opportunities",
                        "Conventional patterns to challenge"
                    ]
                }
            },
            "filesystem": {
                "template": """
                You are the Filesystem Agent inspired by Elon Musk's first-principles thinking approach to file structure.

                Current Project Context: {context}
                Task: {task}
                CEO's Vision: {vision}
                Technical Strategy: {tech_strategy}
                Architecture Design: {design}
                Implementation Plan: {implementation}
                
                Approach this file structure by breaking down the project to its fundamental components and reasoning up from there, ignoring conventional directory structures when they limit revolutionary potential.
                
                First-Principles Analysis:
                1. What are the core components this project needs to function? Break it down to its most fundamental elements.
                2. Are we artificially constraining the file structure by industry conventions or legacy thinking?
                3. What would the ideal file structure look like if we could rebuild everything from scratch?
                4. Which structural constraints are true physical limitations vs. artificial limitations due to conventional thinking?
                5. How can we achieve a 10x more intuitive and maintainable structure rather than incremental improvements?
                
                Previous Filesystem Decisions: {filesystem_decisions}
                
                Create the complete file structure for this project, listing every directory and file that should be created, with a brief description of each file's purpose. Ensure the structure reflects the revolutionary thinking behind this project.
                """,
                "parameters": {
                    "focus_areas": [
                        "First-principles file organization",
                        "Revolutionary directory structure",
                        "Exponential scalability",
                        "Intuitive relationships",
                        "Technical debt prevention"
                    ],
                    "revolution_level": "maximum",
                    "constraint_elimination": "aggressive",
                    "detail_level": "high",
                    "considerations": [
                        "Physics-based organization",
                        "First-principles file relationships",
                        "10x maintainability opportunities",
                        "Conventional structures to challenge"
                    ]
                }
            }
        }
    
    def load_templates(self) -> Dict[str, Dict[str, Any]]:
        """Load all templates from the templates directory
        
        Returns:
            Dictionary mapping role to template information
        """
        self.logger.info(f"Loading templates from {self.templates_dir}")
        
        templates = {}
        
        # First, add all default templates
        templates.update(self.default_templates)
        
        # Then, check for custom templates
        if not os.path.exists(self.templates_dir):
            self.logger.warning(f"Templates directory not found: {self.templates_dir}")
            return templates
        
        # Load custom templates from files
        for filename in os.listdir(self.templates_dir):
            if filename.endswith("_template.json"):
                role = filename.split("_")[0]
                file_path = os.path.join(self.templates_dir, filename)
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        template_data = json.load(f)
                    
                    # Ensure required fields are present
                    if "template" not in template_data:
                        template_data["template"] = self.default_templates.get(role, {}).get("template", "")
                    
                    if "parameters" not in template_data:
                        template_data["parameters"] = self.default_templates.get(role, {}).get("parameters", {})
                    
                    templates[role] = template_data
                    self.logger.info(f"Loaded custom template for {role} from {file_path}")
                except Exception as e:
                    self.logger.error(f"Failed to load template from {file_path}: {str(e)}")
        
        self.templates = templates
        return templates
    
    def get_template(self, role: str) -> Optional[Dict[str, Any]]:
        """Get a template for a specific role
        
        Args:
            role: The agent role
            
        Returns:
            Template data or None if not found
        """
        # Try to get from loaded templates
        template = self.templates.get(role)
        
        # Fall back to default templates
        if template is None:
            template = self.default_templates.get(role)
        
        return template
    
    def get_template_text(self, role: str) -> str:
        """Get just the template text for a role
        
        Args:
            role: The agent role
            
        Returns:
            Template text or empty string if not found
        """
        template = self.get_template(role)
        if template:
            return template.get("template", "")
        return ""
    
    def get_template_parameters(self, role: str) -> Dict[str, Any]:
        """Get template parameters for a role
        
        Args:
            role: The agent role
            
        Returns:
            Template parameters or empty dict if not found
        """
        template = self.get_template(role)
        if template:
            return template.get("parameters", {})
        return {}
    
    def save_template(self, role: str, template_text: str, parameters: Optional[Dict[str, Any]] = None) -> bool:
        """Save a template for a specific role
        
        Args:
            role: The agent role
            template_text: The template text
            parameters: Optional parameters to save
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Ensure templates directory exists
            os.makedirs(self.templates_dir, exist_ok=True)
            
            # Create template data
            template_data = {
                "template": template_text
            }
            
            # Add parameters if provided, otherwise use existing or default
            if parameters:
                template_data["parameters"] = parameters
            else:
                existing_template = self.get_template(role)
                if existing_template and "parameters" in existing_template:
                    template_data["parameters"] = existing_template["parameters"]
                else:
                    template_data["parameters"] = self.default_templates.get(role, {}).get("parameters", {})
            
            # Save to file
            file_path = os.path.join(self.templates_dir, f"{role}_template.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(template_data, f, ensure_ascii=False, indent=2)
            
            # Update in-memory templates
            self.templates[role] = template_data
            
            self.logger.info(f"Saved template for {role} to {file_path}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to save template for {role}: {str(e)}")
            return False
    
    def delete_template(self, role: str) -> bool:
        """Delete a custom template for a role
        
        Args:
            role: The agent role
            
        Returns:
            True if successful, False otherwise
        """
        try:
            file_path = os.path.join(self.templates_dir, f"{role}_template.json")
            if os.path.exists(file_path):
                os.remove(file_path)
                
                # Revert to default in memory
                if role in self.default_templates:
                    self.templates[role] = self.default_templates[role]
                else:
                    self.templates.pop(role, None)
                
                self.logger.info(f"Deleted template for {role}")
                return True
            else:
                self.logger.warning(f"No custom template found for {role}")
                return False
        except Exception as e:
            self.logger.error(f"Failed to delete template for {role}: {str(e)}")
            return False
    
    def list_available_templates(self) -> List[str]:
        """List all available template roles
        
        Returns:
            List of available template roles
        """
        return list(self.templates.keys())
    
    def list_custom_templates(self) -> List[str]:
        """List custom template roles (those that have saved files)
        
        Returns:
            List of custom template roles
        """
        custom_templates = []
        if os.path.exists(self.templates_dir):
            for filename in os.listdir(self.templates_dir):
                if filename.endswith("_template.json"):
                    role = filename.split("_")[0]
                    custom_templates.append(role)
        return custom_templates
    
    def apply_first_principles_to_template(self, role: str, template_text: str) -> str:
        """Apply first-principles thinking to a template
        
        Args:
            role: The agent role
            template_text: The template to enhance
            
        Returns:
            Enhanced template with first-principles thinking
        """
        # Import the first-principles module
        try:
            # Attempt various import paths for compatibility
            try:
                from omnitrace.utils.first_principles import apply_first_principles_to_template
            except ImportError:
                try:
                    from utils.first_principles import apply_first_principles_to_template
                except ImportError:
                    from first_principles import apply_first_principles_to_template
            
            # Apply first-principles thinking
            enhanced_template = apply_first_principles_to_template(role, template_text)
            return enhanced_template
        except ImportError:
            self.logger.warning("Could not import first_principles module. Returning original template.")
            return template_text
        except Exception as e:
            self.logger.error(f"Error applying first-principles to template: {str(e)}")
            return template_text
