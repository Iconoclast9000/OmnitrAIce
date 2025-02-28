"""
OmniAgent - Streamlined project generation using LangChain and Ollama
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

class OmniAgent:
    """Main OmniAgent system for project generation"""

    def __init__(self, model_name: str = "deepseek-r1:1.5b"):
        self.logger = self._setup_logger()
        
        # Initialize LLM
        self.llm = OllamaLLM(model=model_name)
        
        # Agent templates
        self.agent_templates = {
            "ceo": """
            You are the CEO Agent responsible for high-level project vision.
            Current Project Context: {context}
            Task: {task}
            
            Focus on:
            1. Project requirements
            2. Resource allocation
            3. Timeline planning
            4. Risk assessment
            
            Previous Decisions: {decisions}
            
            Provide your analysis and decisions.
            """,
            
            "architect": """
            You are the Architect Agent responsible for technical design.
            Current Project Context: {context}
            Task: {task}
            CEO's Vision: {vision}
            
            Focus on:
            1. System architecture
            2. Component design
            3. Technical patterns
            4. Integration points
            
            Previous Designs: {designs}
            
            Provide your technical design decisions.
            """,
            
            "developer": """
            You are the Developer Agent responsible for implementation.
            Current Project Context: {context}
            Task: {task}
            Architecture Design: {design}
            
            Focus on:
            1. Code structure
            2. File organization
            3. Implementation details
            4. Best practices
            
            Previous Work: {work}
            
            Provide specific implementation details.
            """
        }
        
        # Initialize agent chains
        self.agent_chains = {
            role: ChatPromptTemplate.from_template(template) | self.llm
            for role, template in self.agent_templates.items()
        }
        
        # Project state
        self.project_state = {
            "context": "",
            "decisions": "",
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

    async def process_with_agent(
        self,
        role: str,
        task: str,
        additional_context: Dict[str, Any] = None
    ) -> str:
        """Process task with specific agent"""
        try:
            # Prepare context
            context = {
                "context": self.project_state["context"],
                "task": task,
                "decisions": self.project_state["decisions"],
                "designs": self.project_state["designs"],
                "work": self.project_state["work"],
                "vision": self.project_state["decisions"],  # CEO's decisions as vision
                "design": self.project_state["designs"]  # Architect's designs
            }
            
            # Add any additional context
            if additional_context:
                context.update(additional_context)
            
            # Process with agent
            chain = self.agent_chains[role]
            result = await asyncio.to_thread(chain.invoke, context)
            
            # Extract response
            response = result.text if hasattr(result, "text") else str(result)
            
            # Update project state based on role
            if role == "ceo":
                self.project_state["decisions"] += f"\n{response}"
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
        """Create project using agent collaboration"""
        try:
            # Reset project state
            self.project_state = {key: "" for key in self.project_state}
            
            # Create timestamps for documentation
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Step 1: CEO Agent - Project Vision
            self.logger.info("CEO Agent: Analyzing project requirements...")
            vision = await self.process_with_agent(
                "ceo",
                f"Analyze project requirements for {name}: {description}"
            )
            
            # Step 2: Architect Agent - Technical Design
            self.logger.info("Architect Agent: Creating technical design...")
            design = await self.process_with_agent(
                "architect",
                f"Create technical design for {name}",
                {"vision": vision}
            )
            
            # Step 3: Developer Agent - Implementation
            self.logger.info("Developer Agent: Planning implementation...")
            implementation = await self.process_with_agent(
                "developer",
                f"Plan implementation for {name}",
                {"design": design}
            )
            
            # Create project structure
            output_dir = os.path.join("projects", name)
            os.makedirs(output_dir, exist_ok=True)
            
            # Save project documentation
            docs_dir = os.path.join(output_dir, "docs")
            os.makedirs(docs_dir, exist_ok=True)
            
            # Save vision document with metadata
            vision_content = f"""# Project Vision

## Project Details
- Name: {name}
- Description: {description}
- Generated: {timestamp}

## Vision Statement
{vision}
"""
            with open(os.path.join(docs_dir, "vision.md"), "w") as f:
                f.write(vision_content)
            
            # Save architecture document with metadata
            arch_content = f"""# Technical Architecture

## Project Details
- Name: {name}
- Generated: {timestamp}

## Architecture Overview
{design}
"""
            with open(os.path.join(docs_dir, "architecture.md"), "w") as f:
                f.write(arch_content)
            
            # Save implementation document with metadata
            impl_content = f"""# Implementation Plan

## Project Details
- Name: {name}
- Generated: {timestamp}

## Implementation Details
{implementation}
"""
            with open(os.path.join(docs_dir, "implementation.md"), "w") as f:
                f.write(impl_content)
            
            # Save project history with timestamps
            history_content = f"""# Project Development History
Generated: {timestamp}

## Project Details
- Name: {name}
- Description: {description}

## Development Timeline
{self.project_state['context']}
"""
            with open(os.path.join(output_dir, "project_history.md"), "w") as f:
                f.write(history_content)
            
            # Create a project summary
            summary_content = f"""# {name}

## Project Overview
{description}

## Documentation
- [Project Vision](docs/vision.md)
- [Technical Architecture](docs/architecture.md)
- [Implementation Plan](docs/implementation.md)
- [Development History](project_history.md)

## Generated
This project was generated by OmnitrAIce on {timestamp}.
"""
            with open(os.path.join(output_dir, "README.md"), "w") as f:
                f.write(summary_content)
            
            return {
                "status": "success",
                "output_dir": output_dir,
                "timestamp": timestamp,
                "artifacts": {
                    "readme": "README.md",
                    "vision": "docs/vision.md",
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
        print("\nOmnitrAIce System Initialized")
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
                        print("\nCreation Result:")
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
        print("\nAvailable Commands:")
        print("  help   - Show this help message")
        print("  create - Create new project (format: create ProjectName \"Project Description\")")
        print("  exit   - Exit the system")
        print("\nExample:")
        print('  create TaskFlow "A task management system with real-time updates"')

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