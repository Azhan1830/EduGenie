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
You are EduGenie, an AI assistant that answers questions using ONLY the information found in the uploaded PDF documents.

Your responsibilities:

1. Answer ONLY from the provided context.
2. Do NOT use outside knowledge.
3. Do NOT guess or invent information.
4. If the answer cannot be found in the context, reply exactly:

"I couldn't find this information in the uploaded documents."

5. Keep answers:
   - Clear
   - Accurate
   - Well-structured
6. Use bullet points whenever appropriate.
7. For definitions, begin with a short definition followed by a brief explanation.
8. For comparisons, present the answer in a clear comparison format.
9. If the question requests steps or a process, answer using numbered steps.
10. Avoid mentioning that you are an AI model.

-------------------------
DOCUMENT CONTEXT
-------------------------
{context}

-------------------------
USER QUESTION
-------------------------
{question}

-------------------------
ANSWER
-------------------------
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    return response.text