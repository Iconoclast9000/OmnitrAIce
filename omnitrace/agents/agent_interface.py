"""
Protocol defining the standard interface for all revolutionary agents in OmnitrAIce.
"""

from typing import Dict, Any, Protocol, Optional
from langchain_core.language_models import BaseLLM

class RevolutionaryAgent(Protocol):
    """Protocol defining the interface for all revolutionary agents."""
    
    def __init__(self, llm: BaseLLM, template: Optional[str] = None, 
                parameters: Optional[Dict[str, Any]] = None) -> None: ...
    
    async def process(self, task: str, context: Dict[str, Any]) -> str: ...
    
    def set_revolution_level(self, level: str) -> None: ...
    
    def set_constraint_elimination(self, level: str) -> None: ...
