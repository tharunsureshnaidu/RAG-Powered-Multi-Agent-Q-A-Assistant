from langchain.vectorstores import FAISS
# from langchain.embeddings.openai import OpenAIEmbeddings
import pickle
from langchain.embeddings import HuggingFaceEmbeddings 

# Load FAISS index
with open("vector_store.pkl", "rb") as f:
    vectorstore = pickle.load(f)

def retrieve_chunks(query):
    results = vectorstore.similarity_search(query, k=3)
    return [res.page_content for res in results]
