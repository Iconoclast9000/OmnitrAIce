#!/usr/bin/env python3
"""
OmnitrAIce System Test Script v1.1.0

This script tests all major components of the OmnitrAIce system to verify
they are working correctly after reorganization and consolidation.
"""

import os
import sys
import logging
import importlib
import traceback
from pathlib import Path
from datetime import datetime

# Ensure the project root is in the Python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

# Configure logging
def setup_logging():
    """Set up logging for the test script"""
    logger = logging.getLogger("SystemTest")
    logger.setLevel(logging.INFO)
    
    # Ensure logs directory exists
    Path(os.path.join(PROJECT_ROOT, "logs")).mkdir(exist_ok=True)
    
    # Create handlers
    file_handler = logging.FileHandler(
        os.path.join(PROJECT_ROOT, f"logs/system_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
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

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 80)
    print(f" {text}")
    print("=" * 80)

def print_result(name, success):
    """Print a test result with color coding"""
    if success:
        print(f"  ✅ {name}: SUCCESS")
    else:
        print(f"  ❌ {name}: FAILED")
    return success

def test_imports():
    """Test importing major components from the correct package structure"""
    print_header("Testing Imports")
    all_passed = True
    
    # List of modules to import
    modules_to_test = [
        ("omnitrace.core.omniagent", "OmniAgent"),
        ("omnitrace.core.enhanced_omniagent", "EnhancedOmniAgent"),
        ("omnitrace.core.revolutionary_omniagent", "UnifiedOmniAgent"),
        ("omnitrace.agents.cto_agent", "CTOAgent"),
        ("omnitrace.agents.filesystem_agent", "FilesystemAgent"),
        ("omnitrace.ui.web_ui", "OmnitrAIceWebUI"),
        ("omnitrace.utils.first_principles", "FirstPrinciplesAnalyzer"),
        ("omnitrace.generation.code_generator", "RevolutionaryCodeGenerator")
    ]
    
    for module_path, class_name in modules_to_test:
        try:
            module = importlib.import_module(module_path)
            class_obj = getattr(module, class_name)
            all_passed &= print_result(f"Import {module_path}.{class_name}", True)
        except (ImportError, AttributeError) as e:
            logger.error(f"Failed to import {module_path}.{class_name}: {e}")
            all_passed &= print_result(f"Import {module_path}.{class_name}", False)
    
    return all_passed

def test_agent_creation():
    """Test creating agent instances"""
    print_header("Testing Agent Creation")
    all_passed = True
    
    # Test OmniAgent
    try:
        from omnitrace.core.omniagent import OmniAgent
        agent = OmniAgent()
        all_passed &= print_result("Create OmniAgent", agent is not None)
    except Exception as e:
        logger.error(f"Failed to create OmniAgent: {e}")
        all_passed &= print_result("Create OmniAgent", False)
    
    # Test EnhancedOmniAgent
    try:
        from omnitrace.core.enhanced_omniagent import EnhancedOmniAgent
        agent = EnhancedOmniAgent()
        all_passed &= print_result("Create EnhancedOmniAgent", agent is not None)
    except Exception as e:
        logger.error(f"Failed to create EnhancedOmniAgent: {e}")
        all_passed &= print_result("Create EnhancedOmniAgent", False)
    
    # Test UnifiedOmniAgent
    try:
        from omnitrace.core.revolutionary_omniagent import UnifiedOmniAgent
        agent = UnifiedOmniAgent()
        all_passed &= print_result("Create UnifiedOmniAgent", agent is not None)
    except Exception as e:
        logger.error(f"Failed to create UnifiedOmniAgent: {e}")
        all_passed &= print_result("Create UnifiedOmniAgent", False)
    
    return all_passed

def test_file_existence():
    """Test existence of key files"""
    print_header("Testing File Existence")
    all_passed = True
    
    # Key paths to check
    paths_to_check = [
        "omnitrace/run.py",
        "omnitrace/core/omniagent.py",
        "omnitrace/core/enhanced_omniagent.py",
        "omnitrace/core/revolutionary_omniagent.py",
        "omnitrace/agents/cto_agent.py",
        "omnitrace/agents/filesystem_agent.py",
        "omnitrace/ui/web_ui.py",
        "omnitrace/utils/first_principles.py",
        "omnitrace/generation/code_generator.py",
        "run_web_ui.py",
        "run.py"
    ]
    
    for path in paths_to_check:
        full_path = os.path.join(PROJECT_ROOT, path)
        exists = os.path.exists(full_path)
        all_passed &= print_result(f"Exists: {path}", exists)
    
    return all_passed

def test_configuration():
    """Test configuration files"""
    print_header("Testing Configuration Files")
    all_passed = True
    
    # Check template files
    template_files = [
        "omnitrace/config/templates/ceo_template.json",
        "omnitrace/config/templates/cto_template.json",
        "omnitrace/config/templates/architect_template.json",
        "omnitrace/config/templates/developer_template.json",
        "omnitrace/config/templates/filesystem_template.json"
    ]
    
    for template_file in template_files:
        full_path = os.path.join(PROJECT_ROOT, template_file)
        exists = os.path.exists(full_path)
        all_passed &= print_result(f"Template exists: {template_file}", exists)
    
    # Check config files
    config_files = [
        "omnitrace/config/config_files/default_config.yaml",
    ]
    
    for config_file in config_files:
        full_path = os.path.join(PROJECT_ROOT, config_file)
        exists = os.path.exists(full_path)
        all_passed &= print_result(f"Config exists: {config_file}", exists)
    
    return all_passed

def test_documentation():
    """Test documentation files"""
    print_header("Testing Documentation Files")
    all_passed = True
    
    # Check documentation files
    doc_files = [
        "omnitrace/docs/architecture.md",
        "omnitrace/docs/development_guide.md",
        "omnitrace/docs/web_ui_guide.md",
        "omnitrace/CHANGE_LOG.md",
        "README.md",
        "REORGANIZATION_SUMMARY.md",
        "CONFIG_MIGRATION.md"
    ]
    
    for doc_file in doc_files:
        full_path = os.path.join(PROJECT_ROOT, doc_file)
        exists = os.path.exists(full_path)
        all_passed &= print_result(f"Doc exists: {doc_file}", exists)
    
    return all_passed

def main():
    """Run all system tests"""
    global logger
    logger = setup_logging()
    
    print("\n" + "=" * 80)
    print(" OmnitrAIce System Test v1.1.0")
    print("=" * 80)
    print(f" Running tests from: {PROJECT_ROOT}")
    print(" Testing system functionality after reorganization and consolidation")
    print("=" * 80)
    
    # Run all tests
    import_result = test_imports()
    agent_result = test_agent_creation()
    file_result = test_file_existence()
    config_result = test_configuration()
    doc_result = test_documentation()
    
    # Overall result
    all_passed = import_result and agent_result and file_result and config_result and doc_result
    
    print("\n" + "=" * 80)
    print(f" OVERALL TEST RESULT: {'SUCCESS' if all_passed else 'FAILED'}")
    print("=" * 80)
    
    if not all_passed:
        print("\nSome tests failed. Check the logs for details.")
        return 1
    
    print("\nAll tests passed! The system is properly consolidated.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
