import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import *

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None:
        raise RuntimeError("No API key!")
    
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("prompt", type=str, help="User prompt") 
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]
    prompt = args.prompt

    for _ in range(20):
        response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature=0)
        )

        if response.candidates != None:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if response.usage_metadata == None:
            raise RuntimeError("Failed API request!")
        
        if args.verbose is True:
            print(f"User prompt: {prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.function_calls != None:
            for function_call in response.function_calls:
                function_call_result = call_function(function_call)
                if function_call_result.parts == None:
                    raise Exception
                if function_call_result.parts[0].function_response == None:
                    raise Exception
                if function_call_result.parts[0].function_response.response == None:
                    raise Exception
                function_result_list = []
                function_result_list.append(function_call_result.parts[0])
            messages.append(types.Content(role="user", parts=function_result_list))
            if args.verbose is True:
                print(f"-> {function_call_result.parts[0].function_response.response["result"]}")    
        else:
            print(f"Response:\n{response.text}")
            return
       
if __name__ == "__main__":
    main()
