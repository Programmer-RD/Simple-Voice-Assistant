import speech_recognition as sr
import playsound
import webbrowser
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            talk("ask " + ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
            talk("I didnt get what you said ! ")
        except sr.RequestError:
            talk("My Sever is broken ! ")


def talk(text):
    tts = gTTS(text=text, lang="en")
    r_ = random.randint(1, 10000000000000000000)
    filename = "audio-" + str(r_) + ".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    print(text)
    os.remove(filename)


def respond(voice_data):
    try:
        if "what is your name" in voice_data:
            talk("My Name is Ranuga ! ")
        if "what is the time" in voice_data:
            talk(ctime())
        if "search" in voice_data:
            talk("Say what ")
            time.sleep(2.5)
            search = record_audio("What do you want to search for ? ")
            url = f"https://google.com/search?q={search}"
            webbrowser.get().open(url)
            talk(f"Results : {search}")
        if "find location" in voice_data:
            talk("Say what ")
            loc = record_audio("What is the location ? ")
            url = "https://google.nl/maps/place" + loc + "/&amp;"
            webbrowser.get().open(url)
            talk(f"Location Searched : {loc}")
        if "exit" in voice_data:
            talk("Exiting....")
            quit()
        if "thanks" in voice_data or "thank" in voice_data:
            talk("No Problem Bro ! ")
    except:
        talk("I didnt get that ! ")


talk("How can I help you ? ")
while 1:
    voice_data = record_audio()
    respond(voice_data)
