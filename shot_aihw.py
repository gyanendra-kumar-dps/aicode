from config import groq,huggingface
isgroq=0
backend=input("Enter the backend to be used(groq,hf):")
if backend.lower()=='groq':
    isgroq=True
elif backend.lower()=='hf':
    isgroq=False
else:
    print("Error:give a correct backend")
    exit()
if isgroq:
    from openai import OpenAI
    groqurl="https://api.groq.com/openai/v1"
    models=["llama-3.1-8b-instant", "mixtral-8x7b-32768"]
    def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
        if not groq:
            return "Error: GROQ_API_KEY missing"
        client = OpenAI(api_key=groq, base_url=groqurl)
        last_err = None
        for m in models:
            try:
                r = client.chat.completions.create(model=m,messages=[{"role": "user", "content": prompt}],temperature=temperature,max_tokens=max_tokens,)
                return r.choices[0].message.content
            except Exception as e:
                last_err = e
        return f"Error: {last_err}"
else:
    from huggingface_hub import InferenceClient
    MODELS = ["meta-llama/Llama-3.1-8B-Instruct"]
    def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
        if not huggingface:
            return "error HF_API_KEY missing"
        last_err = None
        for m in MODELS:
            try:
                client = InferenceClient(model=m, token=huggingface)
                r = client.chat_completion(messages=[{"role": "user", "content": prompt}],temperature=temperature,max_tokens=max_tokens,)
                return r.choices[0].message.content
            except Exception as e:
                last_err = e
        return f"Error: {last_err}"
def run_activity():
    print("zero-shot one-shot few-shot learning Activity")
    category = input("Enter a category (e.g., animal, food, city): ").strip()
    item = input(f"Enter a specific {category} to classify: ").strip()
    zero_shot_prompt = f"Is {item} a {category}? Answer yes or no."
    print("zero-shot learning")
    print(f"Response: {generate_response(zero_shot_prompt, temperature=0.3, max_tokens=1024)}")
    one_shot_prompt = f"""Example:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.
Now you try:
Category: {category}
Item: {item}
Answer:"""
    print("one short learning")
    print(f"Response: {generate_response(one_shot_prompt, temperature=0.3, max_tokens=1024)}")
    few_shot_prompt = f"""Example 1:
Category: fruit
Item: apple
Answer: Yes, apple is a fruit.
Example 2:
Category: animal
Item: cat
Answer: Yes, cat is an animal.
Now you try:
Category: {category}
Item: {item}
Answer:"""
    print("few shot learning")
    print(f"Response: {generate_response(few_shot_prompt, temperature=0.3, max_tokens=1024)}")
    creative_prompt = f"""Write a one-sentence story about the given word.
Example 1: Word: moon
Story: The moon winked at the lovers as they shared their time.
Word: {item}
Story:"""
    print("creative few short learning")
    print(f"Response: {generate_response(creative_prompt, temperature=0.7, max_tokens=1024)}")
if __name__ == "__main__":
    run_activity()