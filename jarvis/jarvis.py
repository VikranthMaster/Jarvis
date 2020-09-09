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
from playsound import playsound
import time

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
        speak("Recognizing...")  
        print("Recognizing...")  
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        print("Say that again please")
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
    img = cv2.imread("Photos/space.jpg")
    cv2.imshow("Space Image",img)
    cv2.waitKey(0)

def video():
    cap = cv2.VideoCapture(1)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

    playsound('Music/Bomb Timer.mp3')
  
  
# input time in seconds 
t = speak(input("Enter the time in seconds: "))



if __name__ == "__main__":
    wishMe()

    while True:
    # if 1:
        query = takeCommand().lower()

        WHO = ["who are you","what are you"]
        for phrase in WHO:
            if phrase in query:
                playsound("Music/kill bill pandey.mp3")
                pass

        WIKIPEDIA = ["wikipedia","who","what"]
        for phrase in WIKIPEDIA:
            if phrase in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

        YOUTUBE = ["open youtube","i want to watch videos","i want to watch movies","open YouTube"]
        for phrase in YOUTUBE:
            if phrase in query:
                    webbrowser.open("https://www.youtube.com/")

        GOOGLE = ["open google","search","open Google"]
        for phrase in GOOGLE:
            if phrase in query:
                webbrowser.open("https://www.google.com/")

        NEVERSKIP = ["open neverskip","neverskip"]
        for phrase in NEVERSKIP:
            if phrase in query:
                webbrowser.open("https://parent.neverskip.com/#/auth/login")

        PLAY_MUSIC = ["play music","start music","music please","music"]
        for phrase in PLAY_MUSIC:
            if phrase in query:
                speak("Playing...")             
                path="C:/Users/TS/Music/telugu songs/"
                files=os.listdir(path)
                d=random.choice(files)
                os.startfile(path + d)
            
        TIME = ["what is the time","time"]
        for phrase in TIME:
            if phrase in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"The time is {strTime}")

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
            if phrase in query:
                speak("Analysing..")
                show_image()

        VIDEO = ["open camera","analyse video","video"]
        for phrase in VIDEO:
            if phrase in query:
                speak("Analysing..")
                video()

        STOP = ["stop","break"]
        for phrase in STOP:
            if phrase in query:
                break
                speak("Shutting....")

        COMMAND = ["open command prompt","open cmd"]
        for phrase in COMMAND:
            if phrase in query:
                subprocess.Popen(["cmd.exe"])

        TIMER = ["set a timer","start the countdown","timer"]
        for phrase in TIMER:
            if phrase in query:
                countdown(int(t))
