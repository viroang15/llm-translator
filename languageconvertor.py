from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["openai"]["api_key"])

def translate(text: str, model = "gpt-4o-mini"):
    system = "You are a professional translator. Translate any user text from English to German. Answer with German only"
    response = client.chat.completions.create(
        model = model,
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": text}
        ]
    )
    content = response.choices[0].message.content
    if content is None:
        raise RuntimeError("API returned no content—see the raw response above.")
    return content.strip()

