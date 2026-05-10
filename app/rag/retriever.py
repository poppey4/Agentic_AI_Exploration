from app.rag.vector_store import collection


class RetrievalAgent:

    def retrieve(self, query_embedding):
        results = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=3
        )

        return results