import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) 
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning! Sir")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir")
    
    else:
        speak("Good Evening! Sir")
    
    speak("My Name Is Jarvis , How may I help you.")

def takecommand():
    '''
    It takes microphone input from user
    '''
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        # r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)

        print("Please say that again..")
        return "None"
    return query

def commands(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia')
        query= query.replace("wikipedia","")
        results = wikipedia.summary(query , sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
        
    elif "open youtube" in query:
        # webbrowser.open("youtube.com")
        speak("opening..")
        url="https://youtube.com"
        webbrowser.open(url)
        # webbrowser.get(using='windows-default').open("youtube.com")

    elif "open google" in query:
        # webbrowser.open("google.com")
        speak("opening")
        url="https://google.com"
        webbrowser.open(url)
    
    elif "time" in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir , The time is {strtime} ")
    
    elif "finish" in query:
        speak("Thank you Sir..")
        exit()
    
    # elif ""
 
if __name__ == "__main__":
    # speak("Hello Anand Samantnani")
    # wishme()
    # while True:
    query = takecommand().lower()

    commands(query)
    