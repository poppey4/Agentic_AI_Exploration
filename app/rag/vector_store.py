import chromadb

client = chromadb.Client()

collection = client.create_collection(name="enterprise_docs")


def store_embeddings(documents, embeddings):
    for idx, embedding in enumerate(embeddings):
        collection.add(
            ids=[str(idx)],
            documents=[documents[idx]],
            embeddings=[embedding.tolist()]
        )