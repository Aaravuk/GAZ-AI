import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# rate = engine.getProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greetME():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, SIR!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, SIR!")
    
    else:
        speak("Good Evening, SIR!")
    
    speak("I'm GAZ, How may I help you?")