"""
Revolutionary OmniAgent - Unified implementation with all advanced capabilities
"""

import asyncio
import os
import sys
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List, Union, Tuple

# Import base and enhanced functionality with fallbacks for compatibility
try:
    from omnitrace.core.enhanced_omniagent import EnhancedOmniAgent
except ImportError:
    try:
        from core.enhanced_omniagent import EnhancedOmniAgent
    except ImportError:
        from enhanced_omniagent import EnhancedOmniAgent

# Import specialized agents with fallbacks for compatibility
try:
    from omnitrace.agents.cto_agent import CTOAgent
    from omnitrace.agents.filesystem_agent import FilesystemAgent
except ImportError:
    try:
        from agents.cto_agent import CTOAgent
        from agents.filesystem_agent import FilesystemAgent
    except ImportError:
        try:
            from cto_agent import CTOAgent
            from filesystem_agent import FilesystemAgent
        except ImportError:
            CTOAgent = None
            FilesystemAgent = None

# Import revolutionary capabilities with fallbacks
try:
    from omnitrace.generation.code_generator import RevolutionaryCodeGenerator
    from omnitrace.utils.first_principles import FirstPrinciplesAnalyzer, RevolutionaryApproach, PromptEnhancer
except ImportError:
    try:
        from generation.code_generator import RevolutionaryCodeGenerator
        from utils.first_principles import FirstPrinciplesAnalyzer, RevolutionaryApproach, PromptEnhancer
    except ImportError:
        try:
            from code_generator import RevolutionaryCodeGenerator
            from first_principles import FirstPrinciplesAnalyzer, RevolutionaryApproach, PromptEnhancer
        except ImportError:
            RevolutionaryCodeGenerator = None
            FirstPrinciplesAnalyzer = None
            RevolutionaryApproach = None
            PromptEnhancer = None

class UnifiedOmniAgent(EnhancedOmniAgent):
    """
    Unified OmniAgent that integrates all revolutionary capabilities:
    - Enhanced agent customization
    - Specialized agent implementations (CTO, Filesystem)
    - First-principles analysis
    - Revolutionary file structure generation
    - Revolutionary code generation
    """
    
    def __init__(self, model_name: str = "deepseek-r1:1.5b") -> None:
        """Initialize the Unified OmniAgent with all revolutionary capabilities.
        
        Args:
            model_name: The name of the language model to use
        """
        super().__init__(model_name)
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Initializing UnifiedOmniAgent with model: {model_name}")
        
        # Initialize specialized agents if available
        self.cto_agent = CTOAgent(self.llm) if CTOAgent else None
        self.filesystem_agent = FilesystemAgent(self.llm) if FilesystemAgent else None
        
        # Initialize revolutionary capabilities if available
        self.code_generator = RevolutionaryCodeGenerator(self.llm) if RevolutionaryCodeGenerator else None
        self.first_principles = FirstPrinciplesAnalyzer() if FirstPrinciplesAnalyzer else None
        self.revolutionary_approach = RevolutionaryApproach() if RevolutionaryApproach else None
        self.prompt_enhancer = PromptEnhancer() if PromptEnhancer else None
        
        # Configuration flags
        self.enable_code_gen: bool = True
        self.enable_file_structure: bool = True
        self.revolution_level: str = "maximum"
        self.constraint_elimination: str = "aggressive"
        
        # Version information
        self.version = "1.1.0"
        self.version_date = datetime.now().strftime("%Y-%m-%d")
        
        self.logger.info(f"UnifiedOmniAgent initialized (version {self.version})")
        
    def set_revolution_level(self, level: str) -> None:
        """Set the revolution level for all agents and components.
        
        Args:
            level: Revolution level (moderate, high, maximum)
        """
        valid_levels = ["moderate", "high", "maximum"]
        if level not in valid_levels:
            self.logger.warning(f"Invalid revolution level: {level}. Using 'maximum'")
            level = "maximum"
            
        self.revolution_level = level
        self.logger.info(f"Revolution level set to: {level}")
        
        # Update revolution level in all components
        if hasattr(self.cto_agent, "set_revolution_level"):
            self.cto_agent.set_revolution_level(level)
        
        if hasattr(self.revolutionary_approach, "revolution_level"):
            self.revolutionary_approach.revolution_level = level
            
    def set_constraint_elimination(self, level: str) -> None:
        """Set constraint elimination level for all agents.
        
        Args:
            level: Constraint elimination level (cautious, moderate, aggressive)
        """
        valid_levels = ["cautious", "moderate", "aggressive"]
        if level not in valid_levels:
            self.logger.warning(f"Invalid constraint elimination level: {level}. Using 'aggressive'")
            level = "aggressive"
            
        self.constraint_elimination = level
        self.logger.info(f"Constraint elimination set to: {level}")
        
        # Update constraint elimination in all components
        if hasattr(self.cto_agent, "set_constraint_elimination"):
            self.cto_agent.set_constraint_elimination(level)
        
        if hasattr(self.revolutionary_approach, "constraint_elimination"):
            self.revolutionary_approach.constraint_elimination = level
            
    def enable_code_generation(self, enabled: bool = True) -> None:
        """Enable or disable code generation functionality.
        
        Args:
            enabled: Whether code generation is enabled
        """
        self.enable_code_gen = enabled
        self.logger.info(f"Code generation {'enabled' if enabled else 'disabled'}")
        
    def to_enhanced_agent(self):
        """Convert this UnifiedOmniAgent to an EnhancedOmniAgent for backward compatibility.
        
        Returns:
            An EnhancedOmniAgent instance with settings copied from this agent
        """
        self.logger.info("Converting UnifiedOmniAgent to EnhancedOmniAgent for backward compatibility")
        
        try:
            # Import with fallbacks for compatibility
            try:
                from omnitrace.core.enhanced_omniagent import EnhancedOmniAgent
            except ImportError:
                try:
                    from core.enhanced_omniagent import EnhancedOmniAgent
                except ImportError:
                    from enhanced_omniagent import EnhancedOmniAgent
            
            # Create a new EnhancedOmniAgent with the same model
            enhanced_agent = EnhancedOmniAgent(model_name=self.llm.model_name if hasattr(self.llm, 'model_name') else "deepseek-r1:1.5b")
            
            # Copy templates if available
            if hasattr(self, "agent_templates") and hasattr(enhanced_agent, "agent_templates"):
                enhanced_agent.agent_templates = self.agent_templates.copy()
            
            # Copy project state if available
            if hasattr(self, "project_state") and hasattr(enhanced_agent, "project_state"):
                enhanced_agent.project_state = self.project_state.copy()
                
            return enhanced_agent
        except Exception as e:
            self.logger.error(f"Failed to convert to EnhancedOmniAgent: {e}")
            raise
        
    def enable_file_structure_generation(self, enabled: bool = True) -> None:
        """Enable or disable file structure generation.
        
        Args:
            enabled: Whether file structure generation is enabled
        """
        self.enable_file_structure = enabled
        self.logger.info(f"File structure generation {'enabled' if enabled else 'disabled'}")
        
    def get_available_agents(self) -> List[str]:
        """Get a list of all available agents in the system.
        
        Returns:
            List of agent names
        """
        # Base agents from parent class
        base_agents = super().get_available_agents() if hasattr(super(), "get_available_agents") else []
        
        # Add specialized agents
        specialized_agents = []
        if self.cto_agent:
            specialized_agents.append("cto")
        if self.filesystem_agent:
            specialized_agents.append("filesystem")
        
        return list(set(base_agents + specialized_agents))
    
    def get_revolutionary_metrics(self) -> Dict[str, Any]:
        """Get revolutionary metrics for the current configuration.
        
        Returns:
            Dictionary of revolutionary metrics
        """
        metrics = {
            "revolution_level": self.revolution_level,
            "constraint_elimination": self.constraint_elimination,
            "code_generation": self.enable_code_gen,
            "file_structure_generation": self.enable_file_structure,
            "first_principles_metrics": {
                "innovation_score": 0.85,  # Placeholder, would be calculated dynamically
                "disruption_factor": 0.90, # Placeholder
                "10x_improvement_score": 0.95  # Placeholder
            }
        }
        
        return metrics
        
    async def create_project(self, name: str, description: str) -> Dict[str, Any]:
        """Create revolutionary project using the unified agent system.
        
        This enhanced method extends the base create_project method with:
        - First-principles analysis
        - File structure generation
        - Code generation
        - Revolutionary metrics
        
        Args:
            name: Project name
            description: Project description
            
        Returns:
            Dictionary with project creation results
        """
        self.logger.info(f"Creating revolutionary project: {name}")
        self.logger.info(f"Using revolution level: {self.revolution_level}")
        self.logger.info(f"Using constraint elimination: {self.constraint_elimination}")
        
        try:
            # Apply first-principles analysis to the project description
            fp_analysis = None
            revolutionary_analysis = None
            
            if self.first_principles and self.revolutionary_approach:
                fp_analysis = self.first_principles.apply_first_principles(description)
                revolutionary_analysis = self.revolutionary_approach.apply_revolutionary_approach(fp_analysis)
            
            # Reset project state
            self.project_state = {key: "" for key in self.project_state}
            
            # Create timestamps for documentation
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Step 1: CEO Agent - Revolutionary Project Vision with first-principles thinking
            self.logger.info("CEO Agent: Creating revolutionary vision with first-principles thinking...")
            additional_context = {}
            if revolutionary_analysis:
                additional_context["first_principles_analysis"] = revolutionary_analysis
                
            vision = await self.process_with_agent(
                "ceo",
                f"Create a revolutionary vision for {name} using first-principles thinking: {description}",
                additional_context
            )
            
            # Step 2: CTO Agent - Revolutionary Technical Strategy
            self.logger.info("CTO Agent: Developing revolutionary technical strategy with first-principles thinking...")
            if self.cto_agent:
                # Use specialized CTO agent if available
                tech_strategy = await self.cto_agent.process(
                    f"Develop revolutionary technical strategy for {name} using first-principles thinking",
                    {"context": self.project_state["context"], "vision": vision, "technical_decisions": self.project_state["technical_decisions"]}
                )
                # Update project state
                self.project_state["technical_decisions"] += f"\n{tech_strategy}"
                self.project_state["context"] += f"\nCTO: {tech_strategy}"
            else:
                # Fall back to basic agent
                tech_strategy = await self.process_with_agent(
                    "cto",
                    f"Develop revolutionary technical strategy for {name} using first-principles thinking",
                    {"vision": vision, "first_principles_analysis": revolutionary_analysis} if revolutionary_analysis else {"vision": vision}
                )
            
            # Step 3: Architect Agent - Revolutionary Technical Design
            self.logger.info("Architect Agent: Creating revolutionary technical design with first-principles thinking...")
            architect_context = {"vision": vision, "tech_strategy": tech_strategy}
            if revolutionary_analysis:
                architect_context["first_principles_analysis"] = revolutionary_analysis
                
            design = await self.process_with_agent(
                "architect",
                f"Create revolutionary technical design for {name} using first-principles thinking",
                architect_context
            )
            
            # Step 4: Developer Agent - Revolutionary Implementation Plan
            self.logger.info("Developer Agent: Planning revolutionary implementation with first-principles thinking...")
            developer_context = {"design": design, "tech_strategy": tech_strategy}
            if revolutionary_analysis:
                developer_context["first_principles_analysis"] = revolutionary_analysis
                
            implementation = await self.process_with_agent(
                "developer",
                f"Plan revolutionary implementation for {name} using first-principles thinking",
                developer_context
            )
            
            # Create project structure
            # Strip whitespace from project name to avoid path issues
            safe_name = name.strip().replace(" ", "_")
            output_dir = os.path.join("projects", safe_name)
            os.makedirs(output_dir, exist_ok=True)
            
            # Track generated files
            generated_files = []
            
            # Save project documentation
            docs_dir = os.path.join(output_dir, "docs")
            os.makedirs(docs_dir, exist_ok=True)
            generated_files.append(docs_dir)
            
            # Save vision document with metadata
            vision_content = f"""# Revolutionary Project Vision

## Project Details
- Name: {safe_name}
- Description: {description}
- Generated: {timestamp}
- Revolution Level: {self.revolution_level}
- Constraint Elimination: {self.constraint_elimination}

## First-Principles Vision Analysis
{vision}
"""
            if revolutionary_analysis:
                vision_content += "\n## Revolutionary Analysis Summary\n"
                vision_content += json.dumps(revolutionary_analysis, indent=2)
                
            vision_path = os.path.join(docs_dir, "vision.md")
            self._save_file_with_encoding(vision_path, vision_content)
            generated_files.append(vision_path)
            
            # Save architecture document with metadata
            arch_content = f"""# Revolutionary Technical Architecture

## Project Details
- Name: {safe_name}
- Generated: {timestamp}
- Revolution Level: {self.revolution_level}

## First-Principles Architecture Analysis
{design}
"""
            arch_path = os.path.join(docs_dir, "architecture.md")
            self._save_file_with_encoding(arch_path, arch_content)
            generated_files.append(arch_path)
            
            # Save technical strategy document with metadata
            tech_content = f"""# Revolutionary Technical Strategy

## Project Details
- Name: {safe_name}
- Generated: {timestamp}
- Revolution Level: {self.revolution_level}

## First-Principles Technical Strategy
{tech_strategy}
"""
            tech_path = os.path.join(docs_dir, "technical_strategy.md")
            self._save_file_with_encoding(tech_path, tech_content)
            generated_files.append(tech_path)
            
            # Save implementation document with metadata
            impl_content = f"""# Revolutionary Implementation Plan

## Project Details
- Name: {safe_name}
- Generated: {timestamp}
- Revolution Level: {self.revolution_level}

## First-Principles Implementation Details
{implementation}
"""
            impl_path = os.path.join(docs_dir, "implementation.md")
            self._save_file_with_encoding(impl_path, impl_content)
            generated_files.append(impl_path)
            
            # Step 5: Create file structure (if enabled)
            file_structure = None
            if self.enable_file_structure and self.filesystem_agent:
                self.logger.info("Filesystem Agent: Creating revolutionary file structure...")
                try:
                    file_structure = await self.filesystem_agent.process(
                        f"Create revolutionary file structure for {name} using first-principles thinking",
                        {
                            "context": self.project_state["context"],
                            "vision": vision,
                            "tech_strategy": tech_strategy,
                            "design": design,
                            "implementation": implementation,
                            "filesystem_decisions": ""
                        }
                    )
                    
                    # Create the actual files and directories
                    if file_structure:
                        self.logger.info(f"Creating file structure in {output_dir}...")
                        created_files = await self.filesystem_agent.create_structure(output_dir, file_structure)
                        generated_files.extend(created_files)
                        
                        # Save structure analysis
                        structure_analysis = await self.filesystem_agent.analyze_structure(file_structure)
                        structure_analysis_path = os.path.join(docs_dir, "structure_analysis.md")
                        structure_analysis_content = f"""# Revolutionary File Structure Analysis

## Project: {safe_name}
- Generated: {timestamp}
- Revolution Level: {self.revolution_level}
- Constraint Elimination: {self.constraint_elimination}

## Structure Metrics
- Total Directories: {structure_analysis.get('total_directories', 0)}
- Total Files: {structure_analysis.get('total_files', 0)}
- Complexity Score: {structure_analysis.get('revolutionary_metrics', {}).get('complexity_score', 0)}
- Innovation Score: {structure_analysis.get('revolutionary_metrics', {}).get('innovation_score', 0)}
- Maintainability Score: {structure_analysis.get('revolutionary_metrics', {}).get('maintainability_score', 0)}
- Revolutionary Impact: {structure_analysis.get('revolutionary_metrics', {}).get('revolutionary_impact', 0)}

## Optimization Opportunities
{json.dumps(structure_analysis.get('optimization_opportunities', []), indent=2)}
"""
                        self._save_file_with_encoding(structure_analysis_path, structure_analysis_content)
                        generated_files.append(structure_analysis_path)
                except Exception as e:
                    self.logger.error(f"Error creating file structure: {str(e)}")
                    # Continue with the rest of the project creation
            
            # Step 6: Generate code (if enabled)
            code_analysis = None
            if self.enable_code_gen and self.code_generator and file_structure:
                self.logger.info("Code Generator: Generating revolutionary code...")
                try:
                    # Prepare project context for code generation
                    project_context = {
                        "vision": vision,
                        "tech_strategy": tech_strategy,
                        "design": design,
                        "implementation": implementation
                    }
                    
                    # Generate code for the project structure
                    generated_code = await self.code_generator.generate_project_code(
                        file_structure,
                        project_context,
                        output_dir
                    )
                    
                    # Analyze the generated code
                    code_analysis = await self.code_generator.analyze_generated_code(generated_code)
                    
                    # Save code analysis
                    code_analysis_path = os.path.join(docs_dir, "code_analysis.md")
                    code_analysis_content = f"""# Revolutionary Code Analysis

## Project: {safe_name}
- Generated: {timestamp}
- Revolution Level: {self.revolution_level}
- Constraint Elimination: {self.constraint_elimination}

## Code Metrics
- Total Files: {code_analysis.get('total_files', 0)}
- Total Lines: {code_analysis.get('total_lines', 0)}
- Languages: {json.dumps(code_analysis.get('languages', {}), indent=2)}
- Average Complexity: {code_analysis.get('average_complexity', 0)}

## Revolutionary Metrics
- Conventional Patterns: {code_analysis.get('revolutionary_metrics', {}).get('conventional_patterns', 0)}
- Revolutionary Patterns: {code_analysis.get('revolutionary_metrics', {}).get('revolutionary_patterns', 0)}
- Innovation Score: {code_analysis.get('revolutionary_metrics', {}).get('innovation_score', 0)}
- Disruption Factor: {code_analysis.get('revolutionary_metrics', {}).get('disruption_factor', 0)}
- 10x Improvement Score: {code_analysis.get('revolutionary_metrics', {}).get('10x_improvement_score', 0)}

## Optimization Opportunities
{json.dumps(code_analysis.get('optimization_opportunities', []), indent=2)}
"""
                    self._save_file_with_encoding(code_analysis_path, code_analysis_content)
                    generated_files.append(code_analysis_path)
                except Exception as e:
                    self.logger.error(f"Error generating code: {str(e)}")
                    # Continue with the rest of the project creation
            
            # Save project history with timestamps
            history_content = f"""# Revolutionary Project Development History
Generated: {timestamp}

## Project Details
- Name: {safe_name}
- Description: {description}
- Revolution Level: {self.revolution_level}
- Constraint Elimination: {self.constraint_elimination}
"""

            if revolutionary_analysis:
                history_content += "\n## First-Principles Analysis\n"
                history_content += json.dumps(revolutionary_analysis, indent=2)
            
            history_content += f"\n\n## Development Timeline using First-Principles Thinking\n{self.project_state['context']}\n"
            
            history_path = os.path.join(output_dir, "project_history.md")
            self._save_file_with_encoding(history_path, history_content)
            generated_files.append(history_path)
            
            # Create a project summary
            summary_content = f"""# {safe_name} - Revolutionary Project

## Project Overview
This project was created using Elon Musk's first-principles thinking approach to break down the problem to its fundamental components and reason up from there: {description}

## Documentation
- [Revolutionary Project Vision](docs/vision.md)
- [Revolutionary Technical Strategy](docs/technical_strategy.md)
- [Revolutionary Technical Architecture](docs/architecture.md)
- [Revolutionary Implementation Plan](docs/implementation.md)
- [Development History](project_history.md)

## Revolutionary Metrics
- Revolution Level: {self.revolution_level}
- Constraint Elimination: {self.constraint_elimination}
"""

            # Add file structure and code analysis if available
            if file_structure:
                summary_content += "- [File Structure Analysis](docs/structure_analysis.md)\n"
            if code_analysis:
                summary_content += "- [Code Analysis](docs/code_analysis.md)\n"
                
            summary_content += f"""
## Generated
This revolutionary project was generated by UnifiedOmniAgent v{self.version} using first-principles thinking on {timestamp}.
"""
            readme_path = os.path.join(output_dir, "README.md")
            self._save_file_with_encoding(readme_path, summary_content)
            generated_files.append(readme_path)
            
            return {
                "status": "success",
                "output_dir": output_dir,
                "timestamp": timestamp,
                "artifacts": {
                    "readme": "README.md",
                    "vision": "docs/vision.md",
                    "technical_strategy": "docs/technical_strategy.md",
                    "architecture": "docs/architecture.md",
                    "implementation": "docs/implementation.md",
                    "history": "project_history.md"
                },
                "revolutionary_metrics": self.get_revolutionary_metrics(),
                "enhanced_capabilities": {
                    "file_structure": file_structure is not None,
                    "code_generation": code_analysis is not None
                },
                "generated_files": generated_files
            }
            
        except Exception as e:
            self.logger.error(f"Project creation failed: {str(e)}")
            import traceback
            self.logger.error(traceback.format_exc())
            return {"status": "error", "error": str(e)}
