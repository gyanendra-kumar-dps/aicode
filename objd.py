import requests
from PIL import Image
from io import BytesIO
from config import api_key
def gen_img(prompt,img_path,mask_path):
    url='https://api-inference.huggingface.co/models/facebook/detr-resnet-50'
    header={
        "Authorization":f"Bearer {api_key}"
    }
    with open(img_path,'rb') as f:
        image_data=f.read()
    with open(mask_path,'rb') as f:
        mask_data=f.read()
    payload={"inputs":prompt}
    res=requests.post(url,headers=header,data=payload,files={'image':['image.jpg',image_data,'images/jpg'],'mask':['mask.jpg',mask_data,'images/jpg']})
    return Image.open(BytesIO(res.content))
def main():
    while True:
        inp=input("Enter a prompt:")
        resimg=gen_img(inp,'picture_1762187885.jpg','picture_1762187885.jpg')
        resimg.show()
        resimg.save("out.jpg")
if __name__=='__main__':
    main()