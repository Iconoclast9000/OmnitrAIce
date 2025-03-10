"""
Test cases for OmniAgent with CTO integration
"""

import sys
import os
import unittest
from unittest.mock import patch, MagicMock
import asyncio
import json

# Add project root to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Try importing from the new structure first, then fall back to old structure for compatibility
try:
    from omnitrace.core.omniagent import OmniAgent
except ImportError:
    try:
        from core.omniagent import OmniAgent
    except ImportError:
        from omniagent import OmniAgent

class TestOmniAgent(unittest.TestCase):
    """Test suite for OmniAgent"""
    
    def setUp(self):
        """Set up test case"""
        # Mock LLM to avoid actual calls during testing
        with patch('langchain_ollama.OllamaLLM'):
            self.agent = OmniAgent()
            
    def test_agent_initialization(self):
        """Test that the agent initializes correctly"""
        self.assertIsNotNone(self.agent)
        self.assertEqual(len(self.agent.agent_templates), 4)  # CEO, CTO, Architect, Developer
        self.assertIn("ceo", self.agent.agent_templates)
        self.assertIn("cto", self.agent.agent_templates)
        self.assertIn("architect", self.agent.agent_templates)
        self.assertIn("developer", self.agent.agent_templates)
        
        # Check that project state includes technical_decisions
        self.assertIn("technical_decisions", self.agent.project_state)
    
    @patch('asyncio.to_thread')
    async def test_process_with_cto_agent(self, mock_to_thread):
        """Test that process_with_agent works with CTO agent"""
        # Mock response from LLM
        mock_result = MagicMock()
        mock_result.text = "Test CTO strategy"
        mock_to_thread.return_value = mock_result
        
        # Test CTO agent processing
        response = await self.agent.process_with_agent("cto", "Test task")
        
        # Check the response
        self.assertEqual(response, "Test CTO strategy")
        
        # Check that project state was updated
        self.assertIn("Test CTO strategy", self.agent.project_state["technical_decisions"])
        self.assertIn("CTO: Test CTO strategy", self.agent.project_state["context"])
        
    @patch('asyncio.to_thread')
    async def test_create_project_with_cto(self, mock_to_thread):
        """Test that create_project includes CTO step"""
        # Mock responses from LLM for different agents
        responses = {
            "CEO: Test task": MagicMock(text="CEO Vision"),
            "CTO: Develop technical strategy for Test": MagicMock(text="CTO Strategy"),
            "ARCHITECT: Create technical design for Test": MagicMock(text="Architecture Design"),
            "DEVELOPER: Plan implementation for Test": MagicMock(text="Implementation Plan")
        }
        
        # Configure mock to return different responses based on input
        def side_effect(chain, context):
            task = context.get("task", "")
            for key, response in responses.items():
                if key in task:
                    return response
            return MagicMock(text="Default response")
            
        mock_to_thread.side_effect = side_effect
        
        # Mock file operations
        with patch('os.makedirs'), patch('builtins.open', MagicMock()), patch.object(self.agent, '_save_file_with_encoding', return_value=True):
            # Call create_project
            result = await self.agent.create_project("Test", "Test description")
            
            # Verify result contains CTO artifact
            self.assertEqual(result["status"], "success")
            self.assertIn("technical_strategy", result["artifacts"])
            self.assertEqual(result["artifacts"]["technical_strategy"], "docs/technical_strategy.md")
        
if __name__ == '__main__':
    unittest.main()
