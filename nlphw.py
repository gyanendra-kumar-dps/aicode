from config import api_key
import requests
url="https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
header={'Authorization':f'Bearer {api_key}'}
def get_data(text):
    res=requests.post(url,headers=header,json={'inputs':text})
    return res.json()
while True:
    inp=input("Enter a sentence for analysis:")
    data=get_data(inp)
    print(f"{data[0][0]['label']}:- {data[0][0]['score']*100:.4f}%")
    print(f"{data[0][1]['label']}:- {get_data(inp)[0][1]['score']*100:.4f}%")