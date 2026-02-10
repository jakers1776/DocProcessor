# Document Processor with Ollama

A Python tool that extracts text from documents (.docx, .pdf, .txt) and generates AI-powered summaries using Ollama.

## Features

- 📄 Extract text from multiple document formats (.docx, .pdf, .txt)
- 🤖 AI-powered summarization using Ollama
- 💾 Automatic output file naming (`filename_text.txt`, `filename_summary.txt`)
- 📦 Batch processing support
- 🔧 Customizable LLM models

## Prerequisites

- Python 3.7+
- [Ollama](https://ollama.ai) installed and running
- At least one Ollama model pulled (e.g., `llama2`, `mistral`, `llama3`)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jakers1776/document-processor-ollama.git
cd document-processor-ollama
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

3. Install and start Ollama:
```bash
# Visit https://ollama.ai for installation instructions
# Then pull a model:
ollama pull llama2
```

## Usage

### Command Line

Process a single document:
```bash
python process_docs.py path/to/document.pdf
```

Process multiple documents:
```bash
python process_docs.py doc1.docx doc2.pdf doc3.txt
```

Specify a different Ollama model:
```bash
python process_docs.py document.pdf --model mistral
```

### As a Python Module

```python
from document_processor import process_document, process_multiple_documents

# Single file
process_document("example.pdf", model='llama2')

# Multiple files
files = ["doc1.docx", "doc2.pdf", "doc3.txt"]
results = process_multiple_documents(files, model='llama2')
```

## Output

For each input file, the tool creates two output files:

- `{filename}_text.txt` - Extracted text content
- `{filename}_summary.txt` - AI-generated summary

Example:
```
Input: quarterly_report.pdf
Output: 
  - quarterly_report_text.txt
  - quarterly_report_summary.txt
```

## Supported File Types

- `.docx` - Microsoft Word documents
- `.pdf` - PDF documents
- `.txt` - Plain text files

## Configuration

Edit the summarization prompt in `document_processor.py` to customize summary style:

```python
def summarize_with_ollama(text, model='llama2'):
    prompt = f"Your custom prompt here: {text}"
    # ...
```

## Available Ollama Models

Popular models you can use:
- `llama2` (default)
- `llama3`
- `mistral`
- `mixtral`
- `phi`

View all available models: `ollama list`

## Troubleshooting

**"Ollama connection error"**
- Ensure Ollama is running: `ollama serve`
- Check that you have a model installed: `ollama list`

**"Unsupported file type"**
- Verify file extension is .docx, .pdf, or .txt
- Check that the file is not corrupted

**"Memory error with large PDFs"**
- Try processing smaller documents
- Use a more efficient model like `mistral`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Acknowledgments

- [Ollama](https://ollama.ai) for local LLM inference
- [python-docx](https://python-docx.readthedocs.io/) for Word document processing
- [PyPDF2](https://pypdf2.readthedocs.io/) for PDF processing
