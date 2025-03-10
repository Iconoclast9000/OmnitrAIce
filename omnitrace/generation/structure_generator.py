"""
Structure Generator - Revolutionary project structure creation using first-principles thinking
"""

import os
import json
import logging
import asyncio
from typing import Dict, Any, List, Optional

class StructureGenerator:
    """Generates revolutionary project structure based on first-principles thinking"""
    
    def __init__(self, llm):
        """Initialize the Structure Generator with first-principles thinking
        
        Args:
            llm: The LLM to use for generation
        """
        self.llm = llm
        self.logger = logging.getLogger(__name__)
        
        # Structure generation template
        self.structure_template = """
        You are a Revolutionary Structure Generator inspired by Elon Musk's first-principles thinking.
        
        Task: Generate a complete project structure for: {project_name}
        Project Description: {project_description}
        Project Vision: {vision}
        Technical Strategy: {tech_strategy}
        Architecture Design: {design}
        Implementation Plan: {implementation}
        
        Break down this structure creation task to its fundamental components. Don't use conventional project structures unless they truly represent the optimal organization. Focus on creating a 10x better structure by:
        
        1. Eliminating unnecessary complexity and nesting
        2. Designing from first principles
        3. Organizing by fundamental relationships rather than convention
        4. Challenging conventional project patterns
        5. Creating a revolutionary structure that enables exponential scaling
        
        First-Principles Analysis:
        1. What are the core components this project needs? Break it down to its fundamental elements.
        2. Are there artificial constraints in conventional project structures for this type of project?
        3. How can we organize this with 10x more clarity or 10x more evolvability?
        4. Which organizational patterns are truly necessary vs. conventionally used?
        5. How would we organize this if we were creating a software project structure from scratch?
        
        Generate the complete project structure, defining all key directories and files required for this project.
        
        Return the structure as a JSON object with this format:
        {{
          "project": "{project_name}",
          "root_directory": "{{project_name}}",
          "structure": {{
            "directories": [
              {{
                "name": "directory_name",
                "purpose": "Purpose description",
                "subdirectories": [
                  {{
                    "name": "subdirectory_name",
                    "purpose": "Purpose description",
                    "subdirectories": [],
                    "files": []
                  }}
                ],
                "files": [
                  {{
                    "name": "file_name.ext",
                    "purpose": "Purpose description",
                    "content_type": "code|configuration|data|documentation",
                    "content_summary": "Brief description of file content"
                  }}
                ]
              }}
            ],
            "files": [
              {{
                "name": "root_file.ext",
                "purpose": "Purpose description",
                "content_type": "code|configuration|data|documentation",
                "content_summary": "Brief description of file content"
              }}
            ]
          }}
        }}
        
        Your response should be ONLY the JSON object with no explanation, comments, or markdown formatting.
        """
    
    async def generate_structure(self, 
                               project_name: str, 
                               project_description: str, 
                               project_context: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a revolutionary project structure
        
        Args:
            project_name: Name of the project
            project_description: Description of the project
            project_context: Context information about the project
            
        Returns:
            Dictionary containing the generated structure
        """
        # Create prompt with project information
        from langchain_core.prompts import ChatPromptTemplate
        prompt = ChatPromptTemplate.from_template(self.structure_template)
        
        # Prepare context
        context = {
            "project_name": project_name,
            "project_description": project_description,
            "vision": project_context.get("vision", ""),
            "tech_strategy": project_context.get("tech_strategy", ""),
            "design": project_context.get("design", ""),
            "implementation": project_context.get("implementation", "")
        }
        
        # Generate structure using LLM
        self.logger.info(f"Generating revolutionary structure for project: {project_name}")
        chain = prompt | self.llm
        result = await asyncio.to_thread(chain.invoke, context)
        
        # Extract structure from response
        structure_text = result.text if hasattr(result, "text") else str(result)
        
        try:
            # Parse JSON structure (handling potential markdown formatting)
            import re
            
            # Try to extract JSON if wrapped in markdown code blocks
            json_match = re.search(r'```(?:json)?\n(.*?)\n```', structure_text, re.DOTALL)
            if json_match:
                structure_json = json_match.group(1)
            else:
                structure_json = structure_text
            
            structure = json.loads(structure_json)
            
            # Add metadata
            structure["metadata"] = {
                "generation_timestamp": self._get_timestamp(),
                "project_description": project_description,
            }
            
            self.logger.info(f"Generated revolutionary structure with {self._count_items(structure)} items")
            return structure
            
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse structure JSON: {str(e)}")
            # Return error info for debugging
            return {
                "error": "JSON parsing error",
                "error_details": str(e),
                "raw_text": structure_text
            }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp string"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _count_items(self, structure: Dict[str, Any]) -> int:
        """Count the total number of directories and files in the structure"""
        count = 0
        
        # Count root files
        root_files = structure.get("structure", {}).get("files", [])
        count += len(root_files)
        
        # Count directories and their contents recursively
        directories = structure.get("structure", {}).get("directories", [])
        
        def count_directory(directory):
            nonlocal count
            # Count this directory
            count += 1
            # Count files in this directory
            count += len(directory.get("files", []))
            # Count subdirectories recursively
            for subdir in directory.get("subdirectories", []):
                count_directory(subdir)
        
        for directory in directories:
            count_directory(directory)
            
        return count
    
    async def create_physical_structure(self, output_dir: str, structure: Dict[str, Any]) -> List[str]:
        """Create physical directories and files based on structure
        
        Args:
            output_dir: Path to create the structure in
            structure: The structure definition
            
        Returns:
            List of created files and directories
        """
        self.logger.info(f"Creating physical structure in: {output_dir}")
        
        created_items = []
        root_directory = os.path.join(output_dir, structure.get("root_directory", ""))
        
        # Create root directory
        os.makedirs(root_directory, exist_ok=True)
        created_items.append(root_directory)
        
        # Create root files
        for file_info in structure.get("structure", {}).get("files", []):
            file_path = os.path.join(root_directory, file_info["name"])
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# {file_info['purpose']}\n\n# Generated by OmnitrAIce StructureGenerator with first-principles thinking\n\n")
            created_items.append(file_path)
        
        # Create directories and their contents recursively
        async def create_directory(parent_path, directory_info):
            # Create this directory
            directory_path = os.path.join(parent_path, directory_info["name"])
            os.makedirs(directory_path, exist_ok=True)
            created_items.append(directory_path)
            
            # Create README with purpose description
            readme_path = os.path.join(directory_path, "README.md")
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(f"# {directory_info['name']}\n\n{directory_info['purpose']}\n\n_Generated by OmnitrAIce StructureGenerator with first-principles thinking_\n")
            created_items.append(readme_path)
            
            # Create files in this directory
            for file_info in directory_info.get("files", []):
                file_path = os.path.join(directory_path, file_info["name"])
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"# {file_info['purpose']}\n\n# Generated by OmnitrAIce StructureGenerator with first-principles thinking\n\n")
                created_items.append(file_path)
            
            # Create subdirectories recursively
            for subdir_info in directory_info.get("subdirectories", []):
                await create_directory(directory_path, subdir_info)
        
        # Process all root directories
        for directory_info in structure.get("structure", {}).get("directories", []):
            await create_directory(root_directory, directory_info)
        
        # Save structure definition file
        structure_path = os.path.join(root_directory, ".structure.json")
        with open(structure_path, "w", encoding="utf-8") as f:
            json.dump(structure, f, indent=2)
        created_items.append(structure_path)
        
        self.logger.info(f"Created {len(created_items)} files and directories")
        return created_items
    
    async def analyze_structure(self, structure: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze the revolutionary nature of the generated structure
        
        Args:
            structure: The generated structure
            
        Returns:
            Analysis results with revolutionary metrics
        """
        self.logger.info("Analyzing revolutionary structure")
        
        # Calculate statistics
        dir_count = 0
        file_count = 0
        nesting_depth = 0
        
        # Process directories recursively
        directories = structure.get("structure", {}).get("directories", [])
        
        def analyze_directory(directory, depth=1):
            nonlocal dir_count, file_count, nesting_depth
            
            # Count this directory
            dir_count += 1
            
            # Track maximum nesting depth
            nesting_depth = max(nesting_depth, depth)
            
            # Count files in this directory
            file_count += len(directory.get("files", []))
            
            # Process subdirectories recursively
            for subdir in directory.get("subdirectories", []):
                analyze_directory(subdir, depth + 1)
        
        # Count root files
        root_files = structure.get("structure", {}).get("files", [])
        file_count += len(root_files)
        
        # Process all directories
        for directory in directories:
            analyze_directory(directory)
        
        # Calculate revolutionary metrics
        # (These would be more sophisticated in a full implementation)
        complexity_score = 0.5 + (0.5 * (1 - (nesting_depth / 10)))  # Lower nesting is better
        innovation_score = 0.7 + (0.3 * (dir_count / (dir_count + file_count)))  # Balance between dirs and files
        maintainability_score = 0.8 - (0.2 * (nesting_depth / 5))  # Lower nesting is more maintainable
        revolutionary_impact = (complexity_score + innovation_score + maintainability_score) / 3
        
        # Generate analysis
        analysis = {
            "statistics": {
                "total_directories": dir_count,
                "total_files": file_count,
                "nesting_depth": nesting_depth,
                "total_items": dir_count + file_count
            },
            "revolutionary_metrics": {
                "complexity_score": round(complexity_score, 2),
                "innovation_score": round(innovation_score, 2),
                "maintainability_score": round(maintainability_score, 2),
                "revolutionary_impact": round(revolutionary_impact, 2)
            },
            "optimization_opportunities": [
                {
                    "type": "simplification",
                    "description": "Consider reducing nesting depth for better maintainability",
                    "impact": "Would improve comprehension and navigation"
                },
                {
                    "type": "organization",
                    "description": "Group related functionality by fundamental relationship rather than technical boundaries",
                    "impact": "Would align structure with revolutionary intent"
                },
                {
                    "type": "evolutionary_design",
                    "description": "Ensure structure enables exponential growth without rewrites",
                    "impact": "Would support revolutionary evolution of the project"
                }
            ]
        }
        
        return analysis
