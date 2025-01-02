import requests
import json
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
# rate = engine.getProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=#here paste your api key",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=#here paste your api key",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=#here paste your api key",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=#here paste your api key",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=#here paste your api key",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=#here paste your api key"
}
    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url found")
            break
        else:
            url = True
    if url is True:
        speak("url not found")
        
    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")
    
    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"For more info visit: {news_url}")

        a = input("[press 1 to contine] and [press any key to stop]")
        if a == "stop":
            speak("Thanks for listening")
            break
        
    speak("That's all for today. Have a nice day sir. See you again")