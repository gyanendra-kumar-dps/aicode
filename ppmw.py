import requests
from PIL import Image,ImageEnhance,ImageFilter
from io import BytesIO
imurl='https://router.huggingface.co/models/stabilityai/stable-diffusion-2-1'
def request_handling(prompt):
    headers={
        "Authorization":f"Bearer {''}"
    }
    payload={
        "inputs":f"{prompt}"
    }
    response=requests.post(imurl,headers=headers,json=payload)  
    print(response.content)
    image=image=Image.open(BytesIO(response.content))
    return image
def enhance_func(image):
    enhancer=ImageEnhance.Brightness(image)
    bright_img=enhancer.enhance(1.2)
    contrast_img=enhancer.enhance(1.3)
    filter_img=contrast_img.filter(ImageFilter.GaussianBlur(radius=2))
    return filter_img
while True:
    inp=input("enter a prompt:")
    img=request_handling(inp)
    eimage=enhance_func(img)
    inp_img=input("do you want to save it:")
    if inp_img.lower()=='yes':
        inp_name=input("what will be the name without ext:")
        eimage.save(inp_name)