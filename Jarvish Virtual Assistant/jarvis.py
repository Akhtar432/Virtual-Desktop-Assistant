# from email.mime import audio
import code
from http import client
import json
from time import sleep
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import ssl
import requests
from urllib.request import urlopen
import subprocess
import ctypes
from ecapture import ecapture as ec
import time
# import wolframalpha
# import pywhatkit


# speak function for speak
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("good Evening!")
        
    speak("I am Jarvis Sir. Please tell me how may I help you")
    
def takeCommand():
    # It take microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")
    
    except Exception as e:
        # print(e)
        
        print("Said that again please...")
        return "None"
        
    return query

def sendemail(to,content):
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL('smtp.gmail.com',997,context=context)
    server.ehlo()
    server.starttls()
    server.login('ashwanikumarkharwar83@outlook.com','Ashwani@123')
    server.sendmail('ashwanikumarkharwar83@outlook.com',to,content)
    server.close()
        
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    
    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            
        elif 'open google' in query:
            webbrowser.open('goole.com')
            
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
            
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Ashwani.")
            
            
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
            
        elif "who are you" in query:
            speak("I am your virtual assistant created by Ashwani")
            
            
        elif 'play video' in query:
            video_file = 'D:\\Video'
            videos = os.listdir(video_file)
            print(videos)
            os.startfile(os.path.join(video_file,videos[0]))
            
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
            
        elif 'open code' in query:
            code_path = 'C:\\Users\\ashwa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(code_path)
            
        elif 'send email' in query:
            try:
                speak('What would you like to send')
                content = takeCommand()
                to = 'manukumar1999gpl@gmail.com'
                sendemail(to,content)
                speak("Email is Sent")
            except Exception as e:
                print(e)
                speak("Sorry Sir I am not able to send this email")
                
        elif 'read news' in query:
            speak("Which Type of news you want to listen")
            content = takeCommand().lower()
            try:
                jsonObj = urlopen(f'https://newsapi.org/v2/everything?q={content}&apiKey=13326fd4847847df8008e49f291f3b69')
                data = json.load(jsonObj)
                i = 1
                speak("Here are the Top news")
                for item in data['articles']:
                    print(str(i) + '. ' + item['content'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    
                    if i>3:
                        exit()
                    i += 1
                    
            except Exception as e:
                print(e)
                
        elif 'lock system' in query:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()
            
        elif 'shutdown system' in query:
            speak("Hold On A sec Your System is on its way to shut down")
            subprocess.call('shutdown / p /f')
            
        elif 'camera' in query or 'take a photo' in query:
            ec.capture(0,"jarvis Camera","img.jpg")
            
        elif 'sleep' in query:
            speak("Sleeping system")
            subprocess.call(["shutdown","/1"])
            
        # elif 'what is' in query or 'who is' in query:
        #     client = wolframalpha.Client('PWE9VY-JQ8YLAG48Y')
        #     res = client.query(query)
            
        #     try:
        #         print (next(res.results).text)
        #         speak (next(res.results).text)
        #     except Exception as StopIteration:
        #         print("No Results")
        
        
        elif 'search' in query:
             
            query = query.replace("search", "")      
            webbrowser.open(f'google.com/{query}')
            
        elif 'on youtube' in query:
            query = query.replace("on youtube","")
            speak("Start Playing")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
            
            
        elif 'open browser' in query or 'open brave' in query:
            brave = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            os.startfile(brave)
            
        elif 'stop listening' in query or "don't listen" in query:
            speak("Ok ")
            exit()              