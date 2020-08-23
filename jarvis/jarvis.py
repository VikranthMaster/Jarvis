import cv2
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


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
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com') 
    server.ehlo()
    server.starttls()
    server.login("TestEmailVik@gmail.com","vikranth@master")
    server.sendmail("TestEmailVik@gmail.com",to, content)
    server.close()

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def show_image():
    img = cv2.imread("space.jpg")
    cv2.imshow("Space Image",img)
    cv2.waitKey(0)

if __name__ == "__main__":
    wishMe()

    while True:
    # if 1:
        query = takeCommand().lower()

        WIKIPEDIA = ["wikipedia","who","what"]
        for phrase in WIKIPEDIA:
            if phrase in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

        YOUTUBE = ["open youtube","i want to watch videos","i want to watch movies"]
        for phrase in YOUTUBE:
            if phrase in query:
                    webbrowser.open("https://www.youtube.com/")

        GOOGLE = ["open google","search"]
        for phrase in GOOGLE:
            if phrase in query:
                webbrowser.open("https://www.google.com/")

        PLAY_MUSIC = ["play music","start music","music please","music"]
        for phrase in PLAY_MUSIC:
            if phrase in query:
                speak("Playing...")             
                path="C:/Users/shankar/Desktop/python/jarvis/songs/"
                files=os.listdir(path)
                d=random.choice(files)
                os.startfile("C:/Users/shankar/Desktop/python/jarvis/songs/" + d)
            

        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        CODE = ["open code","i want to code","open visual studio code","code"]
        for phrase in CODE:
            if phrase in query:
                speak("Opening....")
                subprocess.Popen("C:/Users/shankar/AppData/Local/Programs/Microsoft VS Code/Code.exe")

        # elif 'email to vikranth' in query:
        #     try:
        #         speak("What Should i say?")
        #         takeCommand()
        #         to = "vikrantht32@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry i am not able to send this email")
        
        DATE = ["what is the date","date","what's the date today"]
        for phrase in DATE:
            if phrase in query:
                current_date = datetime.date.today()
                speak(f"Today's date is {current_date}")
                print(f"Today's date is {current_date}")
        
        NOTE_STRS = ["make a note", "write this down", "remember this"]
        for phrase in NOTE_STRS:
            if phrase in query:
                speak("What would you like me to write down?")
                note_text = takeCommand()
                note(note_text)
                speak("I've made a note of that.")

        PICTURE = ["analyse image","show me picture","picture","image"]
        for phrase in PICTURE:
            if phrase in query == PICTURE[1]:
                speak("Analysing..")
                show_image()
