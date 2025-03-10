# If you're seeing this comment, this is the file you should be using for the web UI
"""
OmnitrAIce Web UI Universal Launcher v1.1.0

This launcher handles path issues and provides a universal entry point
for all web UI options, with robust error handling and logging.
"""

import sys
import os
import logging
import traceback
from datetime import datetime
from pathlib import Path

# Ensure the project root is in the Python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

# Configure logging
def setup_logging():
    """Set up comprehensive logging for the Web UI Launcher"""
    logger = logging.getLogger("WebUILauncher")
    logger.setLevel(logging.INFO)
    
    # Ensure logs directory exists
    Path(os.path.join(PROJECT_ROOT, "logs")).mkdir(exist_ok=True)
    
    # Create handlers
    file_handler = logging.FileHandler(
        os.path.join(PROJECT_ROOT, f"logs/web_ui_launcher_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    )
    console_handler = logging.StreamHandler()
    
    # Create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

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

def main():
    """
    Launch the OmnitrAIce Web Interface with maximum compatibility
    and proper path handling.
    """
    logger = setup_logging()
    logger.info("Starting OmnitrAIce Web UI Universal Launcher v1.1.0")
    
    # Print the ASCII banner
    print_ascii_banner()
    
    # First approach: Try using the AgentCustomizationUI with EnhancedOmniAgent
    logger.info("Attempting to launch the AgentCustomizationUI...")
    
    try:
        # Import with proper path handling - most reliable approach
        try:
            from omnitrace.core.enhanced_omniagent import EnhancedOmniAgent
            from omnitrace.ui.agent_customization_ui import AgentCustomizationUI
            logger.info("Successfully imported from omnitrace package structure")
        except ImportError:
            logger.info("Falling back to root imports...")
            from enhanced_omniagent import EnhancedOmniAgent, AgentCustomizationUI
        
        # Initialize the agent and UI
        agent = EnhancedOmniAgent()
        ui = AgentCustomizationUI(agent)
        
        # Launch the UI
        logger.info("Launching AgentCustomizationUI")
        ui.launch()
        return  # Exit if successful
    except Exception as e:
        logger.error(f"Failed to launch AgentCustomizationUI: {str(e)}")
        logger.error(traceback.format_exc())
        print(f"ERROR: Could not launch AgentCustomizationUI: {str(e)}")
    
    # Second approach: Try using the Revolutionary Web UI
    logger.info("Attempting to launch the OmnitrAIceWebUI...")
    
    try:
        # Import with proper path handling
        try:
            from omnitrace.core.revolutionary_omniagent import UnifiedOmniAgent
            from omnitrace.ui.web_ui import OmnitrAIceWebUI
            logger.info("Successfully imported from omnitrace package structure")
        except ImportError:
            logger.info("Falling back to root imports...")
            # Try direct import
            try:
                from revolutionary_omniagent import UnifiedOmniAgent
                from web_ui import OmnitrAIceWebUI
            except ImportError:
                # Last resort - try dynamic import using importlib
                import importlib.util
                
                spec = importlib.util.spec_from_file_location(
                    "revolutionary_omniagent", 
                    os.path.join(PROJECT_ROOT, "omnitrace", "core", "revolutionary_omniagent.py")
                )
                if spec:
                    revolutionary_omniagent = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(revolutionary_omniagent)
                    UnifiedOmniAgent = revolutionary_omniagent.UnifiedOmniAgent
                
                spec = importlib.util.spec_from_file_location(
                    "web_ui", 
                    os.path.join(PROJECT_ROOT, "omnitrace", "ui", "web_ui.py")
                )
                if spec:
                    web_ui = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(web_ui)
                    OmnitrAIceWebUI = web_ui.OmnitrAIceWebUI
        
        # Initialize the agent and UI
        agent = UnifiedOmniAgent()
        ui = OmnitrAIceWebUI(agent=agent)
        
        # Launch the UI
        logger.info("Launching OmnitrAIceWebUI")
        ui.launch()
        return  # Exit if successful
    except Exception as e:
        logger.error(f"Failed to launch OmnitrAIceWebUI: {str(e)}")
        logger.error(traceback.format_exc())
        print(f"ERROR: Could not launch OmnitrAIceWebUI: {str(e)}")
    
    # Third approach: Fall back to running the Python module directly
    logger.info("Attempting to run the module directly...")
    
    try:
        print("Launching via Python module...")
        command = f"{sys.executable} -m omnitrace.run --web"
        os.system(command)
        return  # Exit if successful
    except Exception as e:
        logger.error(f"Failed to run module: {str(e)}")
        logger.error(traceback.format_exc())
        print(f"ERROR: All launch attempts failed. See logs for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()
