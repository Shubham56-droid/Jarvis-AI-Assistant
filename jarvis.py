import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import os
import webbrowser
import pywhatkit

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices', voices[1].id)
Assistant.setProperty('rate', 170)


def Speak(audio):
    Assistant.say(audio)
    print(f'Jarvis:{audio}')
    Assistant.runAndWait()


def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 0.8
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language="en-in")
            print(f"User said:{query}\n")

        except Exception as Error:
            print("Unable to recogonize sir")
            return "None"

        return query.lower()


def TaskExe():

    def Music():
        Speak("tell me the name of music")
        musicname = takeCommand()

        if 'On my way' in query:
            os.startfile('')

    while True:
        query = takeCommand()
        if 'hello' in query:
            Speak('Hello Sir,Jarvis here')
            Speak('Your personal AI Assistant')
            Speak('Do you need any help sir ?')

        elif 'search in youtube' in query:
            Speak("Ok sir, This is what i found for your search")
            query = query.replace("search in youtube", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done sir")

        elif 'in wikipedia' in query:
            Speak("Searching in wikipedia sir...")
            query = query.replace("in wekipedia","")
            results = wikipedia.summary(query,sentences=3)
            Speak("According to my searches")
            Speak(results)

        elif 'open youtube' in query:
            

        elif 'search in google' in query:
            Speak("Ok sir, This is what i found for your search in chrome")
            query = query.replace("search in google", "")
            pywhatkit.search(query)
            Speak("Done Sir")

        elif 'open website' in query:
            Speak("Ok sir, launching...")
            query = query.replace("open website","")
            query.lower()
            web2 = 'https://www.' + query + '.com'
            webbrowser.open(web2)
            Speak("Done Sir")

        elif 'launch' in query:
            Speak("Tell me the name of the website")
            name = takeCommand()
            web3 = 'https://www.'+ name + '.com'
            webbrowser.open(web3)
            Speak("Done Sir")



        elif 'shutdow' in query:
            Speak("Jarvis shutting down sir")
            break




TaskExe()
