#!/usr/bin/env python

"""
Launcher script for the enhanced OmnitrAIce with agent customization UI
"""

import os
import sys

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the enhanced agent
from enhanced_omniagent import main

if __name__ == "__main__":
    main()
