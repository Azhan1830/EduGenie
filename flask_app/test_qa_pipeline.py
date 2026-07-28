import os

from utils.qa_pipeline import answer_question

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VECTOR_DB = os.path.join(BASE_DIR, "vector_db")

question = "What is the offered salary?"

result = answer_question(
    question=question,
    vector_db_path=VECTOR_DB
)

print("\n" + "=" * 60)
print("ANSWER")
print("=" * 60)
print(result["answer"])

print("\n" + "=" * 60)
print("RETRIEVED CONTEXT")
print("=" * 60)
print(result["context"])