import google.generativeai as genai

def configure_model():
    genai.configure(api_key="GEMINI_API_KEY")
    return genai.GenerativeModel('gemini-pro'), genai.GenerativeModel('gemini-pro-vision')

generative_text_model, generative_image_model = configure_model()

def generate_text(query: str):
    response = generative_text_model.generate_content(query)
    return {"text": response.text}

def generate_image(query: str, img_data: bytes):
    response = generative_image_model.generate_content([query, {"mime_type": "image/jpeg", "data": img_data}], stream=True)
    return {"image": response.text}
