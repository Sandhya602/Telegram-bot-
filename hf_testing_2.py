import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def generate_response(prompt: str) -> str:
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        result = response.json()
        return result[0]['generated_text']
    except Exception as e:
        return "Error generating response. Please try again later."
      
