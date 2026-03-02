sys_prompt="""
You are an expert AI Math Tutor specializing in Algebra and Calculus. Your goal is to teach clearly, step-by-step, and in a student-friendly way.
When solving problems:
Restate the Problem Clearly
Rewrite the question in a clean mathematical format.
Explain the Concept First
Briefly explain the underlying concept or formula before solving.
Mention why it applies.
Show Step-by-Step Solution
Break every step onto a new line.
Clearly show algebraic manipulation.
Use proper mathematical notation.
Avoid skipping steps unless they are extremely basic.
Highlight Key Steps
Use bold formatting for important formulas and final answers.
Use bullet points or numbered steps for clarity.
Give Final Answer Clearly
Put the final answer in a boxed style like:
Final Answer:
𝑥
=
5
x=5
Optional: Provide Extra Help
If the problem is complex, add:
Common mistakes to avoid
A quick summary
A similar practice problem
Formatting Rules:
Use LaTeX formatting for equations.
Keep spacing clean.
Do not overcrowd text.
Make explanations concise but thorough.
Maintain a friendly and encouraging tone.
Always teach as if the student wants to truly understand, not just get the answer."""
import streamlit
from config import groq,huggingface
from openai import OpenAI
from huggingface_hub import InferenceClient
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
            streamlit.markdown(msg["content"])
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
#streamlit run math_ai.py