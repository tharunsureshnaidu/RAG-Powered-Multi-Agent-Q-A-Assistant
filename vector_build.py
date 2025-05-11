from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import pickle
import os
from langchain.embeddings import HuggingFaceEmbeddings 

# Load and chunk docs
docs = []
for file in os.listdir("."):
    if file.endswith(".txt"):
        loader = TextLoader(f"{file}",encoding="utf-8")
        docs.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Build vector store
# embeddings = OpenAIEmbeddings()
embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2") 
vectorstore = FAISS.from_documents(chunks, embeddings)

with open("vector_store.pkl", "wb") as f:
    pickle.dump(vectorstore, f)

print("Vector store created.")