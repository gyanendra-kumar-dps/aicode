from openai import OpenAI
from config import groq,huggingface
from huggingface_hub import InferenceClient
base_url="https://api.groq.com/openai/v1"
key=groq
GROQ_URL = "https://api.groq.com/openai/v1"
MODELS1 = getattr(groq, "GROQ_MODELS", ["llama-3.1-8b-instant", "mixtral-8x7b-32768"])
MODELS2 = getattr(huggingface, "HF_MODELS", ["meta-llama/Llama-3.1-8B-Instruct"])
def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
    c = OpenAI(api_key=key, base_url=GROQ_URL)
    r = c.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}],
    temperature=temperature,
    max_tokens=max_tokens,)
    return r.choices[0].message.content
def reinforcement_learning_activity(initial_response):
    try:
        rating = int(input("Rate the response from 1 (bad) to 5 (good): ").strip())
        if rating < 1 or rating > 5:
            rating = 3
    except ValueError:
        rating = 3
    feedback = input("Provide feedback for improvement: ").strip()
    improved_response = f"{initial_response} (Improved with your feedback: {feedback})"
    return generate_response(improved_response)
def role_based_prompt_activity(category,item):
    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."
    json_prompt="You give answer in json like User:Turn on lights Model:{lights:on},Now your turn User:"+category
    return generate_response(json_prompt)
def run_activity(choice):
    print("Choose an activity:")
    if choice == "1":
        inp1=input("Enter instruction:")
        print(reinforcement_learning_activity(inp1))
    elif choice == "2":
        inp1=input("Enter category:")
        inp2=input("Enter item:")
        print(role_based_prompt_activity(inp1,inp2))
    else:
        print("Invalid choice. Please choose 1 or 2.")
def generate_h_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
    key = huggingface
    if not key:
        return "Error: HF_API_KEY missing in config.py"
    c = InferenceClient(model="meta-llama/Llama-3.1-8B-Instruct", token=key)
    r = c.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return r.choices[0].message.content
if __name__ == "__main__":
    inp=input("Enter choice:")
    run_activity(inp)