# create.py

import os

import openai

PROMPT = "cute pikachu eating mochi"

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)

print(response["data"][0]["url"])