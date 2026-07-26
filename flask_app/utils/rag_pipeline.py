"""
rag_pipeline.py

Main pipeline for processing PDFs.
"""

from utils.pdf_loader import extract_text
from utils.text_splitter import split_text
from utils.embeddings import get_embedding_model
from utils.vector_store import create_vector_store, save_vector_store


def process_pdf(pdf_path, vector_db_path):
    """
    Complete RAG pipeline.

    Args:
        pdf_path (str): Path to uploaded PDF.
        vector_db_path (str): Folder to save FAISS index.

    Returns:
        dict: Processing summary.
    """

    print("Extracting text...")
    text = extract_text(pdf_path)

    print("Splitting text...")
    chunks = split_text(text)

    print("Loading embedding model...")
    embedding_model = get_embedding_model()

    print("Creating vector store...")
    vector_store = create_vector_store(chunks, embedding_model)

    print("Saving vector store...")
    save_vector_store(vector_store, vector_db_path)

    return {
        "status": "success",
        "chunks": len(chunks),
        "message": "Vector database created successfully!"
    }