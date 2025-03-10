#!/usr/bin/env python3
"""
OmnitrAIce Project Launcher
"""

from enhanced_omniagent import AgentCustomizationUI, EnhancedOmniAgent

def main():
    """
    Launch the OmnitrAIce Agent Customization Interface
    """
    agent = EnhancedOmniAgent()
    ui = AgentCustomizationUI(agent)
    ui.launch()

if __name__ == "__main__":
    main()
