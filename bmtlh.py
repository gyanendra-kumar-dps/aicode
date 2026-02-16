from config import groq
from openai import OpenAI
from huggingface_hub import InferenceClient
GROQ_URL="https://api.groq.com/openai/v1"
MODELS=["llama-3.1-8b-instant","meta-llama/Llama-3.1-8B-Instruct"]
def generate_response(prompt,temperature=0.3,max_tokens=512):
    key=groq
    client=OpenAI(api_key=key,base_url=GROQ_URL)
    response=client.chat.completions.create(model=MODELS[0],messages=[{"role":"user","content":prompt}],temperature=temperature,max_tokens=max_tokens)
    return response.choices[0].message.content
def generate_response_hf(prompt,temperature=0.4,max_tokens=512):
    model_name=MODELS[1]
    client=InferenceClient(model=model_name)
    response=client.chat_completion(messages=[{"role":"user","content":prompt}],temperature=temperature,max_tokens=max_tokens)
    return response.choices[0].message.content
def token_limit_activity():
    prompt=input("enter a prompt:").strip()
    short_response=generate_response(prompt, max_tokens=50)
    long_response=generate_response(prompt, max_tokens=500)
    print(short_response)
    print(long_response)
def bias_mitigation_activity():
    prompt=input("enter a prompt to explore bias:").strip()
    initial_response=generate_response(prompt,temperature=0.3,max_tokens=500)
    print(initial_response)
    revised_prompt=input("enter revised prompt:").strip()
    revised_response=generate_response(revised_prompt,temperature=0.3,max_tokens=500)
    print(revised_response)
def run_activity():
    while True:
        choice=input(">>").strip()
        if choice=="1":
            bias_mitigation_activity()
        elif choice=="2":
            token_limit_activity()
        elif choice=="3":
            print("exiting program")
            break
        else:
            print("invalid choice please try again")
if __name__=='__main__':
    run_activity()