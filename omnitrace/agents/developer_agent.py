"""
Developer Agent - Revolutionary implementation planning using Elon Musk's first-principles thinking
"""

import os
import json
import logging
from typing import Dict, Any, Optional, List
from langchain_core.prompts import ChatPromptTemplate

class DeveloperAgent:
    """Developer Agent using Elon Musk's first-principles thinking for revolutionary implementation planning"""

    def __init__(self, llm, template=None, parameters=None):
        """Initialize the Developer Agent with first-principles thinking
        
        Args:
            llm: The LLM to use for generation
            template: Optional custom template to use
            parameters: Optional parameters for customization
        """
        self.logger = logging.getLogger(__name__)
        self.llm = llm
        
        # Default template with first-principles thinking
        self.default_template = """
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
        
        Focus on:
        1. Revolutionary implementation patterns that challenge traditional approaches
        2. Novel code organization that optimizes for system evolution
        3. Extreme simplification of complex functionality
        4. Implementation approaches that maximize future flexibility
        5. Breakthrough development practices for rapid iteration
        
        Previous Work: {work}
        
        Provide your revolutionary implementation plan, including code structure, key algorithms, data models, and development approach that reimagines how this system should be built.
        """
        
        # Load template from file if available
        self.template = template or self._load_template() or self.default_template
        
        # Default parameters with first-principles focus
        self.default_parameters = {
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
        
        # Load parameters from file or use provided ones
        self.parameters = parameters or self._load_parameters() or self.default_parameters
        
        # Create prompt chain
        self.chain = ChatPromptTemplate.from_template(self.template) | self.llm

    def _load_template(self) -> Optional[str]:
        """Load template from file if it exists"""
        template_path = os.path.join("config", "templates", "developer_template.json")
        if os.path.exists(template_path):
            try:
                with open(template_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("template")
            except Exception as e:
                self.logger.error(f"Failed to load Developer template: {str(e)}")
        return None
        
    def _load_parameters(self) -> Optional[Dict[str, Any]]:
        """Load parameters from file if it exists"""
        template_path = os.path.join("config", "templates", "developer_template.json")
        if os.path.exists(template_path):
            try:
                with open(template_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("parameters")
            except Exception as e:
                self.logger.error(f"Failed to load Developer parameters: {str(e)}")
        return None
    
    async def process(self, task: str, context: Dict[str, Any]) -> str:
        """Process a task using the Developer Agent with first-principles thinking
        
        Args:
            task: The task to process
            context: The context to use for processing
                - context: Current project context
                - design: Architecture design
                - tech_strategy: CTO's technical strategy
                - work: Previous implementation work
                
        Returns:
            Revolutionary implementation plan based on first-principles analysis
        """
        try:
            # Ensure required context fields are present
            required_fields = ["context", "design", "tech_strategy", "work"]
            for field in required_fields:
                if field not in context:
                    context[field] = ""
            
            # Add task to context
            context["task"] = task
            
            # Process with LLM
            import asyncio
            self.logger.info(f"Applying first-principles thinking to implementation: {task}")
            result = await asyncio.to_thread(self.chain.invoke, context)
            
            # Extract response
            response = result.text if hasattr(result, "text") else str(result)
            self.logger.info("Generated revolutionary implementation plan using first-principles thinking")
            
            return response
            
        except Exception as e:
            self.logger.error(f"Developer Agent first-principles processing failed: {str(e)}")
            raise

    def set_revolution_level(self, level: str) -> None:
        """Set how revolutionary the developer's approach should be.
        
        Args:
            level: One of "moderate", "high", "maximum"
        """
        valid_levels = ["moderate", "high", "maximum"]
        if level not in valid_levels:
            self.logger.warning(f"Invalid revolution level: {level}. Using 'high'")
            level = "high"
        
        self.parameters["revolution_level"] = level
        self.logger.info(f"Developer revolution level set to: {level}")
        
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
        
    def set_detail_level(self, level: str) -> None:
        """Set the level of detail for the implementation plan.
        
        Args:
            level: One of "low", "medium", "high"
        """
        valid_levels = ["low", "medium", "high"]
        if level not in valid_levels:
            self.logger.warning(f"Invalid detail level: {level}. Using 'medium'")
            level = "medium"
        
        self.parameters["detail_level"] = level
        self.logger.info(f"Detail level set to: {level}")
