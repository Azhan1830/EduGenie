"""
qa_pipeline.py
Combines Retrieval + Gemini
"""
from utils.reteriver import retrieve_chunks
from utils.llm import generate_answer

MIN_CONTEXT_LENGTH = 50

def answer_question(question, vector_db_path):
    """
    Retrieves relevant chunks and generates an answer.
    """

    docs = retrieve_chunks(
        question=question,
        vector_db_path=vector_db_path
    )

    # No chunks retrieved
    if not docs:
        return {
            "answer": (
                "I couldn't find this information in the uploaded documents."
            ),
            "context": "",
            "sources": []
        }

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    ).strip()

    # Retrieved context is too small to be useful
    if len(context) < MIN_CONTEXT_LENGTH:
        return {
            "answer": (
                "I couldn't find enough relevant information in the uploaded documents "
                "to answer your question."
            ),
            "context": context,
            "sources": docs
        }

    answer = generate_answer(
        context=context,
        question=question
    )

    return {
        "answer": answer,
        "context": context,
        "sources": docs
    }