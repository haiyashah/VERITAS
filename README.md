# VERITAS

---

To try it out, download and run: ``` python run_experiment.py ```

---

VERITAS: Verified Enterprise Reasoning via Iterative Test-time Adaptation with Synthetic Signals

This is not a chatbot.
This is a new training + inference paradigm.

Goals:
- Domain adaptation
- Synthetic data
- Evaluation at scale
- Retrieval augmentation
- Efficient post-training
- Enterprise data behind closed doors

LLMs should adapt to a domain at inference time using self-generated tests, synthetic counterfactuals, and verifiable signals, without fine-tuning or labeled data.

Today:

- Fine-tuning is slow
- RAG is brittle
- Synthetic data is noisy
- Evaluation is manual and expensive

My idea:

A self-adapting LLM system that:

- Detects domain mismatch
- Generates synthetic probes
- Scores itself using latent consistency + retrieval agreement
- Updates its reasoning strategy during inference
- Leaves an audit trail (enterprise gold)

Architecture:
```
veritas/
├── run_experiment.py
├── requirements.txt
├── README.md
├── core/
│   ├── __init__.py
│   ├── adapter.py
│   ├── probe_generator.py
│   └── consistency.py
├── retrieval/
│   ├── __init__.py
│   └── simple_rag.py
├── metrics/
│   ├── __init__.py
│   └── scores.py
└── data/
    └── gdpr_docs.txt

```
