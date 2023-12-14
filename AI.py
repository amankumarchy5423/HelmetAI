import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser



engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour =int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good After Noon Sir!")

    else:
        speak("Good Night Sir!")

    speak("I am aman sir. Please tell me how i may help you")

def takecomand():
    '''it take microphone input from the user and return string output'''
    r=sr.Recognizer()
    with sr. Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")

    except Exception as e :
        print (e)
        print("say that again please...")
        return "None"
    return query

if __name__ == "__main__" :
    speak("Hello")
    wishMe()
    while True:
        qurey = takecomand().lower()
        if 'wikipedia' in qurey:
            speak('searching wikipedia...')
            qurey = qurey.replace("wikipedia", "")
            results =wikipedia.summary(qurey,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in qurey:
            webbrowser.open("youtube.com")
        elif 'open google' in qurey:
            webbrowser.open("google.com")
    
    


