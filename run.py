#!/usr/bin/env python3
"""
OmnitrAIce Compatibility Wrapper - Forwards to reorganized structure
"""

import sys
import os

# Ensure the omnitrace package is in the Python path
# This allows for proper importing regardless of where the script is run from
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Forward to the reorganized run.py in the omnitrace package"""
    print("Using reorganized OmnitrAIce structure...")
    
    try:
        # Import the run function from the omnitrace run.py
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "omnitrace"))
        from omnitrace.run import main as omnitrace_main
        
        # Forward to the main function
        omnitrace_main()
    except ImportError as e:
        print(f"Error: Failed to import from the reorganized structure: {e}")
        print("Make sure the omnitrace package is properly installed.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
