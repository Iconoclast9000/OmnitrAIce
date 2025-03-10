#!/usr/bin/env python3
"""
Revolutionary OmnitrAIce Runner - Launch the Enhanced OmniAgent with revolutionary file and code generation

This script launches the Enhanced OmniAgent with revolutionary capabilities for generating
complete projects with actual implementation files using Elon Musk's first-principles thinking.
"""

import os
import sys
import asyncio
import argparse
import logging
from typing import Dict, Any, Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("OmnitrAIce")

def print_ascii_banner():
    """Print an ASCII art banner for the revolutionary OmnitrAIce"""
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

def check_dependencies() -> bool:
    """Check if all required dependencies are installed"""
    try:
        import langchain_ollama
        import aiohttp
        return True
    except ImportError as e:
        logger.error(f"Missing dependency: {str(e)}")
        print(f"Error: Missing dependency - {str(e)}")
        print("Please install required dependencies:")
        print("  pip install langchain langchain-ollama aiohttp")
        return False

def check_enhanced_capabilities() -> bool:
    """Check if enhanced capabilities (file and code generation) are available"""
    try:
        import filesystem_agent
        import code_generator
        import first_principles
        return True
    except ImportError:
        logger.warning("Enhanced capabilities not available, running in documentation-only mode")
        print("\nWarning: Enhanced capabilities not available")
        print("The system will run in documentation-only mode.")
        print("To enable revolutionary file and code generation, make sure the following modules exist:")
        print("  - filesystem_agent.py")
        print("  - code_generator.py")
        print("  - first_principles.py\n")
        return False

def check_ollama_model(model_name: str = "deepseek-r1:1.5b") -> bool:
    """Check if the required Ollama model is available"""
    try:
        import aiohttp
        import asyncio
        
        async def check_model():
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get("http://localhost:11434/api/tags") as response:
                        if response.status == 200:
                            data = await response.json()
                            models = [model["name"] for model in data.get("models", [])]
                            return model_name in models
                        return False
            except Exception:
                return False
        
        return asyncio.run(check_model())
    except Exception:
        return False

def main():
    """Main entry point for the revolutionary OmnitrAIce runner"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Revolutionary OmnitrAIce - Project Generation with First-Principles Thinking")
    parser.add_argument("--model", default="deepseek-r1:1.5b", help="Model name to use (default: deepseek-r1:1.5b)")
    parser.add_argument("--project", help="Project name to create")
    parser.add_argument("--description", help="Project description")
    args = parser.parse_args()
    
    # Print ASCII banner
    print_ascii_banner()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check enhanced capabilities
    enhanced_capabilities = check_enhanced_capabilities()
    if enhanced_capabilities:
        print("✅ Enhanced capabilities available: Revolutionary file and code generation")
    else:
        print("⚠️ Running in documentation-only mode")
    
    # Check Ollama model
    if not check_ollama_model(args.model):
        print(f"⚠️ Warning: Model '{args.model}' not found in Ollama")
        print(f"Please install the model with: ollama pull {args.model}")
        print("Continuing anyway, but may fail if model is not available\n")
    else:
        print(f"✅ Model '{args.model}' is available in Ollama")
    
    print("\nInitializing Revolutionary OmnitrAIce System...")
    
    try:
        # Import EnhancedOmniAgent
        try:
            from enhanced_omniagent import EnhancedOmniAgent
        except ImportError:
            logger.error("Enhanced OmniAgent not found, falling back to regular OmniAgent")
            from omniagent import OmniAgent as EnhancedOmniAgent
        
        # Initialize agent
        agent = EnhancedOmniAgent(model_name=args.model)
        
        # If project and description are provided, create project non-interactively
        if args.project and args.description:
            print(f"\nCreating revolutionary project: {args.project}")
            print(f"Description: {args.description}")
            
            async def create_project():
                result = await agent.create_project(args.project, args.description)
                if result.get("status") == "success":
                    print("\n✅ Project created successfully!")
                    print(f"Output directory: {result.get('output_dir')}")
                    if result.get("enhanced_capabilities") and result.get("generated_files"):
                        print(f"Generated {len(result.get('generated_files'))} implementation files")
                else:
                    print("\n❌ Project creation failed:")
                    print(result.get("error", "Unknown error"))
                return result
            
            result = asyncio.run(create_project())
            return
        
        # Otherwise, run in interactive mode
        asyncio.run(agent.run())
        
    except KeyboardInterrupt:
        print("\nExiting Revolutionary OmnitrAIce System")
    except Exception as e:
        logger.exception("Fatal error")
        print(f"\nFatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
