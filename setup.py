#!/usr/bin/python3

# import std libs
import os
import re
from pathlib import Path
from setuptools import setup

def find_version(*file_paths):
    """
    This pattern was modeled on a method from the Python Packaging User Guide:
        https://packaging.python.org/en/latest/single_source_version.html
    We read instead of importing so we don't get import errors if our code
    imports from dependencies listed in install_requires.
    """
    base_module_file = os.path.join(*file_paths)
    with open(base_module_file) as f:
        base_module_data = f.read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", base_module_data, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

with open("requirements.txt", "r") as f:
    INSTALL_REQUIRES = f.read().splitlines()

def get_packages(package):
    """Return root package and all sub-packages"""
    return [str(path.parent) for path in Path(package).glob("**/__init__.py")]

setup(
    name="vmanage-ops",
    version=find_version("nuts_custom_class", "__init__.py"),
    author="Brian Saunders",
    author_email="brian.t.saunders@gmail.com",
    description="nuts custom class test library",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/briantsaunders/nuts-custom-class-test",
    license="MIT",
    packages=get_packages("nuts_custom_class"),
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.6,<3.9",
)