import pyttsx3 
import speech_recognition as sr
import random

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
        audio = r.listen(source)
        print("Recognizing...")
        
        try:
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
    return query

def game_play():
    speak("Let's Play Rock, Paper, Scissors!")
    print("Let's Playyyyyyyyy!")
    i = 0
    Me_score = 0
    Com_score = 0
    while i < 5:
        choose = ("rock", "paper", "scissors")
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if query == "rock":
            if com_choose == "rock":
                speak("ROCK")
                print(f"Score: Me:- {Me_score} - Computer:- {Com_score}")
            elif com_choose == "paper":
                speak("PAPER")
                Com_score += 1
                print(f"Score: Me:- {Me_score} - Computer:- {Com_score}")
            else:
                speak("SCISSORS")
                Me_score += 1
                print(f"Score: Me:- {Me_score} - Computer:- {Com_score}")
        elif (query == "paper" ):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1
    
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")