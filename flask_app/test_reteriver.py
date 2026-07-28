from utils.reteriver import retrieve_chunks

question = "What is the offer letter about?"

docs = retrieve_chunks(
    question=question,
    vector_db_path="vector_db"
)

print("=" * 50)

print(f"Retrieved {len(docs)} Chunks")

print("=" * 50)

for i, doc in enumerate(docs, start=1):

    print(f"\nChunk {i}\n")

    print(doc.page_content)

    print("-" * 80)