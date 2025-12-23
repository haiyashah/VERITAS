from openai import OpenAI

client = OpenAI()

def call_llm(prompt, temperature=0.2):
    """
    Call the LLM (GPT-4o-mini) with a prompt.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content
