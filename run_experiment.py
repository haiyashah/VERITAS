from core.adapter import call_llm
from core.probe_generator import generate_probes
from core.consistency import consistency_score
from retrieval.simple_rag import load_docs, retrieve_context

QUESTION = "Can EU customer data be stored on US servers?"

def baseline_run(question, context):
    """
    Simple baseline: LLM answer without probes or adaptation.
    """
    answer = call_llm(question + "\nContext:\n" + context)
    return answer

def veritas_run(question, context):
    """
    Run the VERITAS system:
    1. Generate probes
    2. Run LLM on each probe
    3. Measure consistency
    4. Produce final adapted answer
    """
    probes = generate_probes(question)
    probe_answers = [call_llm(p + "\nContext:\n" + context) for p in probes]

    consistency = consistency_score(probe_answers)

    final_prompt = f"""
    Original question: {question}

    Consider the following reasoning checks:
    {probe_answers}

    Provide a final, careful answer.
    """
    final_answer = call_llm(final_prompt)

    return probes, probe_answers, consistency, final_answer

if __name__ == "__main__":
    docs = load_docs("data/gdpr_docs.txt")
    context = retrieve_context(QUESTION, docs)

    print("\n=== BASELINE ===")
    baseline_answer = baseline_run(QUESTION, context)
    print(baseline_answer)

    print("\n=== VERITAS ===")
    probes, probe_answers, consistency, final_answer = veritas_run(QUESTION, context)

    print("\nProbes:")
    for p in probes:
        print("-", p)

    print("\nProbe Answers:")
    for pa in probe_answers:
        print("-", pa)

    print("\nConsistency score:", consistency)

    print("\nFinal Answer:")
    print(final_answer)
