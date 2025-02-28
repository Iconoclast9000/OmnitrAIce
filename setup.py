"""
Setup script for OmnitrAIce
"""

import os
import sys
import subprocess

def setup_directories():
    """Create necessary directories"""
    directories = [
        "config",
        "config/templates",
        "projects",
        "misc/docs",
        "misc/examples"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def check_requirements():
    """Check if requirements are installed"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("All requirements installed successfully.")
        return True
    except subprocess.CalledProcessError:
        print("Failed to install requirements.")
        return False

def main():
    """Main setup function"""
    print("=" * 50)
    print("OmnitrAIce Setup")
    print("=" * 50)
    
    # Create directories
    setup_directories()
    
    # Check requirements
    check_requirements()
    
    print("\nSetup completed successfully!")
    print("\nTo start OmnitrAIce with the customization UI, run:")
    print("python run_omnitrace.py")

if __name__ == "__main__":
    main()
