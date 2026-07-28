import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

models_to_try = [
    "gemini-flash-latest",
    "gemini-3.5-flash",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
]

for model in models_to_try:
    print(f"\nTesting {model}...")

    try:
        response = client.models.generate_content(
            model=model,
            contents="Say Hello"
        )
        print("✅ SUCCESS")
        print(response.text)
    except Exception as e:
        print("❌ FAILED")
        print(e)