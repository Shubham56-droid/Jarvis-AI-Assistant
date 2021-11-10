import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import pywhatkit
import pyautogui

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

        if 'on my way' in musicname:
            Speak("Playing music sir")
            os.startfile('E:\\my_music\\Alan Walker, Sabrina Carpenter & Farruko - On My Way.mp3')

        elif 'apna har din' in musicname:
            Speak("Playing music sir")
            os.startfile('E:\\my_music\\Apna Har Din 128 Kbps.mp3')
        elif 'believer' in musicname:
            Speak("Playing music sir")
            os.startfile('E:\\my_music\\Believer(PagalWorld).mp3')

        elif 'I dont want to listen music' in query:
            Speak("Ok sir music closed")
            return


    def OpenApp():
        Speak("Ok sir, wait a second sir")

        if 'vs code' in query:
            os.startfile('"C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
        elif 'pycharm' in query:
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe")
        elif 'citra' in query:
            os.startfile('C:\\Users\\ADMIN\\AppData\\Local\\Citra\\canary-mingw\\citra-qt.exe')
        elif 'chrome' in query:
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        elif 'no need to open app' in query:
            return


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
            Speak("Opening youtube sir...")
            youtube = "https://www.youtube.com/"
            webbrowser.open(youtube)
            Speak("Done Sir")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir the time is, {strTime}")


        elif 'search in google' in query:
            Speak("Ok sir, This is what i found for your search in chrome")
            query = query.replace("search in google", "")
            pywhatkit.search(query)
            Speak("Done Sir")

        elif 'tell me about' in query:
            Speak("Yes sir, Searching about it sir...")
            query = query.replace("tell me about", "")
            result = wikipedia.summary(query, sentences=3)
            Speak("According to my searches")
            Speak(result)

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

        elif 'screenshot' or 'Screenshot' in query:
            Speak("Ok sir, what should be the name of the file")
            path = takeCommand()
            pathname = path + ".png"
            path1 = "C:\\Users\\ADMIN\\Pictures\\Screenshots\\"+pathname
            ss = pyautogui.screenshot()
            ss.save(path1)
            os.startfile("C:\\Users\\ADMIN\\Pictures\\Screenshots")
            Speak("Here is your screenshot sir")

        elif 'shutdown' in query:
            Speak("Jarvis shutting down sir")
            break




TaskExe()
