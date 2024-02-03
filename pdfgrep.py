#!/usr/bin/env python
import sys
import PyPDF2
import re

def pdfgrep(pattern, pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_number in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_number)
            text = page.extract_text()

            lines = text.split('\n')
            for line_number, line in enumerate(lines, start=1):
                matches = re.finditer(pattern, line, re.IGNORECASE)
                for match in matches:
                    print(f"Page {page_number + 1}, Line {line_number}, Match: '{line}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <pattern> <pdf_file>")
        sys.exit(1)

    pattern_to_search = sys.argv[1]
    pdf_file_path = sys.argv[2]

    pdfgrep(pattern_to_search, pdf_file_path)

