import wolframalpha
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# rate = engine.getProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def WolfRamAlpha(query):
    apikey = "#Your WolframAlpha API key"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)
    
    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not available")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")
    
    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{Final} = {result}")
        speak(result)
        
    except:
        speak("The value is not anserwareble")