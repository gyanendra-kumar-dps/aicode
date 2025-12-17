import requests
from config import api_key
movie_review={
    'Frankestein':'This is a fantastic watch, praised for its gorgeous visuals, emotional depth, and a standout, "phenomenal" performance by Jacob Elordi as the creature. Critics are calling it the "defining 21st-century cinematic Frankenstein" that finds the humanity in the iconic monster. Some critics find the two-and-a-half-hour run time a bit long and the dialogue occasionally weak. A few audience members felt the film was "overwrought" and overly stylized.',
    'Predator:Badlands':'Audiences and many critics call this a "fun time" and an enjoyable, action-packed movie that offers a fresh take on the Predators culture and home world. It is considered a solid, entertaining entry in the franchise, with Elle Fannings performance bringing charm and humor.',
    'The running man':'Glen Powells lead performance is widely praised as the best part of the movie, keeping the film afloat with his charisma and "dad action" appeal. The film is considered a relevant, fun, and high-octane action ride that stays closer to Stephen Kings original novel than the 1987 classic.The movie struggles with a "convoluted mess" of a script and a "messy ending" that feels too "prim" and "perfect" for its dystopian themes. Some viewers felt the Edgar Wright direction was subdued and lacked his signature flair.',
    'Nuremberg':'Russell Crowe delivers a commanding performance in this "handsomely crafted historical drama". Its measured, serious tone has resonated strongly with audiences who gave it an impressive 96% score.The film is noted for being slow-paced, which might not appeal to all viewers.',
    'One Battle After Another':'Paul Thomas Andersons latest is a hit with critics, who praise its "awe-inspiring action set pieces" and find it both entertaining and thematically rich. The near-perfect audience score of 96% suggests most viewers loved it.No major criticisms have emerged; the consensus is overwhelmingly positive.'
}
url="https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
headers={
    'Authorization':f'Bearer {api_key}'
}

for i in movie_review:
    res=requests.post(url,headers=headers,json={'inputs':i})
    res=res.json()
    print(f"{res[0][0]['label']}:- {res[0][0]['score']*100:.4f}%")