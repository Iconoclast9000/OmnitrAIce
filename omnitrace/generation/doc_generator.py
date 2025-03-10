"""
Documentation Generator - Revolutionary documentation creation using first-principles thinking
"""

import os
import json
import logging
import asyncio
from typing import Dict, Any, List, Optional

class DocumentationGenerator:
    """Generates revolutionary documentation based on first-principles thinking"""
    
    def __init__(self, llm):
        """Initialize the Documentation Generator with first-principles thinking
        
        Args:
            llm: The LLM to use for generation
        """
        self.llm = llm
        self.logger = logging.getLogger(__name__)
        
        # Documentation templates for different types
        self.doc_templates = {
            "vision": """
            You are a Revolutionary Vision Documentation Generator inspired by Elon Musk's first-principles thinking.
            
            Task: Generate a vision document for: {project_name}
            Project Description: {project_description}
            Revolutionary Vision: {vision}
            
            Create a comprehensive vision document that captures the revolutionary essence of this project. Focus on:
            
            1. First-principles analysis of the fundamental problem being solved
            2. Revolutionary vision that challenges industry assumptions
            3. 10x improvement opportunities identified through first-principles
            4. Physics-based constraints vs. artificial constraints
            5. Revolutionary roadmap for achieving the vision
            
            Format the document in Markdown with clear sections, including:
            - Executive Summary
            - Revolutionary Vision
            - First-Principles Analysis
            - 10x Improvement Opportunities
            - Revolutionary Roadmap
            - Key Success Metrics
            
            Make this vision document truly revolutionary, challenging conventional approaches with clear first-principles reasoning.
            """,
            
            "technical_strategy": """
            You are a Revolutionary Technical Strategy Documentation Generator inspired by Elon Musk's first-principles thinking.
            
            Task: Generate a technical strategy document for: {project_name}
            Project Description: {project_description}
            Revolutionary Vision: {vision}
            Technical Strategy: {tech_strategy}
            
            Create a comprehensive technical strategy document that outlines the revolutionary technical approach. Focus on:
            
            1. First-principles analysis of the technical challenges
            2. Revolutionary technology selection based on fundamental capabilities
            3. Exponential scaling architecture and infrastructure
            4. Technical debt elimination through fundamental redesign
            5. Emerging technology opportunities for revolutionary impact
            
            Format the document in Markdown with clear sections, including:
            - Technical Strategy Overview
            - First-Principles Technical Analysis
            - Revolutionary Technology Selection
            - Exponential Scaling Design
            - Technical Debt Prevention
            - Emerging Technology Integration
            
            Make this technical strategy truly revolutionary, challenging conventional approaches with clear first-principles reasoning.
            """,
            
            "architecture": """
            You are a Revolutionary Architecture Documentation Generator inspired by Elon Musk's first-principles thinking.
            
            Task: Generate an architecture document for: {project_name}
            Project Description: {project_description}
            Revolutionary Vision: {vision}
            Technical Strategy: {tech_strategy}
            Architecture Design: {design}
            
            Create a comprehensive architecture document that outlines the revolutionary system design. Focus on:
            
            1. First-principles analysis of the essential system components
            2. Revolutionary component design challenging traditional boundaries
            3. Novel interaction patterns between system elements
            4. Architecture for exponential scaling and continuous evolution
            5. Breakthrough approaches to system resilience and optimization
            
            Format the document in Markdown with clear sections, including:
            - Architecture Overview
            - First-Principles Component Analysis
            - Revolutionary Component Design
            - System Interaction Patterns
            - Scaling and Evolution Architecture
            - Component Diagrams and Flows
            
            Make this architecture truly revolutionary, challenging conventional approaches with clear first-principles reasoning.
            """,
            
            "implementation": """
            You are a Revolutionary Implementation Documentation Generator inspired by Elon Musk's first-principles thinking.
            
            Task: Generate an implementation plan document for: {project_name}
            Project Description: {project_description}
            Revolutionary Vision: {vision}
            Technical Strategy: {tech_strategy}
            Architecture Design: {design}
            Implementation Plan: {implementation}
            
            Create a comprehensive implementation plan document that outlines the revolutionary development approach. Focus on:
            
            1. First-principles analysis of the implementation requirements
            2. Revolutionary implementation patterns challenging traditional approaches
            3. Extreme simplification of complex functionality
            4. Future-proof implementation strategies
            5. Breakthrough development practices for rapid iteration
            
            Format the document in Markdown with clear sections, including:
            - Implementation Overview
            - First-Principles Implementation Analysis
            - Revolutionary Code Organization
            - Key Algorithms and Data Structures
            - Development Workflow and Practices
            - Implementation Roadmap and Milestones
            
            Make this implementation plan truly revolutionary, challenging conventional approaches with clear first-principles reasoning.
            """,
            
            "readme": """
            You are a Revolutionary README Generator inspired by Elon Musk's first-principles thinking.
            
            Task: Generate a README for: {project_name}
            Project Description: {project_description}
            Revolutionary Vision: {vision}
            Technical Strategy: {tech_strategy}
            Architecture Design: {design}
            Implementation Plan: {implementation}
            
            Create a comprehensive README that summarizes the revolutionary project. Focus on:
            
            1. Clear explanation of the project's revolutionary purpose
            2. First-principles approach that differentiates this project
            3. Key revolutionary features and capabilities
            4. Revolutionary architecture and implementation highlights
            5. Getting started with the project
            
            Format the document in Markdown with clear sections, including:
            - Project Overview
            - Revolutionary Approach
            - Key Features
            - Architecture
            - Getting Started
            - Documentation
            
            Make this README truly compelling, highlighting the revolutionary nature of the project through clear first-principles reasoning.
            """
        }
    
    async def generate_document(self, 
                             doc_type: str,
                             project_name: str, 
                             project_description: str, 
                             project_context: Dict[str, Any]) -> str:
        """Generate a revolutionary document of the specified type
        
        Args:
            doc_type: Type of document to generate (vision, technical_strategy, architecture, implementation, readme)
            project_name: Name of the project
            project_description: Description of the project
            project_context: Context information about the project
            
        Returns:
            Generated document content as markdown
        """
        # Get template for this document type
        template = self.doc_templates.get(doc_type)
        if not template:
            self.logger.error(f"Unknown document type: {doc_type}")
            return f"Error: Unknown document type: {doc_type}"
        
        # Create prompt with project information
        from langchain_core.prompts import ChatPromptTemplate
        prompt = ChatPromptTemplate.from_template(template)
        
        # Prepare context
        context = {
            "project_name": project_name,
            "project_description": project_description,
            "vision": project_context.get("vision", ""),
            "tech_strategy": project_context.get("tech_strategy", ""),
            "design": project_context.get("design", ""),
            "implementation": project_context.get("implementation", "")
        }
        
        # Generate document using LLM
        self.logger.info(f"Generating revolutionary {doc_type} document for project: {project_name}")
        chain = prompt | self.llm
        result = await asyncio.to_thread(chain.invoke, context)
        
        # Extract document content
        doc_content = result.text if hasattr(result, "text") else str(result)
        
        # Add metadata header if not already present
        if not doc_content.startswith("# "):
            doc_type_title = doc_type.replace("_", " ").title()
            header = f"""# {project_name} - Revolutionary {doc_type_title}

Generated by OmnitrAIce with first-principles thinking on {self._get_timestamp()}

"""
            doc_content = header + doc_content
        
        self.logger.info(f"Generated revolutionary {doc_type} document with {len(doc_content)} characters")
        return doc_content
    
    async def generate_project_documentation(self,
                                         project_name: str,
                                         project_description: str,
                                         project_context: Dict[str, Any],
                                         output_dir: str) -> Dict[str, str]:
        """Generate all documentation for a revolutionary project
        
        Args:
            project_name: Name of the project
            project_description: Description of the project
            project_context: Context information about the project
            output_dir: Directory to write the documentation to
            
        Returns:
            Dictionary mapping document types to their file paths
        """
        self.logger.info(f"Generating complete documentation set for project: {project_name}")
        
        # Create docs directory if needed
        docs_dir = os.path.join(output_dir, "docs")
        os.makedirs(docs_dir, exist_ok=True)
        
        # Document types to generate
        doc_types = ["vision", "technical_strategy", "architecture", "implementation", "readme"]
        
        # Generate each document
        generated_docs = {}
        for doc_type in doc_types:
            doc_content = await self.generate_document(doc_type, project_name, project_description, project_context)
            
            # Determine file path based on type
            if doc_type == "readme":
                file_path = os.path.join(output_dir, "README.md")
            else:
                file_path = os.path.join(docs_dir, f"{doc_type}.md")
            
            # Save to file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(doc_content)
            
            generated_docs[doc_type] = file_path
            self.logger.info(f"Saved {doc_type} document to {file_path}")
        
        # Create documentation index
        index_content = f"""# {project_name} Documentation

Generated by OmnitrAIce DocumentationGenerator with first-principles thinking on {self._get_timestamp()}

## Available Documentation

- [Revolutionary Vision](vision.md)
- [Revolutionary Technical Strategy](technical_strategy.md)
- [Revolutionary Architecture](architecture.md)
- [Revolutionary Implementation Plan](implementation.md)
- [Project README](../README.md)

This documentation represents a revolutionary approach based on Elon Musk's first-principles thinking. It breaks down the project to its fundamental components and challenges conventional wisdom to achieve 10x improvements.
"""
        
        index_path = os.path.join(docs_dir, "index.md")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)
        
        generated_docs["index"] = index_path
        
        self.logger.info(f"Generated {len(generated_docs)} documentation files")
        return generated_docs
    
    def _get_timestamp(self) -> str:
        """Get current timestamp string"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
