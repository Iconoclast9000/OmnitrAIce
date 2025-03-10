"""
CTO Agent - Revolutionary technical strategy using Elon Musk's first-principles thinking
"""

import os
import json
import logging
from typing import Dict, Any, Optional, List
from langchain_core.prompts import ChatPromptTemplate

class CTOAgent:
    """CTO Agent using Elon Musk's first-principles thinking for revolutionary technical strategy"""

    def __init__(self, llm, template=None, parameters=None):
        """Initialize the CTO Agent with first-principles thinking
        
        Args:
            llm: The LLM to use for generation
            template: Optional custom template to use
            parameters: Optional parameters for customization
        """
        self.logger = logging.getLogger(__name__)
        self.llm = llm
        
        # Default template with first-principles thinking
        self.default_template = """
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
        
        After first-principles analysis, focus on:
        1. Revolutionary technical strategy that challenges industry norms
        2. Technology stack selection based on fundamental capabilities rather than popularity
        3. Infrastructure designed for exponential rather than linear scaling
        4. Technical debt elimination through fundamental redesign
        5. Emerging technology opportunities that could disrupt the entire solution space
        
        Previous Technical Decisions: {technical_decisions}
        
        Provide your revolutionary technical strategy recommendations, addressing both immediate implementation needs and a long-term technology roadmap that breaks conventional patterns and creates true disruption.
        """
        
        # Load template from file if available
        self.template = template or self._load_template() or self.default_template
        
        # Default parameters with first-principles focus
        self.default_parameters = {
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
        
        # Load parameters from file or use provided ones
        self.parameters = parameters or self._load_parameters() or self.default_parameters
        
        # Create prompt chain
        self.chain = ChatPromptTemplate.from_template(self.template) | self.llm

    def _load_template(self) -> Optional[str]:
        """Load template from file if it exists"""
        template_path = os.path.join("config", "templates", "cto_template.json")
        if os.path.exists(template_path):
            try:
                with open(template_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("template")
            except Exception as e:
                self.logger.error(f"Failed to load CTO template: {str(e)}")
        return None
        
    def _load_parameters(self) -> Optional[Dict[str, Any]]:
        """Load parameters from file if it exists"""
        template_path = os.path.join("config", "templates", "cto_template.json")
        if os.path.exists(template_path):
            try:
                with open(template_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("parameters")
            except Exception as e:
                self.logger.error(f"Failed to load CTO parameters: {str(e)}")
        return None
    
    async def process(self, task: str, context: Dict[str, Any]) -> str:
        """Process a task using the CTO Agent with first-principles thinking
        
        Args:
            task: The task to process
            context: The context to use for processing
                - context: Current project context
                - vision: CEO's vision
                - technical_decisions: Previous technical decisions
                
        Returns:
            Revolutionary technical strategy based on first-principles analysis
        """
        try:
            # Ensure required context fields are present
            required_fields = ["context", "vision", "technical_decisions"]
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
            self.logger.info("Generated revolutionary technical strategy using first-principles thinking")
            
            return response
            
        except Exception as e:
            self.logger.error(f"CTO Agent first-principles processing failed: {str(e)}")
            raise

    def set_revolution_level(self, level: str) -> None:
        """Set how revolutionary the CTO's approach should be.
        
        Args:
            level: One of "moderate", "high", "maximum"
        """
        valid_levels = ["moderate", "high", "maximum"]
        if level not in valid_levels:
            self.logger.warning(f"Invalid revolution level: {level}. Using 'maximum'")
            level = "maximum"
        
        self.parameters["revolution_level"] = level
        self.logger.info(f"CTO revolution level set to: {level}")
        
    def set_constraint_elimination(self, level: str) -> None:
        """Set how aggressively to eliminate artificial constraints.
        
        Args:
            level: One of "cautious", "moderate", "aggressive"
        """
        valid_levels = ["cautious", "moderate", "aggressive"]
        if level not in valid_levels:
            self.logger.warning(f"Invalid constraint elimination level: {level}. Using 'aggressive'")
            level = "aggressive"
        
        self.parameters["constraint_elimination"] = level
        self.logger.info(f"Constraint elimination level set to: {level}")
