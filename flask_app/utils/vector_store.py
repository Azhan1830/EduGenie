"""
vector_store.py

Creates and saves the FAISS vector database.
"""

import os

from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embedding_model):
    """
    Creates a FAISS vector store from text chunks.

    Args:
        chunks (list): List of text chunks.
        embedding_model: HuggingFace embedding model.

    Returns:
        FAISS vector store.
    """

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model
    )

    return vector_store


def save_vector_store(vector_store, save_path):
    """
    Saves the FAISS vector store to disk.

    Args:
        vector_store: FAISS vector store.
        save_path (str): Directory where the index will be stored.
    """

    os.makedirs(save_path, exist_ok=True)

    vector_store.save_local(save_path)