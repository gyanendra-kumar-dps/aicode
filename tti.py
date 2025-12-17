import requests
from PIL import Image
from io import BytesIO
from config import api_key
from time import time
url="https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
def gen_image():
    while True:
        inp=input("Enter your prompt:")
        header={"Authorization":f"Bearer {api_key}"}
        inpu={"inputs":inp,"ptions": {"wait_for_model": True}}
        res=requests.post(url,headers=header,json=inpu,timeout=30)
        jsn=res.headers.get("Content-Type","").lower()
        if 'image' in jsn:
            jsonimage=res.content
            img=Image.open(BytesIO(jsonimage))
            img.save(f"file_{int(time())}")   
gen_image()