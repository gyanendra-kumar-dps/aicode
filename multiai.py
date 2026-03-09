import streamlit as st
from config import groq, huggingface
from openai import OpenAI
from huggingface_hub import InferenceClient
from PIL import Image
sys_prompt = """
You are an expert AI Math Tutor specializing in Algebra and Calculus.
When solving problems:
1. Restate the problem
2. Explain the concept
3. Show step-by-step solution
4. Highlight formulas
5. Give final answer clearly
Use LaTeX formatting for equations.
If questions of other topic asked even answer that in short.
"""
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": sys_prompt}]
GROQ_URL = "https://api.groq.com/openai/v1"
groq_client = OpenAI(api_key=groq,base_url=GROQ_URL)
hf_client = InferenceClient(model="meta-llama/Llama-3.1-8B-Instruct",token=huggingface)
image_client = InferenceClient(provider="hf-inference",api_key=huggingface)
def generate_groq():
    r = groq_client.chat.completions.create(model="llama-3.1-8b-instant",messages=st.session_state.messages,temperature=0.3,max_tokens=512)
    return r.choices[0].message.content
def generate_hf(prompt):
    r = hf_client.chat_completion(
        messages=[{"role": "system", "content": sys_prompt},{"role": "user", "content": prompt}],temperature=0.3,max_tokens=512)
    return r.choices[0].message.content
def generate_image(prompt):
    image = image_client.text_to_image(prompt,model="stabilityai/stable-diffusion-xl-base-1.0")
    path = "generated.png"
    image.save(path)
    return path
def is_image_prompt(prompt):
    keywords = ['make image','image',"draw","generate image","create image","picture","illustration","diagram"]
    for word in keywords:
        if word in prompt.lower():
            return True
    return False
st.title("AI Math Tutor + Image Generator")
with st.sidebar:
    st.header("Settings")
    use_hf = st.toggle("Use HuggingFace instead of Groq")
    if use_hf:
        st.info("HuggingFace model active")
    else:
        st.info("Groq model active")
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            if msg.get("type") == "image":
                st.image(msg["content"])
            else:
                st.markdown(msg["content"])
user_input = st.chat_input("Enter your question or request an image")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            if is_image_prompt(user_input):
                img = generate_image(user_input)
                st.image(img)
                st.session_state.messages.append({"role": "assistant","content": img,"type": "image"})
            else:
                if use_hf:
                    reply = generate_hf(user_input)
                else:
                    reply = generate_groq()
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant","content": reply})
def export_chat():
    text = ""
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            text += f"{msg['role']} : {msg['content']}\n\n"
    return text
st.sidebar.download_button(
    "Download Chat",
    export_chat(),
    "math_chat.txt"
)
#streamlit run multiai.py