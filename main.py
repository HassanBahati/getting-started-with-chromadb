import chromadb
import uuid

# client = chromadb.Client()
# client = chromadb.PersistentClient(path="./chroma_data")
client = chromadb.HttpClient(host="localhost", port="8000")

# collection = client.create_collection(name="policies")
collection = client.get_or_create_collection(name="policies")

with open("policies.txt", "r", encoding="utf-8") as file:
    policies: list[str] = file.readlines()


# collection.add(
#     ids=[str(uuid.uuid4()) for _ in policies],
#     documents=policies,
#     metadatas=[{"line": line} for line in range(len(policies))]
# )


# print(collection.peek())

results = collection.query(
    query_texts=["What is the damaged items policy?"],
    n_results=5
)


for i, query_results in enumerate(results["documents"]):
    print(f"\nQuery {i}:")
    print("\n".join(query_results))

print(results)