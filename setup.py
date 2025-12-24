from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="document-processor-ollama",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Extract text and generate summaries from documents using Ollama",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/document-processor-ollama",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "python-docx>=0.8.11",
        "PyPDF2>=3.0.0",
        "ollama>=0.1.0",
    ],
    entry_points={
        "console_scripts": [
            "process-docs=process_docs:main",
        ],
    },
)
