# app/main.py
from fastapi import FastAPI
from .models import UserInput
from .zodiac import get_zodiac_sign
from .llm_free import generate_insight
# from .translator import translate_to_hindi
from .cache import get_cache, set_cache

app = FastAPI(title="Free Astrological Insight Generator")

@app.post("/insight")
async def get_astrological_insight(data: UserInput):
    zodiac = get_zodiac_sign(data.birth_date)
    key = f"{data.name}-{zodiac}-{data.birth_date}-{data.language}"

    if data.use_cache:
        cached = get_cache(key)
        if cached:
            return cached

    insight = generate_insight(data.name, zodiac, data.birth_place or "")

    # if data.language.lower() == "hi":
    #     insight = translate_to_hindi(insight)

    result = {
        "zodiac": zodiac,
        "insight": insight,
        "language": data.language
    }

    if data.use_cache:
        set_cache(key, result)

    return result
