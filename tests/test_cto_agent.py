"""
Test cases for the CTO Agent
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
    from omnitrace.agents.cto_agent import CTOAgent
except ImportError:
    try:
        from agents.cto_agent import CTOAgent
    except ImportError:
        from cto_agent import CTOAgent

class TestCTOAgent(unittest.TestCase):
    """Test suite for CTO Agent"""
    
    def setUp(self):
        """Set up test case"""
        # Mock LLM to avoid actual calls during testing
        self.mock_llm = MagicMock()
        self.mock_llm.invoke = MagicMock(return_value=MagicMock(text="Test response"))
        
        # Create CTO Agent with mocked LLM
        self.agent = CTOAgent(llm=self.mock_llm)
        
    def test_agent_initialization(self):
        """Test that the agent initializes correctly"""
        self.assertIsNotNone(self.agent)
        self.assertIsNotNone(self.agent.template)
        self.assertIsNotNone(self.agent.parameters)
        
        # Check that default parameters are set
        self.assertEqual(self.agent.parameters["strategy_level"], "high")
        self.assertEqual(self.agent.parameters["detail_level"], "medium")
        self.assertTrue("Technical strategy" in self.agent.parameters["focus_areas"])
        
    @patch('asyncio.to_thread')
    async def test_process(self, mock_to_thread):
        """Test that process works correctly"""
        # Mock response from LLM
        mock_result = MagicMock()
        mock_result.text = "Test CTO strategy"
        mock_to_thread.return_value = mock_result
        
        # Test context
        context = {
            "context": "Project context",
            "vision": "CEO vision",
            "technical_decisions": ""
        }
        
        # Run the process method
        response = await self.agent.process("Create technical strategy", context)
        
        # Check that the response matches the mock result
        self.assertEqual(response, "Test CTO strategy")
        
        # Check that the LLM was called with the correct context
        mock_to_thread.assert_called_once()
        
    def test_custom_template(self):
        """Test that custom templates work correctly"""
        # Create a custom template
        custom_template = "Custom template with {task} and {context}"
        
        # Create agent with custom template
        agent = CTOAgent(llm=self.mock_llm, template=custom_template)
        
        # Check that the template was set correctly
        self.assertEqual(agent.template, custom_template)
        
    def test_custom_parameters(self):
        """Test that custom parameters work correctly"""
        # Create custom parameters
        custom_params = {
            "focus_areas": ["Custom focus 1", "Custom focus 2"],
            "strategy_level": "low",
            "detail_level": "high",
            "considerations": ["Custom consideration"]
        }
        
        # Create agent with custom parameters
        agent = CTOAgent(llm=self.mock_llm, parameters=custom_params)
        
        # Check that parameters were set correctly
        self.assertEqual(agent.parameters["focus_areas"], custom_params["focus_areas"])
        self.assertEqual(agent.parameters["strategy_level"], "low")
        self.assertEqual(agent.parameters["detail_level"], "high")
        self.assertEqual(agent.parameters["considerations"], ["Custom consideration"])
        
if __name__ == '__main__':
    unittest.main()
