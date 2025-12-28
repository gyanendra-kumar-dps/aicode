import requests
from config import api_key
url = ""
headers={

}
def captioning_image():
    file_name="tree.jpg"
    with open(file_name,'rb') as f:
        image_bytes=f.read()
    res=requests.post(url,headers=headers,data=image_bytes)
    print(res.status_code)
    result=res.json()
    return result
if __name__=='__main__':
    captioning_image()
