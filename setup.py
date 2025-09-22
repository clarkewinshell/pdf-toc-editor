# setup.py

from setuptools import setup, find_packages

setup(
    name="pdf-toc-editor",
    version="0.1.0",
    description="A simple PDF Table of Contents editor built with PyQt5 and PyMuPDF",
    author="clarkewinshell",
    author_email="",
    url="https://github.com/yourusername/pdf-toc-editor",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyQt5>=5.15",
        "PyMuPDF>=1.23"
    ],
    entry_points={
        "console_scripts": [
            "pdf-toc-editor=app.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)
