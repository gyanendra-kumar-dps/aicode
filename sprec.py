import speech_recognition as sr
import pyttsx3
from googletrans import Translator
from datetime import datetime
import os
user={}
usercount=0
def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    if language == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("please speak now in English:-")
        audio = recognizer.listen(source)
    try:
        print("recognizing your speech")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"you said:-{text}")
        return text
    except sr.UnknownValueError:
        print("could not understand your audio")
    except sr.RequestError as e:
        print(f"api error:-{e}")
def translate_text(text, target_language="es"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"translated text:-{translation.text}")
    return translation.text
def display_language_options():
    print("Available translation languages:-")
    print("1:- Hindi(hi)")
    print("2:- Tamil(ta)")
    print("3:- Telugu(te)")
    print("4:- Bengali(bn)")
    print("5:- Marathi(mr)")
    print("6:- Gujarati(gu)")
    print("7:- Malayalam(ml)")
    print("8:- Punjabi(pa)")
    choice = input("Please select the target language number (1-8): ")
    language_dict = {"1":"hi","2":"ta","3":"te","4":"bn","5":"mr","6":"gu","7":"ml","8":"pa"}
    return language_dict.get(choice, "es")
def main():
    while True:
        globals()['usercount']+=1
        target_language = display_language_options()
        original_text = input("Enter your text:")
        if original_text:
            translated_text = translate_text(original_text, target_language=target_language)
            os.system(f'say {translated_text}')
            print("translation done")
        user[f'user{globals()['usercount']}']=original_text
        with open('ttsapp.json','w') as f:
            f.write(f'{user}'.replace("'",'"'))
if __name__=="__main__":
    main()