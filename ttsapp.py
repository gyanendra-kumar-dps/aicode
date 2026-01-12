import pyttsx3
import random
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
    while True:
        text = input("Type:").strip()
        if text.lower()=='exit':
            speak(engine,"Goodbye")
            break
        elif text.lower()=='sample':
            speak(engine,get_samples())
        else:
            speak(engine,text)
if __name__=='__main__':
    main()