from .adapter import call_llm

def generate_probes(question, n=3):
    """
    Generate n factual sub-questions to test understanding of a domain.
    """
    prompt = f"""
    Generate {n} short factual sub-questions that test whether
    someone truly understands the domain behind this question:

    Question: {question}
    """
    raw = call_llm(prompt)
    probes = [p.strip("- ").strip() for p in raw.split("\n") if len(p) > 5]
    return probes[:n]
