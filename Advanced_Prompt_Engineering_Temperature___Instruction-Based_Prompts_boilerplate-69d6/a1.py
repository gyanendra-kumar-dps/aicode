# import os
# import time
# from google import genai
# from google.genai import types
# import config

# 2. DEFINE function generate_response(prompt, temperature=0.5):
#    - Initialize the genai client using the API key from config
#    - Create the content structure with the user's prompt
#    - Configure the response parameters (including temperature)
#    - Send the prompt to Gemini API to generate content
#    - Return the generated response text

# 3. DEFINE function temperature_prompt_activity():
#    - Print introductory information about the tutorial
    # print("=" * 80)
    # print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")
    # print("=" * 80)
    # print("\nIn this activity, we'll explore:")
    # print("1. How temperature affects AI creativity and randomness")
    # print("2. How instruction-based prompts can control AI outputs")
#    - Part 1: Temperature Exploration
    #         print("\n" + "-" * 40)
    # print("PART 1: TEMPERATURE EXPLORATION")
    # print("-" * 40)
#      - Get the user's creative prompt
#      - Generate AI responses with different temperatures (low, medium, high)
#      - Display the responses for each temperature setting
     
#    - Part 2: Instruction-Based Prompts
    # print("\n" + "-" * 40)
    # print("PART 2: INSTRUCTION-BASED PROMPTS")
    # print("-" * 40)
#      - Prompt the user for a topic (e.g., climate change, space exploration)
#      - Display different instruction-based prompts for that topic and generate responses
#      - Show the AI's output for each instruction-based prompt

#    - Part 3: Create Your Own Instruction-Based Prompts
    # print("\n" + "-" * 40)
    # print("PART 3: CREATING YOUR OWN INSTRUCTION-BASED PROMPTS")
    # print("-" * 40)
    
    # print("\nNow it's your turn! Create an instruction-based prompt and test it with different temperatures.")
#      - Allow the user to create their own custom instruction-based prompt
#      - Ask the user to set a temperature (0.1 to 1.0)
#      - Generate a response for the custom prompt and temperature
     
#    - Reflection Questions:
    # print("\n" + "-" * 40)
    # print("REFLECTION QUESTIONS")
    # print("-" * 40)
    # print("1. How did changing the temperature affect the creativity and variety in the AI's responses?")
    # print("2. Which instruction-based prompt produced the most useful or interesting result? Why?")
    # print("3. How might you combine specific instructions and temperature settings in real applications?")
    # print("4. What patterns did you notice in how the AI responds to different types of instructions?")

# #    - Challenge Activity:
#     print("\n" + "-" * 40)
#     print("CHALLENGE ACTIVITY")
#     print("-" * 40)
#     print("Try creating a 'chain' of prompts where:")
#     print("1. First, ask the AI to generate content about a topic")
#     print("2. Then, use an instruction-based prompt to modify or build upon that content")
#     print("3. Experiment with different temperature settings at each step")
#     print("\nFor example: Generate a story → Instruct AI to rewrite it in a specific style → Ask AI to create a sequel")

# 4. DEFINE function generate_streaming_response(prompt, temperature=0.5):
#    - Initialize the genai client
#    - Create the content structure with the user's prompt
#    - Configure the response parameters (including temperature)
#    - Generate content with streaming and print the output as it streams



# 6. IF __name__ == "__main__":
#    - Call temperature_prompt_activity() to run the tutorial
#    - Optional: Ask the user if they want to see streaming responses
#    - If the user agrees, prompt for a streaming response and generate it
