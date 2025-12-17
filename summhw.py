from colorama import Fore
import requests
from config import api_key
def query(payload,modelname):
    header={"Authorization":f"Bearer {api_key}"}
    res=requests.post(f"https://router.huggingface.co/hf-inference/models/{modelname}",headers=header,json=payload)
    return res.json()
def summary_of_text(text,minl,maxl,modelname="google/pegasus-xsum"):
    payl={
        "inputs":text,
        "parameters":{"min_length":int(minl),"max_length":int(maxl)}
    }
    print(Fore.BLUE+f"Performing summary using ai model {modelname}")
    res=query(payl,modelname)
    print(Fore.BLUE+"Your summary creation is done")
    return res
if __name__=="__main__":
    name=input("Hey what is your name:")
    mdl=input("What model would you like to use(google/pegasus-xsum,facebook/bart):")
    mil=input("What min len you want for summary:")
    mal=input("What max len you want for summary:")
    text=input("What is the text:")
    print(summary_of_text(text,mil,mal,mdl))