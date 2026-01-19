import speech_recognition as sr
import pyttsx3
from googletrans import Translator
def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
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
        print("please speak now in English")
        audio = recognizer.listen(source)
    try:
        print("recognizing speech")

        text = recognizer.recognize_google(audio, language="en-US")
        print(f"you said:{text}")
        return text
    except sr.UnknownValueError:
        print("could not understand the audio.error")
    except sr.RequestError as e:
        print(f"api is giving error: {e}")
    return""
def translate_text(text,target_language="es"):
    translator=Translator()
    translation=translator.translate(text,target_language)
    return translation.text
def display_language_options():
    print("Hindi (hi)")
    print("Tamil (ta)")
    print("Telugu (te)")
    print("Bengali (bn)")
    print("Marathi (mr)")
    print("Gujarati (gu)")
    print("Malayalam (ml)")
    print("Punjabi (pa)")
    choice=input("Enter you choice:")
    language_dict = {"1": "hi", "2": "ta", "3": "te", "4": "bn","5": "mr", "6": "gu", "7": "ml", "8": "pa"}
    return language_dict.get(choice,"es")
def main():
    target_language=display_language_options()
    original_text=speech_to_text()
    translated_text=translate_text(original_text,target_language)
    speak(translated_text,"en")
main()