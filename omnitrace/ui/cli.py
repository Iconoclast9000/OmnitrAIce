#!/usr/bin/env python3
"""
OmnitrAIce CLI - Command Line Interface for Revolutionary Project Generation
"""

import argparse
import asyncio
import logging
import sys
import json
import os
from datetime import datetime

# Import with fallbacks for compatibility
try:
    from omnitrace.core.revolutionary_omniagent import UnifiedOmniAgent
except ImportError:
    try:
        from core.revolutionary_omniagent import UnifiedOmniAgent
    except ImportError:
        try:
            from revolutionary_omniagent import UnifiedOmniAgent
        except ImportError:
            from enhanced_omniagent import EnhancedOmniAgent as UnifiedOmniAgent

class OmnitrAIceCLI:
    """Command Line Interface for OmnitrAIce system"""
    
    def __init__(self, agent=None, model_name: str = "deepseek-r1:1.5b"):
        """Initialize the CLI with an agent
        
        Args:
            agent: Optional pre-initialized agent
            model_name: Model name to use if creating a new agent
        """
        self.logger = self._setup_logger()
        self.agent = agent if agent else UnifiedOmniAgent(model_name)
    
    def _setup_logger(self) -> logging.Logger:
        """Set up logging"""
        logger = logging.getLogger("OmnitrAIceCLI")
        logger.setLevel(logging.INFO)
        
        # Ensure logs directory exists
        os.makedirs("logs", exist_ok=True)
        
        # File handler
        file_handler = logging.FileHandler(
            os.path.join("logs", f"cli_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
        )
        
        # Console handler
        console_handler = logging.StreamHandler()
        
        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def print_ascii_banner(self):
        """Print an ASCII art banner for OmnitrAIce"""
        banner = """
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║   ██████╗ ███╗   ███╗███╗   ██╗██╗████████╗██████╗  █████╗ ██╗ ██████╗███████╗   ║
║  ██╔═══██╗████╗ ████║████╗  ██║██║╚══██╔══╝██╔══██╗██╔══██╗██║██╔════╝██╔════╝   ║
║  ██║   ██║██╔████╔██║██╔██╗ ██║██║   ██║   ██████╔╝███████║██║██║     █████╗     ║
║  ██║   ██║██║╚██╔╝██║██║╚██╗██║██║   ██║   ██╔══██╗██╔══██║██║██║     ██╔══╝     ║
║  ╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║   ██║   ██║  ██║██║  ██║██║╚██████╗███████╗   ║
║   ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝   ║
║                                                                       ║
║         REVOLUTIONARY PROJECT GENERATION WITH FIRST PRINCIPLES        ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
"""
        print(banner)
        print("\nInspired by Elon Musk's First-Principles Thinking")
        print("Breaking down problems to their fundamental truths")
        print("Targeting 10x improvements through revolutionary approaches\n")
    
    def print_help(self):
        """Print available commands for interactive mode"""
        print("\nAvailable Revolutionary Commands:")
        print("  help   - Show this help message")
        print("  create - Create new revolutionary project using first-principles thinking")
        print("          (format: create ProjectName \"Project Description\")")
        print("  list   - List all generated projects")
        print("  config - Show or update configuration")
        print("          (format: config [parameter] [value])")
        print("  exit   - Exit the system")
        print("\nExample:")
        print('  create GravityDrive "A revolutionary propulsion system that manipulates spacetime"')
    
    def list_projects(self):
        """List all generated projects"""
        projects_dir = os.path.join(os.getcwd(), "projects")
        if not os.path.exists(projects_dir):
            print("No projects have been generated yet.")
            return
        
        projects = os.listdir(projects_dir)
        if not projects:
            print("No projects have been generated yet.")
            return
        
        print("\nGenerated Projects:")
        for i, project in enumerate(projects, 1):
            readme_path = os.path.join(projects_dir, project, "README.md")
            description = ""
            if os.path.exists(readme_path):
                with open(readme_path, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.strip().startswith("This project was created"):
                            description = line.strip()
                            break
            
            print(f"{i}. {project}")
            if description:
                print(f"   {description}")
            print()
    
    def show_config(self):
        """Show current configuration"""
        print("\nCurrent Configuration:")
        print(f"  Model: {self.agent.llm.model if hasattr(self.agent, 'llm') else 'unknown'}")
        
        if hasattr(self.agent, "revolution_level"):
            print(f"  Revolution Level: {self.agent.revolution_level}")
        
        if hasattr(self.agent, "constraint_elimination"):
            print(f"  Constraint Elimination: {self.agent.constraint_elimination}")
        
        if hasattr(self.agent, "enable_code_gen"):
            print(f"  Code Generation: {'Enabled' if self.agent.enable_code_gen else 'Disabled'}")
    
    def update_config(self, parameter, value):
        """Update a configuration parameter
        
        Args:
            parameter: Parameter to update
            value: New value
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if parameter == "revolution_level":
                if hasattr(self.agent, "set_revolution_level"):
                    self.agent.set_revolution_level(value)
                    return True
            
            elif parameter == "constraint_elimination":
                if hasattr(self.agent, "set_constraint_elimination"):
                    self.agent.set_constraint_elimination(value)
                    return True
            
            elif parameter == "code_generation":
                if hasattr(self.agent, "enable_code_generation"):
                    self.agent.enable_code_generation(value.lower() == "true")
                    return True
            
            return False
        except Exception as e:
            self.logger.error(f"Error updating configuration: {str(e)}")
            return False
    
    async def create_project(self, name: str, description: str) -> None:
        """Create a new revolutionary project
        
        Args:
            name: Project name
            description: Project description
        """
        try:
            print(f"\nCreating revolutionary project: {name}")
            print(f"Description: {description}")
            print("\nApplying first-principles thinking...\n")
            
            result = await self.agent.create_project(name, description)
            
            if result.get("status") == "success":
                print("\n✅ Project created successfully!")
                print(f"Output directory: {result.get('output_dir')}")
                
                # Display enhanced capability information if available
                if result.get("enhanced_capabilities"):
                    capabilities = result.get("enhanced_capabilities", {})
                    print("\nEnhanced capabilities used:")
                    print(f"- File structure generation: {'Yes' if capabilities.get('file_structure', False) else 'No'}")
                    print(f"- Code generation: {'Yes' if capabilities.get('code_generation', False) else 'No'}")
                
                # Display revolutionary metrics if available
                if result.get("revolutionary_metrics"):
                    metrics = result.get("revolutionary_metrics", {})
                    print("\nRevolutionary metrics:")
                    print(f"- Revolution level: {metrics.get('revolution_level', 'N/A')}")
                    print(f"- Constraint elimination: {metrics.get('constraint_elimination', 'N/A')}")
            else:
                print(f"\n❌ Error: {result.get('error', 'Unknown error')}")
        
        except Exception as e:
            self.logger.error(f"Error creating project: {str(e)}")
            print(f"\nError: {str(e)}")
    
    async def interactive_mode(self):
        """Run in interactive mode"""
        self.print_ascii_banner()
        print("Enter 'help' for commands or 'exit' to quit")
        
        while True:
            try:
                command = input("\nCommand > ").strip()
                
                if command.lower() == "exit":
                    break
                elif command.lower() == "help":
                    self.print_help()
                elif command.lower() == "list":
                    self.list_projects()
                elif command.lower() == "config":
                    self.show_config()
                elif command.lower().startswith("config "):
                    parts = command.split()
                    if len(parts) >= 3:
                        parameter = parts[1]
                        value = parts[2]
                        if self.update_config(parameter, value):
                            print(f"Configuration updated: {parameter} = {value}")
                        else:
                            print(f"Failed to update configuration. Invalid parameter or value.")
                    else:
                        print("Invalid format. Use: config [parameter] [value]")
                elif command.lower().startswith("create"):
                    parts = command.split('"')
                    if len(parts) >= 2:
                        name = parts[0].replace("create", "").strip()
                        description = parts[1].strip()
                        await self.create_project(name, description)
                    else:
                        print("Invalid format. Use: create ProjectName \"Project Description\"")
                else:
                    print("Unknown command. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                self.logger.error(f"Error in interactive mode: {str(e)}")
                print(f"\nError: {str(e)}")

def main():
    """Main entry point for OmnitrAIce CLI"""
    parser = argparse.ArgumentParser(description="OmnitrAIce Revolutionary Project Generator")
    parser.add_argument("--model", default="deepseek-r1:1.5b", help="LLM model to use")
    parser.add_argument("--project", help="Project name to create")
    parser.add_argument("--description", help="Project description")
    parser.add_argument("--revolution-level", 
                        choices=["moderate", "high", "maximum"], 
                        default="maximum", 
                        help="Level of revolutionary thinking (moderate=less aggressive, maximum=most aggressive)")
    parser.add_argument("--constraint-elimination",
                        choices=["cautious", "moderate", "aggressive"],
                        default="aggressive",
                        help="Level of constraint elimination (cautious=fewer constraints challenged, aggressive=most constraints challenged)")
    parser.add_argument("--code-gen", action="store_true", help="Enable code generation")
    parser.add_argument("--no-code-gen", action="store_true", help="Disable code generation")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    
    args = parser.parse_args()
    
    # Configure logging level
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level)
    
    try:
        # Initialize CLI
        cli = OmnitrAIceCLI(model_name=args.model)
        
        # Configure based on args
        if hasattr(cli.agent, "set_revolution_level"):
            cli.agent.set_revolution_level(args.revolution_level)
        
        if hasattr(cli.agent, "set_constraint_elimination"):
            cli.agent.set_constraint_elimination(args.constraint_elimination)
        
        if hasattr(cli.agent, "enable_code_generation"):
            # Handle code generation flags
            if args.no_code_gen:
                cli.agent.enable_code_generation(False)
            elif args.code_gen:
                cli.agent.enable_code_generation(True)
        
        # Run in appropriate mode
        if args.interactive:
            # Interactive mode
            asyncio.run(cli.interactive_mode())
        elif args.project and args.description:
            # Project creation mode
            cli.print_ascii_banner()
            asyncio.run(cli.create_project(args.project, args.description))
        else:
            # Default to interactive mode
            asyncio.run(cli.interactive_mode())
    
    except Exception as e:
        logging.error(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
