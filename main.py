import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
from gtts import gTTS
import pygame
import os

r = sr.Recognizer()
ttsx = pyttsx3.init()
newsapi="<API KEY>"


def speak_old(text):
    ttsx.say(text)
    ttsx.runAndWait()
    
def speak(text):
    tts=gTTS("hello")
    tts.save("temp.mp3")
    
    #intialize pygame mixer
    pygame.mixer.init()
    
    #load the mp3 file
    pygame.mixer.music.load('temp.mp3')
    
    #keep the pogram running until the file ends
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


    pygame.mixer.music.unload('temp.mp3')
    os.remove('temp.mp3')
    
def gemini(command):
    genai.configure(api_key="<API KEY>")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(command+"\n Give a short answer")
    return (response.text)
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code==200:
            #parse the json response
            data=r.json()
            
            #extract the articles
            articles=data.get('articles',[])
            
            #print the headlines
            for article in articles:
                speak(article['title'])
                
    else:
        #let OpenAI handle the request
        output=gemini(c)
        output=output.replace('*','')
        speak(output)
    
            
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    audio = r.listen(source,timeout=2,phrase_time_limit=2)
                command = r.recognize_google(audio)
                print(command)    

                processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))