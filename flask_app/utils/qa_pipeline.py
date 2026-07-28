"""
qa_pipeline.py

Combines Retrieval + Gemini
"""

from utils.reteriver import retrieve_chunks
from utils.llm import generate_answer


def answer_question(question, vector_db_path):
    """
    Retrieves relevant chunks and generates an answer.
    """

    docs = retrieve_chunks(
        question=question,
        vector_db_path=vector_db_path
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    answer = generate_answer(
        context=context,
        question=question
    )

    return {
        "answer": answer,
        "context": context,
        "sources": docs
    }