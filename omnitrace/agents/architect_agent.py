"""
Architect Agent - Revolutionary architecture design using Elon Musk's first-principles thinking
"""

import os
import json
import logging
from typing import Dict, Any, Optional, List
from langchain_core.prompts import ChatPromptTemplate

class ArchitectAgent:
    """Architect Agent using Elon Musk's first-principles thinking for revolutionary system design"""

    def __init__(self, llm, template=None, parameters=None):
        """Initialize the Architect Agent with first-principles thinking
        
        Args:
            llm: The LLM to use for generation
            template: Optional custom template to use
            parameters: Optional parameters for customization
        """
        self.logger = logging.getLogger(__name__)
        self.llm = llm
        
        # Default template with first-principles thinking
        self.default_template = """
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
        
        Focus on:
        1. Revolutionary component design that challenges traditional boundaries
        2. Novel interaction patterns between system elements
        3. Architecture that enables continuous evolution without rewrites
        4. System boundaries designed for optimal data flow rather than organizational convenience
        5. Breakthrough approaches to system resilience and scaling
        
        Previous Designs: {designs}
        
        Provide your revolutionary architectural design, including component diagrams, data flows, and system boundaries that reimagine how this system could work.
        """
        
        # Load template from file if available
        self.template = template or self._load_template() or self.default_template
        
        # Default parameters with first-principles focus
        self.default_parameters = {
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
        
        # Load parameters from file or use provided ones
        self.parameters = parameters or self._load_parameters() or self.default_parameters
        
        # Create prompt chain
        self.chain = ChatPromptTemplate.from_template(self.template) | self.llm

    def _load_template(self) -> Optional[str]:
        """Load template from file if it exists"""
        template_path = os.path.join("config", "templates", "architect_template.json")
        if os.path.exists(template_path):
            try:
                with open(template_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("template")
            except Exception as e:
                self.logger.error(f"Failed to load Architect template: {str(e)}")
        return None
        
    def _load_parameters(self) -> Optional[Dict[str, Any]]:
        """Load parameters from file if it exists"""
        template_path = os.path.join("config", "templates", "architect_template.json")
        if os.path.exists(template_path):
            try:
                with open(template_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("parameters")
            except Exception as e:
                self.logger.error(f"Failed to load Architect parameters: {str(e)}")
        return None
    
    async def process(self, task: str, context: Dict[str, Any]) -> str:
        """Process a task using the Architect Agent with first-principles thinking
        
        Args:
            task: The task to process
            context: The context to use for processing
                - context: Current project context
                - vision: CEO's vision
                - tech_strategy: CTO's technical strategy
                - designs: Previous designs
                
        Returns:
            Revolutionary architecture design based on first-principles analysis
        """
        try:
            # Ensure required context fields are present
            required_fields = ["context", "vision", "tech_strategy", "designs"]
            for field in required_fields:
                if field not in context:
                    context[field] = ""
            
            # Add task to context
            context["task"] = task
            
            # Process with LLM
            import asyncio
            self.logger.info(f"Applying first-principles thinking to architecture: {task}")
            result = await asyncio.to_thread(self.chain.invoke, context)
            
            # Extract response
            response = result.text if hasattr(result, "text") else str(result)
            self.logger.info("Generated revolutionary architecture using first-principles thinking")
            
            return response
            
        except Exception as e:
            self.logger.error(f"Architect Agent first-principles processing failed: {str(e)}")
            raise

    def set_revolution_level(self, level: str) -> None:
        """Set how revolutionary the architect's approach should be.
        
        Args:
            level: One of "moderate", "high", "maximum"
        """
        valid_levels = ["moderate", "high", "maximum"]
        if level not in valid_levels:
            self.logger.warning(f"Invalid revolution level: {level}. Using 'high'")
            level = "high"
        
        self.parameters["revolution_level"] = level
        self.logger.info(f"Architect revolution level set to: {level}")
        
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
        """Set the level of detail for the architectural design.
        
        Args:
            level: One of "low", "medium", "high"
        """
        valid_levels = ["low", "medium", "high"]
        if level not in valid_levels:
            self.logger.warning(f"Invalid detail level: {level}. Using 'medium'")
            level = "medium"
        
        self.parameters["detail_level"] = level
        self.logger.info(f"Detail level set to: {level}")
