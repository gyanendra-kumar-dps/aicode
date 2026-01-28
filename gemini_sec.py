from google import genai
from google.genai import types
from config import gemini_api_key
import os
import time
def generate_response(prompt, temperature=0.5):
    try:
        client = genai.Client(api_key=gemini_api_key)
        contents = [types.Content(role="user",parts=[types.Part.from_text(text=prompt)],),]
        generate_content_config = types.GenerateContentConfig(temperature=temperature,response_mime_type="text/plain",)
        response = client.models.generate_content(model="gemini-2.0-flash-lite",contents=contents,config=generate_content_config,)
        for chunk in client.models.generate_content_stream(
        model="gemini-2.0-flash",
        contents=contents,
        config=generate_content_config,
        ):
            print(chunk.text, end="")
        return response.text
    except Exception as e:
        return f"error generating response:{str(e)}"
def temperature_prompt_activity():
    base_prompt = input("\nEnter a creative prompt (e.g., 'Write a short story about a robot learning to paint'): ")
    low_temp_response = generate_response(base_prompt, temperature=0.1)
    print(low_temp_response)
    print("\n--- MEDIUM TEMPERATURE (0.5) - Balanced ---")
    medium_temp_response = generate_response(base_prompt, temperature=0.5)
    print(medium_temp_response)
    time.sleep(1)
    print("\n--- HIGH TEMPERATURE (0.9) - More Random/Creative ---")
    high_temp_response = generate_response(base_prompt, temperature=0.9)
    topic = input("\nChoose a topic (e.g., 'climate change', 'space exploration'): ")
    instructions = [
        f"Summarize the key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I'm a 10-year-old child.",
        f"Write a pro/con list about {topic}.",
        f"Create a fictional news headline from the year 2050 about {topic}."
    ]
    for i, instruction in enumerate(instructions, 1):
        print(f"\n--- INSTRUCTION {i}: {instruction} ---")
        response = generate_response(instruction, temperature=0.7)
        print(response)
        time.sleep(1)
    custom_instruction = input("\nEnter your instruction-based prompt: ")
    try:
        custom_temp = float(input("\nSet a temperature (0.1 to 1.0): "))
        if custom_temp < 0.1 or custom_temp > 1.0:
            print("Invalid temperature. Using default 0.7.")
            custom_temp = 0.7
    except ValueError:
        print("Invalid input. Using default temperature 0.7.")
        custom_temp = 0.7
    custom_response = generate_response(custom_instruction, temperature=custom_temp)
if __name__ == "__main__":
    temperature_prompt_activity()
    choice = input("> ").lower().strip()
    if choice == 'y':
        prompt = input("\nEnter a prompt for streaming response: ")
        generate_response(prompt, temperature=0.7)