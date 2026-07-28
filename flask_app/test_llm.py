from utils.llm import generate_answer

context = """
The annual salary offered is ₹8,00,000.
The joining date is 1st August 2026.
"""

question = "What is the offered salary?"

answer = generate_answer(
    context=context,
    question=question
)

print("\nGemini Answer:\n")
print(answer)