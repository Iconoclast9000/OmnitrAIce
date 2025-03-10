"""
OmniAgent - Revolutionary project generation using first-principles thinking with LangChain and Ollama
"""

import asyncio
import sys
import json
import os
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Import CTO Agent
try:
    from omnitrace.agents.cto_agent import CTOAgent
except ImportError:
    try:
        from agents.cto_agent import CTOAgent
    except ImportError:
        try:
            from cto_agent import CTOAgent
        except ImportError:
            # For backwards compatibility, CTO agent might not be available
            CTOAgent = None

class OmniAgent:
    """Main OmniAgent system for revolutionary project generation using first-principles thinking"""

    def __init__(self, model_name: str = "deepseek-r1:1.5b"):
        self.logger = self._setup_logger()
        
        # Initialize LLM
        self.llm = OllamaLLM(model=model_name)
        
        # Load agent templates from files if available
        self.agent_templates = self._load_agent_templates()
        
        # Initialize agent chains
        self.agent_chains = {
            role: ChatPromptTemplate.from_template(template) | self.llm
            for role, template in self.agent_templates.items()
        }
        
        # Project state
        self.project_state = {
            "context": "",
            "decisions": "",
            "technical_decisions": "",
            "designs": "",
            "work": ""
        }

    def _setup_logger(self) -> logging.Logger:
        """Initialize logging"""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        return logging.getLogger(__name__)
    
    def _load_agent_templates(self) -> Dict[str, str]:
        """Load agent templates from files if available, otherwise use defaults"""
        templates_dir = os.path.join("config", "templates")
        template_files = {
            "ceo": os.path.join(templates_dir, "ceo_template.json"),
            "cto": os.path.join(templates_dir, "cto_template.json"),
            "architect": os.path.join(templates_dir, "architect_template.json"),
            "developer": os.path.join(templates_dir, "developer_template.json")
        }
        
        # Default templates with first-principles thinking
        default_templates = {
            "ceo": """
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
            
            "cto": """
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
            
            "architect": """
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
            
            "developer": """
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
            """
        }
        
        # Load templates from files if they exist
        templates = {}
        for role, file_path in template_files.items():
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        templates[role] = data.get("template", default_templates[role])
                except Exception as e:
                    self.logger.error(f"Failed to load template for {role}: {str(e)}")
                    templates[role] = default_templates[role]
            else:
                templates[role] = default_templates[role]
        
        return templates
    
    def _save_file_with_encoding(self, file_path: str, content: str) -> bool:
        """Save file with UTF-8 encoding to handle special characters"""
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception as e:
            self.logger.error(f"Error saving file {file_path}: {str(e)}")
            return False

    async def process_with_agent(
        self,
        role: str,
        task: str,
        additional_context: Dict[str, Any] = None
    ) -> str:
        """Process a task with a specific agent using first-principles thinking
        
        All agents use Elon Musk's first-principles thinking to break down problems
        to their fundamental components and reason up from there.
        """
        try:
            # Prepare context
            context = {
                "context": self.project_state["context"],
                "task": task,
                "decisions": self.project_state["decisions"],
                "technical_decisions": self.project_state["technical_decisions"],
                "designs": self.project_state["designs"],
                "work": self.project_state["work"],
                "vision": self.project_state["decisions"],  # CEO's decisions as vision
                "design": self.project_state["designs"],  # Architect's designs
                "tech_strategy": self.project_state["technical_decisions"]  # CTO's technical strategy
            }
            
            # Add any additional context
            if additional_context:
                context.update(additional_context)
            
            # Process with agent
            self.logger.info(f"Applying first-principles thinking with {role.upper()} agent to: {task}")
            chain = self.agent_chains[role]
            result = await asyncio.to_thread(chain.invoke, context)
            
            # Extract response
            response = result.text if hasattr(result, "text") else str(result)
            
            # Update project state based on role
            if role == "ceo":
                self.project_state["decisions"] += f"\n{response}"
            elif role == "cto":
                self.project_state["technical_decisions"] += f"\n{response}"
            elif role == "architect":
                self.project_state["designs"] += f"\n{response}"
            elif role == "developer":
                self.project_state["work"] += f"\n{response}"
            
            self.project_state["context"] += f"\n{role.upper()}: {response}"
            
            return response
            
        except Exception as e:
            self.logger.error(f"Agent processing failed: {str(e)}")
            raise

    async def create_project(self, name: str, description: str) -> Dict[str, Any]:
        """Create revolutionary project using first-principles thinking and agent collaboration"""
        try:
            # Reset project state
            self.project_state = {key: "" for key in self.project_state}
            
            # Create timestamps for documentation
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Step 1: CEO Agent - Revolutionary Project Vision
            self.logger.info("CEO Agent: Creating revolutionary vision with first-principles thinking...")
            vision = await self.process_with_agent(
                "ceo",
                f"Create a revolutionary vision for {name} using first-principles thinking: {description}"
            )
            
            # Step 2: CTO Agent - Revolutionary Technical Strategy
            self.logger.info("CTO Agent: Developing revolutionary technical strategy with first-principles thinking...")
            tech_strategy = await self.process_with_agent(
                "cto",
                f"Develop revolutionary technical strategy for {name} using first-principles thinking",
                {"vision": vision}
            )
            
            # Step 3: Architect Agent - Revolutionary Technical Design
            self.logger.info("Architect Agent: Creating revolutionary technical design with first-principles thinking...")
            design = await self.process_with_agent(
                "architect",
                f"Create revolutionary technical design for {name} using first-principles thinking",
                {"vision": vision, "tech_strategy": tech_strategy}
            )
            
            # Step 4: Developer Agent - Revolutionary Implementation Plan
            self.logger.info("Developer Agent: Planning revolutionary implementation with first-principles thinking...")
            implementation = await self.process_with_agent(
                "developer",
                f"Plan revolutionary implementation for {name} using first-principles thinking",
                {"design": design, "tech_strategy": tech_strategy}
            )
            
            # Create project structure
            # Strip whitespace from project name to avoid path issues
            safe_name = name.strip()
            output_dir = os.path.join("projects", safe_name)
            os.makedirs(output_dir, exist_ok=True)
            
            # Save project documentation
            docs_dir = os.path.join(output_dir, "docs")
            os.makedirs(docs_dir, exist_ok=True)
            
            # Save vision document with metadata
            vision_content = f"""# Revolutionary Project Vision

## Project Details
- Name: {safe_name}
- Description: {description}
- Generated: {timestamp}

## First-Principles Vision Analysis
{vision}
"""
            self._save_file_with_encoding(os.path.join(docs_dir, "vision.md"), vision_content)
            
            # Save architecture document with metadata
            arch_content = f"""# Revolutionary Technical Architecture

## Project Details
- Name: {safe_name}
- Generated: {timestamp}

## First-Principles Architecture Analysis
{design}
"""
            self._save_file_with_encoding(os.path.join(docs_dir, "architecture.md"), arch_content)
            
            # Save technical strategy document with metadata
            tech_content = f"""# Revolutionary Technical Strategy

## Project Details
- Name: {safe_name}
- Generated: {timestamp}

## First-Principles Technical Strategy
{tech_strategy}
"""
            self._save_file_with_encoding(os.path.join(docs_dir, "technical_strategy.md"), tech_content)
            
            # Save implementation document with metadata
            impl_content = f"""# Revolutionary Implementation Plan

## Project Details
- Name: {safe_name}
- Generated: {timestamp}

## First-Principles Implementation Details
{implementation}
"""
            self._save_file_with_encoding(os.path.join(docs_dir, "implementation.md"), impl_content)
            
            # Save project history with timestamps
            history_content = f"""# Revolutionary Project Development History
Generated: {timestamp}

## Project Details
- Name: {safe_name}
- Description: {description}

## Development Timeline using First-Principles Thinking
{self.project_state['context']}
"""
            self._save_file_with_encoding(os.path.join(output_dir, "project_history.md"), history_content)
            
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

## Generated
This revolutionary project was generated by OmnitrAIce using first-principles thinking on {timestamp}.
"""
            self._save_file_with_encoding(os.path.join(output_dir, "README.md"), summary_content)
            
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
                }
            }
            
        except Exception as e:
            self.logger.error(f"Project creation failed: {str(e)}")
            return {"status": "error", "error": str(e)}

    async def run(self):
        """Run the OmniAgent system"""
        print("\nOmnitrAIce Revolutionary System Initialized")
        print("Enter 'help' for commands or 'exit' to quit")

        while True:
            try:
                command = input("\nCommand > ").strip()

                if command.lower() == "exit":
                    break
                elif command.lower() == "help":
                    self._print_help()
                elif command.lower().startswith("create"):
                    parts = command.split('"')
                    if len(parts) >= 2:
                        name = parts[0].replace("create", "").strip()
                        description = parts[1].strip()
                        result = await self.create_project(name, description)
                        print("\nRevolutionary Creation Result:")
                        print(json.dumps(result, indent=2))
                    else:
                        print("Invalid format. Use: create ProjectName \"Project Description\"")
                else:
                    print("Unknown command. Type 'help' for available commands.")

            except KeyboardInterrupt:
                break
            except Exception as e:
                self.logger.error(f"Error in main loop: {str(e)}")
                print(f"\nError: {str(e)}")

    def _print_help(self):
        """Print available commands"""
        print("\nAvailable Revolutionary Commands:")
        print("  help   - Show this help message")
        print("  create - Create new revolutionary project using first-principles thinking")
        print("          (format: create ProjectName \"Project Description\")")
        print("  exit   - Exit the system")
        print("\nExample:")
        print('  create GravityDrive "A revolutionary propulsion system that manipulates spacetime"')

def main():
    """Main entry point"""
    try:
        agent = OmniAgent()
        asyncio.run(agent.run())
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
