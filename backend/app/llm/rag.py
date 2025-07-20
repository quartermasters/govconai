import faiss
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Dict

class RAGSystem:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.index = None
        self.documents = []

    def add_documents(self, documents: List[Dict]):
        # documents are expected to be a list of dictionaries with 'content' and 'chunk_id'
        self.documents.extend(documents)
        corpus = [doc['content'] for doc in documents]
        if corpus:
            embeddings = self.vectorizer.fit_transform(corpus).toarray()
            if self.index is None:
                self.index = faiss.IndexFlatL2(embeddings.shape[1])
            self.index.add(embeddings)

    def search(self, query: str, k: int = 5) -> List[Dict]:
        if self.index is None:
            return []
        query_embedding = self.vectorizer.transform([query]).toarray()
        D, I = self.index.search(query_embedding, k)  # D is distances, I is indices
        results = []
        for i in I[0]:
            if i != -1:  # Check if a valid index is returned
                results.append(self.documents[i])
        return results

# Example Usage (for testing purposes)
if __name__ == "__main__":
    rag_system = RAGSystem()
    rag_system.add_documents([
        {"chunk_id": "chunk1", "content": "The quick brown fox jumps over the lazy dog."},
        {"chunk_id": "chunk2", "content": "Never jump over a lazy dog quickly."},
        {"chunk_id": "chunk3", "content": "A brown fox is quick."}
    ])

    query = "quick fox"
    results = rag_system.search(query, k=2)
    print(f"Query: {query}")
    for res in results:
        print(f"  - Chunk ID: {res['chunk_id']}, Content: {res['content']}")