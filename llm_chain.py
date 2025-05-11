from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import os

llm = ChatGroq(groq_api_key="API kEY", model_name="deepseek-r1-distill-llama-70b")

prompt = PromptTemplate.from_template("""
Use the following context to answer the question:

{context}

Question: {question}
Answer:
""")
print("llm is workign fine")
print(llm.invoke("what is aiml"))
def ask_llm(question, context):
    combined_context = "\n".join(context)
    return llm.predict(prompt.format(context=combined_context, question=question))