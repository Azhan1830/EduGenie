"""
retriever.py
Loads the FAISS vector database and retrieves
relevant chunks for a given question.
"""

from langchain_community.vectorstores import FAISS

from utils.embeddings import get_embedding_model

def load_vector_store(vector_db_path):
    """
    Loads the saved FAISS vector database.
    """
    embedding_model = get_embedding_model()

    vector_store = FAISS.load_local(
        vector_db_path,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store

def retrieve_chunks(question, vector_db_path, k=3):
    """
    Retrieves the most relevant chunks.

    Args:
        question (str)
        vector_db_path (str)
        k (int)

    Returns:
        list
    """
    vector_store = load_vector_store(vector_db_path)

    docs = vector_store.similarity_search(
        question,
        k=k
    )

    return docs