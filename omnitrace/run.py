#!/usr/bin/env python3
"""
OmnitrAIce Unified Launcher - Single entry point for all capabilities
"""

import argparse
import asyncio
import logging
import sys
import json
import os
import traceback
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

# Try to import the UnifiedOmniAgent with fallbacks for compatibility
try:
    from omnitrace.core.revolutionary_omniagent import UnifiedOmniAgent
except ImportError:
    try:
        from core.revolutionary_omniagent import UnifiedOmniAgent
    except ImportError:
        try:
            from revolutionary_omniagent import UnifiedOmniAgent
        except ImportError:
            try:
                from omnitrace.core.enhanced_omniagent import EnhancedOmniAgent as UnifiedOmniAgent
            except ImportError:
                try:
                    from core.enhanced_omniagent import EnhancedOmniAgent as UnifiedOmniAgent
                except ImportError:
                    try:
                        from enhanced_omniagent import EnhancedOmniAgent as UnifiedOmniAgent
                    except ImportError:
                        try:
                            from omnitrace.core.omniagent import OmniAgent as UnifiedOmniAgent
                        except ImportError:
                            try:
                                from core.omniagent import OmniAgent as UnifiedOmniAgent
                            except ImportError:
                                from omniagent import OmniAgent as UnifiedOmniAgent

# Configure logging
def setup_logging(debug_mode: bool = False) -> logging.Logger:
    """Set up logging with appropriate level based on debug mode."""
    log_level = logging.DEBUG if debug_mode else logging.INFO
    
    # Create logs directory if it doesn't exist
    Path("logs").mkdir(exist_ok=True)
    
    # Configure root logger
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(f"logs/omnitrace_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger("OmnitrAIce")

def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """Load configuration from YAML or JSON file if provided."""
    if not config_path:
        return {}
        
    config_path = Path(config_path)
    if not config_path.exists():
        logging.warning(f"Config file not found: {config_path}")
        return {}
        
    try:
        with open(config_path, 'r') as f:
            if config_path.suffix.lower() in ['.yaml', '.yml']:
                import yaml
                return yaml.safe_load(f)
            elif config_path.suffix.lower() == '.json':
                return json.load(f)
            else:
                logging.warning(f"Unsupported config file type: {config_path.suffix}")
                return {}
    except Exception as e:
        logging.error(f"Error loading config file: {e}")
        return {}

def print_ascii_banner():
    """Print an ASCII art banner for the OmnitrAIce system."""
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
║              UNIFIED REVOLUTIONARY PROJECT GENERATION                 ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
"""
    print(banner)
    print("\nInspired by Elon Musk's First-Principles Thinking")
    print("Breaking down problems to their fundamental truths")
    print("Targeting 10x improvements through revolutionary approaches\n")

def check_dependencies() -> bool:
    """Check if all required dependencies are installed."""
    try:
        import langchain_ollama
        import aiohttp
        return True
    except ImportError as e:
        logging.error(f"Missing dependency: {str(e)}")
        print(f"Error: Missing dependency - {str(e)}")
        print("Please install required dependencies:")
        print("  pip install langchain langchain-ollama aiohttp")
        return False

def main() -> None:
    """Main entry point for the OmnitrAIce unified launcher."""
    parser = argparse.ArgumentParser(description="OmnitrAIce Revolutionary Project Generator")
    parser.add_argument("--model", default="deepseek-r1:1.5b", help="LLM model to use")
    parser.add_argument("--web", action="store_true", help="Launch web interface")
    parser.add_argument("--project", help="Project name to create")
    parser.add_argument("--description", help="Project description")
    parser.add_argument("--code-gen", action="store_true", help="Enable code generation")
    parser.add_argument("--no-code-gen", action="store_true", help="Disable code generation")
    parser.add_argument("--config", help="Path to configuration file (YAML or JSON)")
    parser.add_argument("--revolution-level", 
                        choices=["moderate", "high", "maximum"], 
                        default="maximum", 
                        help="Level of revolutionary thinking (moderate=less aggressive, maximum=most aggressive)")
    parser.add_argument("--constraint-elimination",
                        choices=["cautious", "moderate", "aggressive"],
                        default="aggressive",
                        help="Level of constraint elimination (cautious=fewer constraints challenged, aggressive=most constraints challenged)")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    
    args = parser.parse_args()
    
    # Print ASCII banner
    print_ascii_banner()
    
    # Set up logging
    logger = setup_logging(args.verbose)
    logger.info("Starting OmnitrAIce Unified System")
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Load configuration
    config = load_config(args.config)
    logger.debug(f"Loaded configuration: {config}")
    
    try:
        # Initialize the unified agent
        agent = UnifiedOmniAgent(model_name=args.model)
        
        # Configure based on args and config
        if hasattr(agent, "set_revolution_level"):
            revolution_level = config.get("revolution_level", args.revolution_level)
            agent.set_revolution_level(revolution_level)
        
        if hasattr(agent, "set_constraint_elimination"):
            constraint_elimination = config.get("constraint_elimination", args.constraint_elimination)
            agent.set_constraint_elimination(constraint_elimination)
        
        # Handle code generation flags
        if hasattr(agent, "enable_code_generation"):
            if args.no_code_gen:
                code_gen = False
            else:
                code_gen = config.get("code_generation", args.code_gen)
            
            agent.enable_code_generation(code_gen)
        
        # Launch web UI if requested
        if args.web:
            logger.info("Launching web interface")
            # Try to launch with progressive fallbacks
            web_ui_launched = False
            
            # Try OmnitrAIceWebUI first
            if not web_ui_launched:
                try:
                    # Try to import from new structure first, with fallbacks
                    try:
                        from omnitrace.ui.web_ui import OmnitrAIceWebUI
                    except ImportError:
                        try:
                            from ui.web_ui import OmnitrAIceWebUI
                        except ImportError:
                            from web_ui import OmnitrAIceWebUI
                    
                    logger.info("Launching OmnitrAIceWebUI...")
                    ui = OmnitrAIceWebUI(agent=agent)
                    ui.launch()
                    web_ui_launched = True
                except Exception as e:
                    logger.error(f"Failed to launch OmnitrAIceWebUI: {e}")
                    logger.debug(traceback.format_exc())
            
            # Fall back to AgentCustomizationUI
            if not web_ui_launched:
                try:
                    try:
                        from omnitrace.ui.agent_customization_ui import AgentCustomizationUI
                    except ImportError:
                        try:
                            from ui.agent_customization_ui import AgentCustomizationUI
                        except ImportError:
                            from enhanced_omniagent import AgentCustomizationUI
                    
                    logger.info("Falling back to AgentCustomizationUI...")
                    # Convert UnifiedOmniAgent to EnhancedOmniAgent if needed
                    if hasattr(agent, "to_enhanced_agent"):
                        enhanced_agent = agent.to_enhanced_agent()
                    else:
                        enhanced_agent = agent
                        
                    ui = AgentCustomizationUI(enhanced_agent)
                    ui.launch()
                    web_ui_launched = True
                except Exception as e:
                    logger.error(f"Failed to launch AgentCustomizationUI: {e}")
                    logger.debug(traceback.format_exc())
            
            # If both UIs failed, notify the user and fall back to interactive mode
            if not web_ui_launched:
                print("Error: Failed to launch Web UI. Falling back to interactive mode.")
                logger.warning("All Web UI attempts failed, falling back to interactive mode")
                try:
                    asyncio.run(agent.run())
                except KeyboardInterrupt:
                    logger.info("Interactive mode terminated by user")
                    print("\nExiting OmnitrAIce")
                except Exception as e:
                    logger.error(f"Error in interactive mode: {e}")
                    sys.exit(1)
                
        # Generate project if name and description are provided
        elif args.project and args.description:
            logger.info(f"Generating project: {args.project}")
            try:
                result = asyncio.run(agent.create_project(args.project, args.description))
                if result.get("status") == "success":
                    logger.info(f"Project created successfully at: {result.get('output_dir')}")
                    print(f"\n✅ Project created successfully!")
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
                    logger.error(f"Project creation failed: {result.get('error')}")
                    print(f"\n❌ Error: {result.get('error')}")
            except Exception as e:
                logger.error(f"Error generating project: {e}")
                logger.debug(traceback.format_exc())
                print(f"Error generating project: {str(e)}")
                sys.exit(1)
        else:
            # Interactive mode
            logger.info("Starting interactive mode")
            try:
                asyncio.run(agent.run())
            except KeyboardInterrupt:
                logger.info("Interactive mode terminated by user")
                print("\nExiting OmnitrAIce")
            except Exception as e:
                logger.error(f"Error in interactive mode: {e}")
                logger.debug(traceback.format_exc())
                print(f"Error: {str(e)}")
                sys.exit(1)
    
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        logger.debug(traceback.format_exc())
        print(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
