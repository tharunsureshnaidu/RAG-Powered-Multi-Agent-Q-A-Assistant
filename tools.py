def calculator_tool(query):
    try:
        return str(eval(query.split("calculate")[-1].strip()))
    except:
        return "Error: Could not compute."

def dictionary_tool(query):
    definitions = {
        "rag": "Retrieval-Augmented Generation, a technique combining search and generation.",
        "llm": "Large Language Model, a deep learning model trained on vast text data.",
    }
    for word in definitions:
        if word in query.lower():
            return definitions[word]
    return "Definition not found."