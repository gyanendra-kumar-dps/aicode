import pyttsx3
import random
json_to_write={}
def setup_tts():
    engine=pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 0.9)
    return engine
def speak(engine:pyttsx3.Engine,text):
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except:
            print(f"audio:{text}")
    else:
        print(f"audio:{text}")
def get_samples():
    sample=["Hello! I am your computer","Python is awesome","This is A.I speaking","Welcome to the future"]
    return random.choice(sample)
def main():
    engine = setup_tts()
    if engine:
        print("type something")
    else:
        print("audio not audible")
    speak(engine, "type something")
    user_input_count=0
    while True:
        text = input("Type:").strip()
        user_input_count+=1
        if text.lower()=='exit':
            speak(engine,"Goodbye")
            json_to_write[f'input{user_input_count}']=text
            json_to_write[f'output{user_input_count}']="Goodbye"
            break
        elif text.lower()=='sample':
            sample=get_samples()
            json_to_write[f'input{user_input_count}']=text
            json_to_write[f'output{user_input_count}']=sample
            speak(engine,sample)
        else:
            json_to_write[f'input{user_input_count}']=text
            json_to_write[f'output{user_input_count}']=text
            speak(engine,text)
    with open('ttsapp.json','w') as f:
        f.write(str(json_to_write))
if __name__=='__main__':
    main()