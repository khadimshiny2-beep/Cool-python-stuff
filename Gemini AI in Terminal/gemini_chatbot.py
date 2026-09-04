from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

while True:
    question = input("--You--: ")

    if question.lower() == "exit": break

    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents=question
        )

    print("'-_Gemini_-': ", response.text)