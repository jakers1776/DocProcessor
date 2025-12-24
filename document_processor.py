import os
from pathlib import Path
from docx import Document
import PyPDF2
import ollama


def extract_text_from_docx(file_path):
    '''Extract text from .docx files.'''
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\\n'.join(text)


def extract_text_from_pdf(file_path):
    '''Extract text from .pdf files.'''
    text = []
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text.append(page.extract_text())
    return '\\n'.join(text)


def extract_text_from_txt(file_path):
    '''Extract text from .txt files.'''
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def extract_text(file_path):
    '''Extract text based on file extension.'''
    extension = Path(file_path).suffix.lower()
    
    if extension == '.docx':
        return extract_text_from_docx(file_path)
    elif extension == '.pdf':
        return extract_text_from_pdf(file_path)
    elif extension == '.txt':
        return extract_text_from_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {extension}")


def summarize_with_ollama(text, model='llama2'):
    '''Generate summary using Ollama.'''
    prompt = f'''Please provide a concise summary of the following text. 
Focus on the main points and key information:

{text}

Summary:'''
    
    try:
        response = ollama.generate(model=model, prompt=prompt)
        return response['response']
    except Exception as e:
        raise Exception(f"Ollama error: {str(e)}. Make sure Ollama is running and the model '{model}' is available.")


def process_document(file_path, model='llama2'):
    '''Process a document: extract text and generate summary.'''
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Create output filenames
    base_name = file_path.stem
    output_dir = file_path.parent
    text_output = output_dir / f"{base_name}_text.txt"
    summary_output = output_dir / f"{base_name}_summary.txt"
    
    print(f"Processing: {file_path.name}")
    
    # Extract text
    print("  Extracting text...")
    text = extract_text(file_path)
    
    # Save extracted text
    with open(text_output, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"  ✓ Text saved to: {text_output.name}")
    
    # Generate summary
    print("  Generating summary with Ollama...")
    summary = summarize_with_ollama(text, model=model)
    
    # Save summary
    with open(summary_output, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"  ✓ Summary saved to: {summary_output.name}")
    
    return text_output, summary_output


def process_multiple_documents(file_paths, model='llama2'):
    '''Process multiple documents.'''
    results = []
    for file_path in file_paths:
        try:
            text_file, summary_file = process_document(file_path, model)
            results.append({
                'original': file_path,
                'text': text_file,
                'summary': summary_file,
                'status': 'success'
            })
        except Exception as e:
            print(f"  ✗ Error processing {file_path}: {str(e)}")
            results.append({
                'original': file_path,
                'status': 'failed',
                'error': str(e)
            })
    return results


if __name__ == "__main__":
    # Example usage
    print("Document Processor with Ollama")
    print("Please use process_docs.py for command-line usage")