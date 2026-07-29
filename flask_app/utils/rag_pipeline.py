"""
rag_pipeline.py

Processes all uploaded PDFs and creates a single FAISS vector database.
"""

import os

from utils.pdf_loader import extract_text
from utils.text_splitter import split_text
from utils.embeddings import get_embedding_model
from utils.vector_store import create_vector_store, save_vector_store


def process_pdf(upload_folder, vector_db_path):
    """
    Process every PDF inside the upload folder.

    Args:
        upload_folder (str): Folder containing uploaded PDFs.
        vector_db_path (str): Folder where the FAISS index is stored.

    Returns:
        dict: Processing summary.
    """

    all_text = ""
    pdf_count = 0

    print("\n========== PROCESSING PDFs ==========")

    for filename in os.listdir(upload_folder):

        if filename.lower().endswith(".pdf"):

            pdf_path = os.path.join(upload_folder, filename)

            print(f"Reading: {filename}")

            text = extract_text(pdf_path)

            if text.strip():

                all_text += "\n\n" + text
                pdf_count += 1

    if pdf_count == 0:
        #  Remove old vector database if it exists
        if os.path.exists(vector_db_path):
            
            import shutil
            shutil.rmtree(vector_db_path)
        
        return{
            "status": "empty",
            "pdfs": 0,
            "chunks": 0,
            "message": "No PDF documents available"
        }

    print(f"\nTotal PDFs processed : {pdf_count}")

    print("Splitting text...")
    chunks = split_text(all_text)

    print(f"Total Chunks : {len(chunks)}")

    print("Loading embedding model...")
    embedding_model = get_embedding_model()

    print("Creating vector database...")
    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    print("Saving vector database...")
    save_vector_store(
        vector_store,
        vector_db_path
    )

    print("========== DONE ==========\n")

    return {
        "status": "success",
        "pdfs": pdf_count,
        "chunks": len(chunks),
        "message": f"{pdf_count} PDF(s) indexed successfully!"
    }