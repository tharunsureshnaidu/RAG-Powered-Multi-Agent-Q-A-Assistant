import streamlit as st
from agents import route_query

st.title("🧠 Multi-Agent Knowledge Assistant")
query = st.text_input("Ask a question:")

if query:
    decision, context, answer = route_query(query)
    
    st.markdown(f"**Agent decision:** `{decision}`")
    st.markdown("**Retrieved context:**")
    for i, chunk in enumerate(context):
        st.markdown(f"`Chunk {i+1}`: {chunk[:300]}...")
    
    st.markdown("**Final Answer:**")
    st.write(answer)