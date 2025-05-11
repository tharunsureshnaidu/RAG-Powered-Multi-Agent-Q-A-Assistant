from retriever import retrieve_chunks
from llm_chain import ask_llm
from tools import calculator_tool, dictionary_tool

def route_query(query):
    q_lower = query.lower()
    if any(k in q_lower for k in ["calculate", "compute"]):
        decision = "Calculator Tool"
        return decision, [], calculator_tool(query)
    elif any(k in q_lower for k in ["define", "meaning of"]):
        decision = "Dictionary Tool"
        return decision, [], dictionary_tool(query)
    else:
        decision = "RAG Pipeline"
        context = retrieve_chunks(query)
        answer = ask_llm(query, context)
        return decision, context, answer