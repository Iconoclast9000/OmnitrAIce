"""
First-Principles Thinking Module for OmnitrAIce

This module provides utilities and functions to apply Elon Musk's
first-principles thinking approach to problem-solving in the multi-agent system.
"""

import logging
from typing import List, Dict, Any, Optional, Tuple

class FirstPrinciplesAnalyzer:
    """Analyzes problems using Elon Musk's first-principles thinking."""
    
    def __init__(self, logger=None):
        """Initialize the analyzer.
        
        Args:
            logger: Optional logger instance
        """
        self.logger = logger or logging.getLogger(__name__)
        
    def break_down_problem(self, problem: str) -> List[str]:
        """Break down a problem to its fundamental components.
        
        Args:
            problem: The problem to break down
            
        Returns:
            List of fundamental components
        """
        self.logger.info(f"Breaking down problem to fundamentals: {problem}")
        
        # In a more advanced implementation, this would use the LLM to
        # identify the fundamental components of the problem
        
        # For now, we'll provide a structured approach to breaking down problems
        fundamental_components = [
            f"Core problem statement: {problem}",
            "Physics-based constraints",
            "Artificial constraints to eliminate",
            "Core functionality requirements",
            "Fundamental user needs"
        ]
        
        return fundamental_components
    
    def identify_constraints(self, problem: str) -> Tuple[List[str], List[str]]:
        """Identify physical vs. artificial constraints.
        
        Args:
            problem: The problem to analyze
            
        Returns:
            Tuple of (physical_constraints, artificial_constraints)
        """
        self.logger.info(f"Identifying constraints for: {problem}")
        
        # Again, in a full implementation, this would use the LLM
        
        # Sample physical constraints (true limitations)
        physical_constraints = [
            "Laws of physics",
            "Mathematical limitations",
            "Hardware constraints",
            "Time constraints",
            "Resource limitations"
        ]
        
        # Sample artificial constraints (conventional limitations)
        artificial_constraints = [
            "Industry standards",
            "Conventional approaches",
            "Traditional architecture patterns",
            "Legacy compatibility",
            "Risk aversion"
        ]
        
        return physical_constraints, artificial_constraints
    
    def generate_10x_opportunities(self, problem: str, components: List[str]) -> List[str]:
        """Generate potential 10x improvement opportunities.
        
        Args:
            problem: The original problem
            components: Fundamental components of the problem
            
        Returns:
            List of potential 10x improvement opportunities
        """
        self.logger.info(f"Generating 10x improvement opportunities for: {problem}")
        
        # In a full implementation, this would use the LLM to generate
        # revolutionary improvements based on first principles
        
        opportunities = [
            "Eliminate artificial constraints in conventional approach",
            "Optimize for exponential rather than linear scaling",
            "Simplify architecture by challenging traditional patterns",
            "Design for revolutionary capabilities rather than incremental features",
            "Rebuild from the ground up with physics-based limitations only"
        ]
        
        return opportunities
    
    def apply_first_principles(self, problem: str) -> Dict[str, Any]:
        """Apply first-principles thinking to a problem.
        
        Args:
            problem: The problem to analyze
            
        Returns:
            Dictionary containing first-principles analysis
        """
        self.logger.info(f"Applying first-principles thinking to: {problem}")
        
        # Break down the problem
        components = self.break_down_problem(problem)
        
        # Identify constraints
        physical, artificial = self.identify_constraints(problem)
        
        # Generate 10x opportunities
        opportunities = self.generate_10x_opportunities(problem, components)
        
        # Create first-principles analysis
        analysis = {
            "problem": problem,
            "fundamental_components": components,
            "physical_constraints": physical,
            "artificial_constraints": artificial,
            "10x_opportunities": opportunities
        }
        
        return analysis

class RevolutionaryApproach:
    """Implements revolutionary approaches based on first-principles thinking."""
    
    def __init__(self, 
                 revolution_level: str = "maximum",
                 constraint_elimination: str = "aggressive",
                 logger=None):
        """Initialize the revolutionary approach.
        
        Args:
            revolution_level: Level of revolutionary thinking (moderate/high/maximum)
            constraint_elimination: How aggressively to eliminate constraints
            logger: Optional logger instance
        """
        self.logger = logger or logging.getLogger(__name__)
        
        valid_revolution_levels = ["moderate", "high", "maximum"]
        if revolution_level not in valid_revolution_levels:
            self.logger.warning(f"Invalid revolution level: {revolution_level}. Using 'maximum'")
            revolution_level = "maximum"
        
        valid_constraint_levels = ["cautious", "moderate", "aggressive"]
        if constraint_elimination not in valid_constraint_levels:
            self.logger.warning(f"Invalid constraint elimination: {constraint_elimination}. Using 'aggressive'")
            constraint_elimination = "aggressive"
        
        self.revolution_level = revolution_level
        self.constraint_elimination = constraint_elimination
        
        # Configure revolution level factors
        self.revolution_factors = {
            "moderate": 0.3,  # 30% revolutionary
            "high": 0.7,      # 70% revolutionary
            "maximum": 1.0    # 100% revolutionary
        }
        
        # Configure constraint elimination factors
        self.elimination_factors = {
            "cautious": 0.3,  # Eliminate 30% of artificial constraints
            "moderate": 0.7,  # Eliminate 70% of artificial constraints
            "aggressive": 1.0 # Eliminate 100% of artificial constraints
        }
    
    def apply_revolutionary_approach(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Apply revolutionary approach to first-principles analysis.
        
        Args:
            analysis: First-principles analysis dictionary
            
        Returns:
            Enhanced analysis with revolutionary approach
        """
        self.logger.info(f"Applying revolutionary approach at level: {self.revolution_level}")
        
        # Get revolution factor
        revolution_factor = self.revolution_factors.get(self.revolution_level)
        
        # Get constraint elimination factor
        elimination_factor = self.elimination_factors.get(self.constraint_elimination)
        
        # Calculate which artificial constraints to eliminate
        artificial_constraints = analysis.get("artificial_constraints", [])
        constraints_to_eliminate = artificial_constraints[:int(len(artificial_constraints) * elimination_factor)]
        
        # Focus on 10x opportunities based on revolution level
        opportunities = analysis.get("10x_opportunities", [])
        prioritized_opportunities = opportunities[:int(len(opportunities) * revolution_factor) + 1]
        
        # Enhance analysis with revolutionary approach
        revolutionary_analysis = analysis.copy()
        revolutionary_analysis.update({
            "revolution_level": self.revolution_level,
            "constraint_elimination": self.constraint_elimination,
            "constraints_to_eliminate": constraints_to_eliminate,
            "prioritized_opportunities": prioritized_opportunities,
            "revolutionary_factor": revolution_factor,
            "elimination_factor": elimination_factor
        })
        
        return revolutionary_analysis

class PromptEnhancer:
    """Enhances agent prompts with first-principles thinking."""
    
    def __init__(self, logger=None):
        """Initialize the prompt enhancer.
        
        Args:
            logger: Optional logger instance
        """
        self.logger = logger or logging.getLogger(__name__)
        
        # First-principles thinking prompts
        self.first_principles_prompts = {
            "ceo": """
            Approach this project by breaking down the problem to its fundamental truths and reasoning up from there. Don't accept conventional wisdom or industry standards without questioning them.
            
            First-Principles Analysis:
            1. What fundamental problem are we truly trying to solve?
            2. What would the ideal solution look like if there were no constraints?
            3. Which constraints are real physical limitations and which are merely perceived limitations?
            4. How can we achieve a 10x improvement rather than a 10% improvement?
            5. What would this solution look like if we started completely from scratch?
            """,
            
            "cto": """
            Approach this project by breaking down the technical challenges to their fundamental components and reasoning up from there, ignoring conventional technology approaches when they limit revolutionary potential.
            
            First-Principles Analysis:
            1. What is the core technical problem we're trying to solve? Break it down to its most fundamental elements.
            2. Are we artificially constraining our solution by industry conventions or legacy thinking?
            3. What would the ideal technical solution look like if we could rebuild everything from scratch?
            4. Which technical constraints are true physical limitations vs. artificial limitations due to conventional thinking?
            5. How can we achieve a 10x improvement in our technical approach rather than incremental improvements?
            """,
            
            "architect": """
            Approach this architecture by deconstructing the system to its fundamental components and rebuilding it without the constraints of conventional patterns.
            
            First-Principles Architecture Analysis:
            1. What are the essential system components needed to fulfill the core requirements?
            2. Which traditional architecture patterns are we using out of habit rather than necessity?
            3. How can we design a system that scales exponentially rather than linearly?
            4. What would this architecture look like if we had unlimited resources but were constrained only by physics?
            5. How can we achieve a 10x simpler or more powerful architecture?
            """,
            
            "developer": """
            Approach implementation planning by questioning conventional development practices and focusing on revolutionary approaches.
            
            First-Principles Implementation Analysis:
            1. What are the fundamental programming constructs needed to implement this system?
            2. Which development patterns are we using out of convention rather than necessity?
            3. How can we implement this system with 10x less code or 10x more capability?
            4. What would our implementation approach look like if we started from scratch without legacy considerations?
            5. Which technical constraints are fundamental vs. artificially imposed by tools or conventions?
            """
        }
    
    def enhance_prompt(self, agent_type: str, original_prompt: str) -> str:
        """Enhance an agent prompt with first-principles thinking.
        
        Args:
            agent_type: The type of agent (ceo, cto, architect, developer)
            original_prompt: The original agent prompt
            
        Returns:
            Enhanced prompt with first-principles thinking
        """
        self.logger.info(f"Enhancing {agent_type} prompt with first-principles thinking")
        
        # Get first-principles prompt for this agent type
        first_principles_prompt = self.first_principles_prompts.get(agent_type.lower(), "")
        
        if not first_principles_prompt:
            self.logger.warning(f"No first-principles prompt available for agent type: {agent_type}")
            return original_prompt
        
        # Find a good insertion point - after the introduction but before the task
        # This is a simple implementation; a more robust implementation would parse the prompt structure
        
        # Look for "Task:" or similar
        task_indices = [
            original_prompt.find("Task:"),
            original_prompt.find("Current Project Context:"),
            original_prompt.find("Focus on:"),
        ]
        
        # Filter out -1 (not found)
        valid_indices = [idx for idx in task_indices if idx != -1]
        
        if valid_indices:
            # Insert at the earliest task indicator
            insertion_point = min(valid_indices)
            enhanced_prompt = (
                original_prompt[:insertion_point] + 
                first_principles_prompt + 
                original_prompt[insertion_point:]
            )
        else:
            # Default to inserting after the first paragraph
            paragraphs = original_prompt.split("\n\n")
            if len(paragraphs) > 1:
                paragraphs.insert(1, first_principles_prompt)
                enhanced_prompt = "\n\n".join(paragraphs)
            else:
                # Just append if we can't find a good insertion point
                enhanced_prompt = original_prompt + "\n\n" + first_principles_prompt
        
        return enhanced_prompt

def apply_first_principles_to_template(agent_type: str, template: str) -> str:
    """Apply first-principles thinking to an agent template.
    
    Args:
        agent_type: The type of agent (ceo, cto, architect, developer)
        template: The agent template
        
    Returns:
        Template enhanced with first-principles thinking
    """
    enhancer = PromptEnhancer()
    return enhancer.enhance_prompt(agent_type, template)

def create_first_principles_analysis(problem: str, 
                                    revolution_level: str = "maximum",
                                    constraint_elimination: str = "aggressive") -> Dict[str, Any]:
    """Create a comprehensive first-principles analysis of a problem.
    
    Args:
        problem: The problem to analyze
        revolution_level: Level of revolutionary thinking
        constraint_elimination: Level of constraint elimination
        
    Returns:
        Dictionary containing first-principles analysis with revolutionary approach
    """
    analyzer = FirstPrinciplesAnalyzer()
    revolutionary = RevolutionaryApproach(
        revolution_level=revolution_level,
        constraint_elimination=constraint_elimination
    )
    
    # Apply first-principles thinking
    analysis = analyzer.apply_first_principles(problem)
    
    # Enhance with revolutionary approach
    revolutionary_analysis = revolutionary.apply_revolutionary_approach(analysis)
    
    return revolutionary_analysis
