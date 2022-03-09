# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import  speech_recognition as sr
import webbrowser as wb
import datetime as dt
import time




from gtts import gTTS
from playsound import playsound
import random 
import os



r=sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio=r.listen(source)
        voice=''
        
        try:
            voice=r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            speak("Anlamadım")
            
        except sr.RequestError:
            speak("Hata oluştu")
            
        return voice
    
    
    
    
    
def response(voice):
    if 'nasılsın' in voice:
        speak("İyi")
    if 'havalar nasıl' in voice:
        speak("Yağmurlu")
    if 'burası güneşli' in voice:
        speak("güneşi sevmem")
        exit()
       
    
    

def speak(string):
    tts=gTTS(string,lang="tr")
    rand=random.randint(1, 1000)
    file="audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
    
    
speak("Bismillahirrahmanirrahîm Sübhânekellâhümme ve bi hamdik ve tebârakesmük ve teâlâ ceddük ve lâ ilâhe ğayrük.")
while 1:
    voice=record()
    print(voice)
    response(voice)

