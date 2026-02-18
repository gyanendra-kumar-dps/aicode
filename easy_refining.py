from config import groq,huggingface
from openai import OpenAI
from huggingface_hub import InferenceClient
GROQ_URL = "https://api.groq.com/openai/v1"
MODELS = ["llama-3.1-8b-instant", "mixtral-8x7b-32768","meta-llama/Llama-3.1-8B-Instruct"]
def generate_response(prompt,temperature,max_tokens=512):
    key=groq
    c=OpenAI(api_key=key, base_url=GROQ_URL)
    r=c.chat.completions.create(model=MODELS[0],messages=[{"role":"user","content":prompt}],temperature=temperature,max_tokens=max_tokens)
    return r.choices[0].message.content
def generate_response_hf(prompt,temperature=0.3,max_tokens=512):
    key=huggingface
    c=InferenceClient(model=MODELS[2],token=key)
    r=c.chat_completion(messages=[{"role":"user","content":prompt}],temperature=temperature,max_tokens=max_tokens)
    return r.choices[0].message.content
def get_essay_details():
    topic = input("What is the topic of your essay? ").strip()
    backend = input("Which backend would you like to use(hf,groq)? ")
    len_inp=int(input("What is the length in words (300,200)? "))
    temp=float(input("Enter temperature (0.1 structured, 0.7 creative): ").strip())
    intro_p=f"Write an introduction for an {topic} essay..."
    concl_p=f"Write a conclusion for an {topic} essay..."
    rating=int(input("\nRate satisfaction (1-5): ").strip())
    if backend=='groq':
        res=generate_response(f"{topic} {len_inp} in words {intro_p} {concl_p} according to rating {rating}",temp)
    elif backend=='hf':
        res=generate_response_hf(f"{topic} {len_inp} in words {intro_p} {concl_p} according to rating {rating}",temp)
    print(res)
if __name__=="__main__":
    get_essay_details()
