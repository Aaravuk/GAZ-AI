import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import time

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# rate = engine.getProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5)
        
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("Could not understand. Please try again.")
        return "None" 
    return query

# set alarm
def alarm(query):
    Timehere = open("Alarmtext.txt", "a")
    Timehere.write(query)
    Timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetME
            greetME()
            
            while True:
                query = takeCommand().lower()
                
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break
                
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                    
                elif "i am fine" in query:
                    speak("that's great, sir")
                    
                elif "how are you" in query:
                    speak("Perfect, sir")
                    
                elif "thank you" in query:
                    responses = [
                    "You're most welcome, sir.",
                    "Anytime, sir.",
                    "Is there anything else I can help you with, sir?",
                    "Happy to help, sir.",
                    ]
                    speak.random.choice(responses)
                
                # Opening Apps
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                # Closing Apps
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                
                # Searching from web
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                
                # Temperatures
                elif "temperature" in query:
                    search = "temperature in Rayagada"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                
                # Alarm
                elif "set alarm" in query:
                    print("Input time exapmle:- 10 and 10 and 10")
                    speak("Tell me the time to set alarm:- ")
                    a = input("Please tell me the time to set alarm:- ")
                    alarm(a)
                    speak("Alarm has been set")
                    
                # Youtube Controls like Play, Pause, Stop, Mute
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted")
                
                elif "volume up" in query:
                    from Keyboard import volumeup
                    speak("Turning volume up, Sir")
                    volumeup()
                elif "volume down" in query:
                    from Keyboard import volumedown
                    speak("Turning volume down, Sir")
                    volumedown()
                    
                # Reminder
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me to remember that" + rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me to remember that" + remember.read())
                    remember.close()
                
                # Personalized Playlist
                # elif "tired" in query:
                #     speak("Playing your favourite song, sir")
                #     a = (1,2,3) #You can  choose any numbers of songs
                #     b = random.choice(a)
                #     if b ==1:
                #         webbrowser.open(https://youtu.be/6xJypoyQFnQ?si=nemjLSvWvJW2tKdy)
                #     elif b ==2:
                #         webbrowser.open(https://youtu.be/mt-5ZbKqiDc?si=t5dAqSoUVdXl3s7b)
                #     elif b ==3:
                #         webbrowser.open(https://youtu.be/vsWxs1tuwDk?si=1wyIBPpEujXR0mr2)
                
                # News Function
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                
                # Calculator
                elif "calculate" in query:
                    from Calculatenumbers import Wolframalpha
                    from Calculatenumbers import Calc
                    query = query.replace("jarvis", "")
                    query = query.replace("calculate", "")
                    Calc(query)
                
                # WhatsApp automation
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                
                # Shutdown system with your voice
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shut down?")
                    shutdown = input("Do you wish to shutdown your computer? (y/n): ")
                    if shutdown == "y":
                        speak("Shutting down the system")
                        os.system("shutdown /s /t 1")
                    elif shutdown == "n":
                        break
                    
                # Time
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                
                # Finally Sleep
                elif "finally sleep" in query:
                    speak("Okay, sir, I will go to sleep now.")
                    break

