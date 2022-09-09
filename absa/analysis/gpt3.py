import os
import openai
from textwrap import dedent

openai.api_key = os.getenv("OPENAI_API_KEY")

ABSA_PROMPT = dedent(
    f"""
    Please extract aspect expressions, related segments and related sentiments from the following text and format output in JSON:

    This product is good but the battery doesn't last. It's lightweight and very easy to use. Well worth the money.

    [
      {{ "aspect": "Overall satisfaction", "segment": "This product is good", "sentiment": "positive" }},
      {{ "aspect": "Battery", "segment": "the battery doesn't last", "sentiment": "negative" }},
      {{ "aspect": "Weight", "segment": "It's lightweight", "sentiment": "positive" }},
      {{ "aspect": "Usability", "segment": "very easy to use", "sentiment": "positive" }},
      {{ "aspect": "Value for money", "segment": "Well worth the money", "sentiment": "positive" }}
    ]

    I don't like this product, it's very noisy. Anyway, it's very cheap. The other one I had was better.

    [
      {{ "aspect": "Overall satisfaction", "segment": "I don't like this product", "sentiment": "negative" }},
      {{ "aspect": "Noise", "segment": "it's very noisy", "sentiment": "negative" }},
      {{ "aspect": "Price", "segment": "it's very cheap", "sentiment": "positive" }},
      {{ "aspect": "Comparison", "segment": "The other one I had was better.", "sentiment": "negative" }}
    ]
"""
)


def analyze(
    text,
    prompt_text=ABSA_PROMPT,
    extra_prompt="",
    temperature=0.5,
    max_tokens=128,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
):
    prompt = f"{prompt_text}\n{extra_prompt}\n{text}"

    return openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
