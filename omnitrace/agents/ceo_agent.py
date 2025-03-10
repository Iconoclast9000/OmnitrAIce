"""
CEO Agent - Revolutionary vision creation using Elon Musk's first-principles thinking
"""

import os
import json
import logging
from typing import Dict, Any, Optional, List
from langchain_core.prompts import ChatPromptTemplate

class CEOAgent:
    """CEO Agent using Elon Musk's first-principles thinking for revolutionary vision creation"""

    def __init__(self, llm, template=None, parameters=None):
        """Initialize the CEO Agent with first-principles thinking
        
        Args:
            llm: The LLM to use for generation
            template: Optional custom template to use
            parameters: Optional parameters for customization
        """
        self.logger = logging.getLogger(__name__)
        self.llm = llm
        
        # Default template with first-principles thinking
        self.default_template = """
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
        
        After first-principles analysis, focus on:
        1. Revolutionary vision that challenges industry assumptions
        2. Resource allocation optimized for breakthrough results
        3. Timeline planning that enables rapid iteration and evolution
        4. Risk assessment that distinguishes real physics-based risks from perceived conventional risks
        
        Previous Decisions: {decisions}
        
        Provide a revolutionary vision that challenges assumptions and uses first-principles thinking to achieve breakthrough results.
        """
        
        # Load template from file if available
        self.template = template or self._load_template() or self.default_template
        
        # Default parameters with first-principles focus
        self.default_parameters = {
            "focus_areas": [
                "First-principles problem analysis",
                "Revolutionary vision creation",
                "10x improvement identification",
                "Constraint elimination strategy",
                "Moonshot goal setting"
            ],
            "first_principles_level": "high",
            "revolutionary_factor": "maximum",
            "constraints_consideration": "minimal",
            "ambition_level": "moonshot",
            "detail_level": "medium",
            "considerations": [
                "Physics-based limitations",
                "First-principles feasibility",
                "10x improvement opportunities",
                "Conventional wisdom to challenge"
            ]
        }
        
        # Load parameters from file or use provided ones
        self.parameters = parameters or self._load_parameters() or self.default_parameters
        
        # Create prompt chain
        self.chain = ChatPromptTemplate.from_template(self.template) | self.llm

    def _load_template(self) -> Optional[str]:
        """Load template from file if it exists"""
        template_path = os.path.join("config", "templates", "ceo_template.json")
        if os.path.exists(template_path):
            try:
                with open(template_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("template")
            except Exception as e:
                self.logger.error(f"Failed to load CEO template: {str(e)}")
        return None
        
    def _load_parameters(self) -> Optional[Dict[str, Any]]:
        """Load parameters from file if it exists"""
        template_path = os.path.join("config", "templates", "ceo_template.json")
        if os.path.exists(template_path):
            try:
                with open(template_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("parameters")
            except Exception as e:
                self.logger.error(f"Failed to load CEO parameters: {str(e)}")
        return None
    
    async def process(self, task: str, context: Dict[str, Any]) -> str:
        """Process a task using the CEO Agent with first-principles thinking
        
        Args:
            task: The task to process
            context: The context to use for processing
                - context: Current project context
                - decisions: Previous decisions
                
        Returns:
            Revolutionary vision based on first-principles analysis
        """
        try:
            # Ensure required context fields are present
            required_fields = ["context", "decisions"]
            for field in required_fields:
                if field not in context:
                    context[field] = ""
            
            # Add task to context
            context["task"] = task
            
            # Process with LLM
            import asyncio
            self.logger.info(f"Applying first-principles thinking to: {task}")
            result = await asyncio.to_thread(self.chain.invoke, context)
            
            # Extract response
            response = result.text if hasattr(result, "text") else str(result)
            self.logger.info("Generated revolutionary vision using first-principles thinking")
            
            return response
            
        except Exception as e:
            self.logger.error(f"CEO Agent first-principles processing failed: {str(e)}")
            raise

    def set_revolution_level(self, level: str) -> None:
        """Set how revolutionary the CEO's approach should be.
        
        Args:
            level: One of "moderate", "high", "maximum"
        """
        valid_levels = ["moderate", "high", "maximum"]
        if level not in valid_levels:
            self.logger.warning(f"Invalid revolution level: {level}. Using 'maximum'")
            level = "maximum"
        
        self.parameters["revolutionary_factor"] = level
        self.logger.info(f"CEO revolution level set to: {level}")
        
    def set_constraint_elimination(self, level: str) -> None:
        """Set how aggressively to eliminate artificial constraints.
        
        Args:
            level: One of "cautious", "moderate", "aggressive"
        """
        constraint_map = {
            "cautious": "balanced",
            "moderate": "limited",
            "aggressive": "minimal"
        }
        if level not in constraint_map:
            self.logger.warning(f"Invalid constraint elimination level: {level}. Using 'aggressive'")
            level = "aggressive"
        
        self.parameters["constraints_consideration"] = constraint_map[level]
        self.logger.info(f"Constraint consideration level set to: {constraint_map[level]}")
        
    def set_ambition_level(self, level: str) -> None:
        """Set the ambition level for the CEO's vision.
        
        Args:
            level: One of "incremental", "revolutionary", "moonshot"
        """
        valid_levels = ["incremental", "revolutionary", "moonshot"]
        if level not in valid_levels:
            self.logger.warning(f"Invalid ambition level: {level}. Using 'moonshot'")
            level = "moonshot"
        
        self.parameters["ambition_level"] = level
        self.logger.info(f"Ambition level set to: {level}")
