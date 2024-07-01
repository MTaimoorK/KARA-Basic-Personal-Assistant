import pyttsx3
import wikipedia
import webbrowser
import pywhatkit as wk
import speech_recognition as sr
import datetime
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<=12:
        speak("Morning, Mr. Taimoor.")
        
    elif hour>=12 and hour<=18:
        speak("Good Afternoon, Mr. Taimoor")
        
    else:
        speak("Good Evening, Mr. Taimoor")
        
    speak("Ready to serve, what can I do for you today?")
    
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
        
    except Exception as e:
        print("Please repeat yourself..")
        return "None"
    return query

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()
        if "alexa" in query:
            print("Yes, Sir.")
            speak("Yes, Sir.")
        
        elif "who are you?" in query:
            print("I am an AI Voice Assistant named Alexa. Created by Mr.Taimoor Khan")
            speak("I am an AI Voice Assistant named Alexa. Created by Mr.Taimoor Khan")
            
        elif "what is" in query:
            print('Searching...')
            speak('Searching...')
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to my knowledge..")
            print(results)
            speak(results)
            
        elif "just open google" in query:
            webbrowser.open('google.com')
        
        elif "open google" in query:
            print("what should I search?")
            speak("what should I search?")
            
            qry = take_command().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences = 3)
            speak(results)
            
        elif 'just open' in query:
            query = query.replace("just open", "").lower()
            webbrowser.open(f"{query}.com")
            
        elif 'search on youtube' in query:
            query = query.replace("search on", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
            
        elif "close browser" in query:
            os.system("taskkill /f /im chrome.exe")
            