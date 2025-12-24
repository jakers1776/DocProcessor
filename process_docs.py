#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from document_processor import process_document, process_multiple_documents


def main():
    parser = argparse.ArgumentParser(
        description='Extract text and generate summaries from documents using Ollama'
    )
    parser.add_argument(
        'files',
        nargs='+',
        help='One or more document files to process (.docx, .pdf, .txt)'
    )
    parser.add_argument(
        '--model',
        '-m',
        default='llama2',
        help='Ollama model to use for summarization (default: llama2)'
    )
    
    args = parser.parse_args()
    
    # Verify files exist
    valid_files = []
    for file_path in args.files:
        path = Path(file_path)
        if not path.exists():
            print(f"Warning: File not found: {file_path}", file=sys.stderr)
        else:
            valid_files.append(file_path)
    
    if not valid_files:
        print("Error: No valid files to process", file=sys.stderr)
        sys.exit(1)
    
    # Process documents
    print(f"Processing {len(valid_files)} document(s) with model: {args.model}\n")
    results = process_multiple_documents(valid_files, model=args.model)
    
    # Print summary
    print("\n" + "="*50)
    print("PROCESSING COMPLETE")
    print("="*50)
    
    successful = sum(1 for r in results if r['status'] == 'success')
    failed = len(results) - successful
    
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    
    if failed > 0:
        print("\nFailed files:")
        for r in results:
            if r['status'] == 'failed':
                print(f"  - {r['original']}: {r['error']}")


if __name__ == "__main__":
    main()