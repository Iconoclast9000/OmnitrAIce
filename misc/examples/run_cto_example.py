"""
Example script to demonstrate the CTO Agent functionality
"""

import asyncio
import os
import sys
import json

# Add project root to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from omniagent import OmniAgent

async def main():
    """Run a simple example with CTO agent"""
    # Create OmniAgent instance
    agent = OmniAgent()
    
    print("\n===== CTO Agent Example =====\n")
    
    # Project details
    project_name = "TechCRM"
    project_description = "A cloud-based customer relationship management system with AI-powered insights"
    
    print(f"Project: {project_name}")
    print(f"Description: {project_description}")
    print("\nGenerating project with CTO agent integration...")
    
    # Create project
    result = await agent.create_project(project_name, project_description)
    
    # Display result
    if result["status"] == "success":
        print("\n✅ Project successfully generated!")
        print(f"Output directory: {result['output_dir']}")
        print("\nGenerated files:")
        for artifact_name, artifact_path in result["artifacts"].items():
            full_path = os.path.join(result["output_dir"], artifact_path)
            print(f"- {artifact_name}: {full_path}")
            
        # Show a preview of the CTO's technical strategy
        tech_strategy_path = os.path.join(result["output_dir"], result["artifacts"]["technical_strategy"])
        if os.path.exists(tech_strategy_path):
            print("\n===== Preview of Technical Strategy =====\n")
            with open(tech_strategy_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Show first 500 characters as preview
                preview = content[:500] + "..." if len(content) > 500 else content
                print(preview)
    else:
        print(f"\n❌ Error: {result.get('error', 'Unknown error')}")
    
    print("\n===== End of Example =====")

if __name__ == "__main__":
    asyncio.run(main())
