"""
Setup script for OmnitrAIce - Revolutionary Project Generation System
"""

from setuptools import setup, find_packages

# Define version in the omnitrace package
__version__ = '1.0.0'

# Read long description from README
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="omnitrace",
    version=__version__,
    author="OmnitrAIce Team",
    author_email="info@omnitrace.ai",
    description="Revolutionary Project Generation with First-Principles Thinking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omnitrace/omnitrace",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'omnitrace': ['config/templates/*.json', 'config/config_files/*.yaml'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.9",
    install_requires=[
        "langchain>=0.0.267",
        "langchain-ollama>=0.0.1",
        "gradio>=3.40.0",
        "pydantic>=2.0.0",
        "aiohttp>=3.8.5",
        "PyYAML>=6.0.0",
        "rich>=12.0.0",
    ],
    entry_points={
        'console_scripts': [
            'omnitrace=omnitrace.run:main',
        ],
    },
)
