#!/usr/bin/env python3
"""
Setup script for cursor-analytics-mcp server.
"""

from setuptools import setup, find_packages

setup(
    name="cursor-analytics-mcp",
    version="0.1.0", 
    description="MCP server for cursor-analytics tools and context",
    author="Cursor Analytics Team",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "mcp>=1.0.0",
        "pandas>=2.2.0",
        "numpy>=1.24.0", 
        "snowflake-connector-python[pandas]>=3.6.0",
        "snowflake-snowpark-python>=1.9.0",
        "snowflake-sqlalchemy>=1.4.0",
        "python-dotenv>=0.19.0",
        "gspread>=5.7.0",
        "oauth2client>=4.1.3",
        "gspread-formatting>=1.1.0",
        "google-auth>=2.0.0",
        "google-api-python-client>=2.0.0",
        "google-auth-oauthlib>=1.0.0",
        "google-auth-httplib2>=0.2.0",
        "keyring>=23.0.0",
        "sqlalchemy>=1.4.0",
        "polars>=0.18.0",
        "pyspark>=3.5.0",
        "packaging>=21.0",
    ],
    entry_points={
        "console_scripts": [
            "cursor-analytics-mcp=cursor_analytics_mcp.server:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)