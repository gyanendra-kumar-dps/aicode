from huggingface_hub import InferenceClient
from config import huggingface
import streamlit
from PIL import Image
client = InferenceClient(
    provider="hf-inference",
    api_key=huggingface
)
if "messages" not in streamlit.session_state:
    streamlit.session_state.messages = []
def generate_response_hf(prompt,temperature=0.3,max_tokens=512):
    image = client.text_to_image(
    prompt,
    model="stabilityai/stable-diffusion-xl-base-1.0"
    )
    image.save("castle.png")
    return "castle.png"
def conversation(inp):
    generate_response_hf(inp)
    streamlit.session_state.messages.append({"role": "user", "content": inp})
    streamlit.session_state.messages.append({"role": "assistant", "content": "castle.png"})
    for msg in streamlit.session_state.messages:
        with streamlit.chat_message(msg["role"]):
            if(msg['content']=="castle.png"):
                streamlit.image(Image.open("castle.png"))
            else:
                streamlit.markdown(msg["content"])
streamlit.title("Your own AI image generator")
input=streamlit.chat_input("Enter you prompt here")
if input:
    conversation(input)
#streamlit run im_strmlit.py