def load_docs(path):
    """
    Load all documents as a single string.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def retrieve_context(question, docs):
    """
    Naive retrieval: return first 1500 chars for context.
    """
    return docs[:1500]
