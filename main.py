import os
import argparse

from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None:
        raise RuntimeError("No API key!")
    
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("prompt", type=str, help="User prompt")
    args = parser.parse_args()

    prompt = args.prompt

    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=prompt
    )

    if response.usage_metadata == None:
        raise RuntimeError("Failed API request!")
    
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n{response.text}")

if __name__ == "__main__":
    main()
