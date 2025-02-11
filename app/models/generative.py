import os
import google.generativeai as genai
from google.generativeai.types import GenerateContentConfig

# Load configuration from environment variables
api_key = os.getenv("GEMINI_API_KEY", "your_default_api_key")
text_model_name = os.getenv("TEXT_MODEL_NAME", "gemini-2.0-flash")
image_model_name = os.getenv("IMAGE_MODEL_NAME", "gemini-2.0-flash")
system_prompt = os.getenv("SYSTEM_PROMPT", "")  # Optional system instruction
temperature = float(os.getenv("TEMPERATURE", "0.7"))
max_output_tokens = int(os.getenv("MAX_OUTPUT_TOKENS", "1000"))

def configure_model():
    genai.configure(api_key=api_key)
    text_model = genai.GenerativeModel(text_model_name)
    image_model = genai.GenerativeModel(image_model_name)
    return text_model, image_model

generative_text_model, generative_image_model = configure_model()

def generate_text(query: str):
    config = GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )
    response = generative_text_model.generate_content(query, config=config)
    return {"text": response.text}

def generate_image(query: str, img_data: bytes):
    config = GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )
    combined_query = [query, {"mime_type": "image/jpeg", "data": img_data}]
    response = generative_image_model.generate_content(combined_query, config=config, stream=True)
    return {"image": response.text}
