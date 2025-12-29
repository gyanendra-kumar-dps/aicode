from io import BytesIO
import os
import requests
import json
from PIL import Image
from config import api_key
def queryhf(api_url,payload=None,file=None,method='post'):
    headers={"Authorization":f"Bearer {api_key}"}
    if method.lower()=='post':
        res=requests.post(api_url,headers=headers,json=payload,files=file)
    else:
        res=requests.get(api_url,headers=headers,params=payload)
    return res.content
def getcap(image):
    api_url='https://api-inference.huggingface.co/models/nlpconnect/vit-gp2-image-captioning'
    buff=BytesIO()
    image.save(buff)
    buff.seek(0)
    headers={"Authorization":f"Bearer {api_key}"}
    res=requests.post(api_url,headers=headers,data=buff.read())
    res=res.json()
    caption=res[0].get("generated_text")
def gen_text(prompt,model='gpt2',max_new_tok=60):
    api_url='https://api-inference.huggingface.co/models/nlpconnect/vit-gp2-image-captioning'
    payload={'inputs':prompt,'parameters':{'max_new_tokens':max_new_tok}}
    text_bytes=queryhf(prompt,payload=payload)
    res=json.loads(text_bytes.decode('utf8'))
    gen=res[0].get('generated_text','')
    return gen
def trunc(text:str,lim):
    w=text.strip().split()
    return "".join(w[:lim])
def main():
    image_path=input('tell your path:')
    image=Image.open(image_path)
    cap=getcap(image)
    while True:
        choic=input("Enter(1,2,3,4):")
        if choic==1:
            cap=trunc(cap,5)