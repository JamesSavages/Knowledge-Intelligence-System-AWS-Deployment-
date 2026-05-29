import chromadb 
from langchain.schema import document
from langchain.vectorstores import Chroma, chroma
from langchain.embeddings.openai import OpenAIEmbeddings

class VectorStore:
    def __init__(self, path):
        self.embeddings = OpenAIEmbeddings()
        self.vectir_store = Chroma(
            persist_directory= path,
            embedding_function=self.embeddings
        )

    def add_documents(self, documents):
        self.vectir_store.add_documents(documents)

    def similarity_search(self, query, k=4):
        return self.vectir_store.similarity_search(query=query, k=k)

