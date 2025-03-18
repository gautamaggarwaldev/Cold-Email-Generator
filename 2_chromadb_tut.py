import chromadb

client = chromadb.Client()
collection = client.create_collection("my_collection")
collection.add(
    documents = [
        "This document is about new york",
        "This document is about new new delhi",
    ],
    ids = ["id1","id2"],
    metadatas=[
        {"url": "https://en.wikipedia.org/wiki/New_York_City"},
        {"url": "https://en.wikipedia.org/wiki/New_Delhi"}
    ]
)

all_docs = collection.get()
documents = collection.get(ids=["id1"])
# print(all_docs)
# print(documents)

result = collection.query(
    query_texts=['Query is about India Gate.'],
    n_results=2
)

print(result)