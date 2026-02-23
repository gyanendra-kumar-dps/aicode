#streamlit run stm_ai.py
import streamlit
from config import groq,huggingface
from openai import OpenAI
from huggingface_hub import InferenceClient
if "messages" not in streamlit.session_state:
    streamlit.session_state.messages = []
GROQ_URL = "https://api.groq.com/openai/v1"
MODELS = ["llama-3.1-8b-instant", "mixtral-8x7b-32768","meta-llama/Llama-3.1-8B-Instruct"]
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
def generate_response(prompt,temperature=0.3,max_tokens=512):
    key=groq
    c=OpenAI(api_key=key, base_url=GROQ_URL)
    r=c.chat.completions.create(model=MODELS[0],messages=[{"role":"system","content":sys_prompt},{"role":"user","content":prompt}],temperature=temperature,max_tokens=max_tokens)
    return r.choices[0].message.content
def generate_response_hf(prompt,temperature=0.3,max_tokens=512):
    key=huggingface
    c=InferenceClient(model=MODELS[2],token=key)
    r=c.chat_completion(messages=[{"role":"system","content":sys_prompt},{"role":"user","content":prompt}],temperature=temperature,max_tokens=max_tokens)
    return r.choices[0].message.content
def conversation(inp,reply):
    streamlit.session_state.messages.append({"role": "user", "content": inp})
    streamlit.session_state.messages.append({"role": "assistant", "content": reply})
    for msg in streamlit.session_state.messages:
        with streamlit.chat_message(msg["role"]):
            streamlit.text(msg["content"])
streamlit.title("Your own AI teaching assistant")
with streamlit.sidebar:
    streamlit.title("Settings")
    toggle=streamlit.toggle("On to switch to HF Off to switch to GROQ")
input=streamlit.chat_input("Enter you doubt here:")
if input:
    conversation(input,generate_response(input))