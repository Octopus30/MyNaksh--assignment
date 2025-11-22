# app/llm_free.py
from transformers import pipeline

# Load once at startup
generator = pipeline("text-generation", model="google/flan-t5-small", device=-1)  # device=0 for GPU

def generate_insight(name: str, zodiac: str, birth_place: str = "") -> str:
    prompt = f"Give ONE sentence daily astrology insight for {name}, zodiac sign {zodiac}, birth place {birth_place}."
    output = generator(prompt, max_new_tokens=60, do_sample=True, temperature=0.8)
    return output[0]['generated_text'].strip()

