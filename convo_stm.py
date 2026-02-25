#streamlit run stm_ai.py
import streamlit
from config import groq,huggingface
from openai import OpenAI
from huggingface_hub import InferenceClient
sys_prompt="""You are an AI Teaching Assistant.
Your role is to:
Explain concepts clearly and step-by-step.
Adapt explanations to the student’s level.
Use examples and analogies when helpful.
Encourage critical thinking instead of giving direct answers immediately.
Ask guiding questions if the student is stuck.
Be patient, supportive, and encouraging.
Provide short summaries at the end of explanations.
If a student asks for homework answers directly, guide them through the solution instead of giving the final answer immediately.
If you spot an incomplete prompt then respond with could you please complete you sentence"""
if "messages" not in streamlit.session_state:
    streamlit.session_state.messages = [{"role": "system", "content": sys_prompt}]
GROQ_URL = "https://api.groq.com/openai/v1"
MODELS = ["llama-3.1-8b-instant", "mixtral-8x7b-32768","meta-llama/Llama-3.1-8B-Instruct"]
c=OpenAI(api_key=groq, base_url=GROQ_URL)
d=InferenceClient(model=MODELS[2],token=huggingface)
def generate_response(prompt,temperature=0.3,max_tokens=512):
    key=groq
    r=c.chat.completions.create(model=MODELS[0],messages=streamlit.session_state.messages,temperature=temperature,max_tokens=max_tokens)
    return r.choices[0].message.content
def generate_response_hf(prompt,temperature=0.3,max_tokens=512):
    key=huggingface
    r=d.chat_completion(messages=[{"role":"system","content":sys_prompt},{"role":"user","content":prompt}],temperature=temperature,max_tokens=max_tokens)
    return r.choices[0].message.content
def conversation(inp,reply):
    streamlit.session_state.messages.append({"role": "user", "content": inp})
    streamlit.session_state.messages.append({"role": "assistant", "content": reply})
    for msg in streamlit.session_state.messages:
        with streamlit.chat_message(msg["role"]):
            streamlit.text(msg["content"])
streamlit.title("Your own AI teaching assistant")
is_hf=False
with streamlit.sidebar:
    streamlit.title("Settings")
    toggle=streamlit.toggle("On to switch to HF Off to switch to GROQ")
    if toggle:
        is_hf=True
        streamlit.info("Now hugging face model is being used")
    else:
        is_hf=False
        streamlit.info("Now groq model is being used")
input=streamlit.chat_input("Enter you doubt here:")
if input:
    if not is_hf:
        conversation(input,generate_response(input))
        streamlit.warning("Now groq model is being used")
    else:
        conversation(input,generate_response_hf(input))
        streamlit.warning("Now hugging face model is being used")
def return_to_file():
    printing_list=[]
    for i in streamlit.session_state.messages:
        printing_list.append(i['role']+' : '+i['content'])
    return(''.join(printing_list))