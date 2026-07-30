"""
pdf_loader.py
Handles reading PDF files and extracting text.
"""
from pypdf import PdfReader

def load_pdf(file_path):
    """
    Loads a PDF and returns the PdfReader object.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        PdfReader
    """

    return PdfReader(file_path)

def extract_text(file_path):
    """
    Extracts text from all pages of a PDF.

    Args:
        file_path (str): Path to the PDF.

    Returns:
        str: Complete extracted text.
    """

    reader = load_pdf(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

    return text