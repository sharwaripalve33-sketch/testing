import requests
import json

def ask_gemma(notes):
    prompt = f"""
You are a study assistant.
Read these notes and create 3 short quiz questions.

Notes:
{notes}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma4:e2b",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    return data["response"]

if __name__ == "__main__":
    with open("notes.txt", "r", encoding="utf-8") as file:
        notes = file.read()

    print("Generating quiz questions...\n")
    print(ask_gemma(notes))