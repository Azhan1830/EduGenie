"""
llm.py

Handles communication with the Gemini model.
"""

import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_gemini_client():
    """
    Creates and returns the Gemini client.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not found.")

    client = genai.Client(api_key=api_key)

    return client


def generate_answer(context, question):
    """
    Generates an answer using Gemini.
    """

    client = get_gemini_client()

    prompt = f"""
You are an AI assistant that answers questions ONLY from the given context.

If the answer is not present in the context, reply:
"I could not find the answer in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    return response.text