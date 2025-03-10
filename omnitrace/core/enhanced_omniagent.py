"""
Enhanced OmniAgent - Extends core agent with customization capabilities
"""

import asyncio
import os
import json
import logging
from typing import Dict, Any, List, Optional

# Import from new structure, with fallbacks for compatibility
try:
    from omnitrace.core.omniagent import OmniAgent
except ImportError:
    try:
        from core.omniagent import OmniAgent
    except ImportError:
        from omniagent import OmniAgent

class EnhancedOmniAgent(OmniAgent):
    """Enhanced OmniAgent with customizable agent interface"""

    def __init__(self, model_name: str = "deepseek-r1:1.5b"):
        super().__init__(model_name)

        # Store customized templates
        self.custom_templates = {}
        
        # Load any saved custom templates
        self._load_custom_templates()

    def _load_custom_templates(self):
        """Load saved custom templates"""
        templates_dir = os.path.join("config", "templates")
        if os.path.exists(templates_dir):
            for file_name in os.listdir(templates_dir):
                if file_name.endswith(".json"):
                    role = file_name.split("_")[0]  
                    file_path = os.path.join(templates_dir, file_name)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            template = json.load(f)
                        self.custom_templates[role] = template
                        self.logger.info(f"Loaded custom template for {role} from {file_path}")
                    except Exception as e:
                        self.logger.error(f"Failed to load custom template from {file_path}: {str(e)}")

    def save_custom_template(self, role: str, template: str):
        """Save a custom template for an agent role"""
        templates_dir = os.path.join("config", "templates")
        os.makedirs(templates_dir, exist_ok=True)

        file_path = os.path.join(templates_dir, f"{role}_template.json")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump({"template": template}, f, ensure_ascii=False, indent=2)
            self.custom_templates[role] = template
            return True
        except Exception as e:
            self.logger.error(f"Failed to save custom template for {role}: {str(e)}")
            return False

    def get_template(self, role: str) -> str:
        """Get the current template for an agent role"""
        if role in self.custom_templates:
            return self.custom_templates[role]["template"]
        return self.agent_templates.get(role, "")
    
    def get_available_agents(self) -> List[str]:
        """Get a list of available agent types"""
        return list(self.agent_templates.keys())
