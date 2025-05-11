# RAG-Powered-Multi-Agent-Q-A-Assistant

This project implements a basic knowledge assistant that uses Retrieval-Augmented Generation (RAG) and a simple agentic workflow to answer user questions from a small collection of documents. It supports branching logic for calculations and definitions using tool-based agents.

# Architecture

1. Data Ingestion

Ingested 1 short documents (we can ingest multiple documenst

2. Vector Store & Retrieval

Used FAISS for vector indexing.

Embedded chunks using HuggingFace Embedding (all-mpnet-base-v2).

Retrieved top 3 relevant chunks based on cosine similarity to the query.

3. LLM Integration

Connected to an LLM (e.g., OpenAI GPT-3.5) for answer generation using context retrieved from the vector store.
here i have use GROQ API key and used "deepseek-r1-distill-llama-70b"

4. Agentic Workflow

Built with LangChain's agent tools and custom routing logic.

Query keywords like “calculate” or “define” are routed to:

A calculator tool (via LLMathChain) or

A dictionary tool (mocked via WordNet or static dict API).

All other queries follow the RAG → LLM pipeline.

Each decision step is logged and shown in the output.

5. Demo Interface

Built a Streamlit interface where users can:

Enter questions

View the selected agent/tool

See retrieved context

Get final answers

 How to Run
 Setup
Clone the repo

Install dependencies:


 Run

streamlit run app.py
 Example Query Flow
Query: “What is the warranty period?”
→ RAG Path → LLM answers using document chunks.

Query: “Calculate 15% of 2300”
→ Routed to Calculator Tool.

Query: “Define scalability”
→ Routed to Dictionary Tool.
