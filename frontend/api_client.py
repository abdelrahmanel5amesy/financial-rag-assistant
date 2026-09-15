import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

def query_financial_assistant(question: str):
    url = f"{BASE_URL}/query"
    try:
        response = requests.post(url, json={"question": question}, timeout=60)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API returned status {response.status_code}: {response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Could not connect to backend at {BASE_URL}. Ensure the server is running."}