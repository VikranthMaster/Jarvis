import cv2
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from email.message import EmailMessage
import subprocess
import pygame
from playsound import playsound
import time
import yt_dlp

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
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)        
        cv2.imshow("Face Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

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
  
  
def get_video_url(song_name):
    ydl_opts = {
        'quiet': True,  # Suppress output
        'extract_flat': True,  # Only get video URL without downloading
        'force_generic_extractor': True,  # Use generic extractor
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(f"ytsearch:{song_name}", download=False)
        if 'entries' in result:
            video_url = result['entries'][0]['url']  # Get the URL of the first result
            return video_url
        return None

def playmusic(query):
    url = get_video_url(query)
    os.system(f"yt-dlp -f bestaudio -o - {url} | ffplay -nodisp -autoexit -loglevel quiet -")
    
    


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        WHO = ["who are you","what are you"]
        for phrase in WHO:
            if phrase in query:
                pygame.mixer.init()
                pygame.mixer.music.load("kill_bill_pandey.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

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
            
        TIME = ["what is the time","time"]
        for phrase in TIME:
            if phrase in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"The time is {strTime}")

        CODE = ["open code","i want to code","open visual studio code","code"]
        for phrase in CODE:
            if phrase in query:
                speak("Opening....")
                os.system("code")

        
        EMAIL = ["email", "mail someone","mail"]
        for phrase in EMAIL:
            if phrase in query:
                speak("Whom do you want to send email")
                name = input("Enter email: ")
                speak("What do you want me to send")
                content = takeCommand()
                msg = EmailMessage()
                msg["Subject"] = "Email Python Bot"
                msg["From"] = "greninjaa90@gmail.com"
                msg["To"] = name
                msg.set_content(content)
                
                smtp_server = 'smtp.gmail.com'
                smtp_port = 587
                email = "greninjaa90@gmail.com"
                app_pass = "subd gvqz samk ffuu"

                try:
                    with smtplib.SMTP(smtp_server, smtp_port) as server:
                        server.starttls()
                        server.login(email, app_pass)
                        server.send_message(msg)

                    speak("Message sent successfully")
                    continue
                except:
                    speak("Sorry there was problem in sending..Try again")
        
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
                speak("Shutting....")
                break

        COMMAND = ["open command","open cmd"]
        for phrase in COMMAND:
            if phrase in query:
                subprocess.Popen(["cmd.exe"])

        TIMER = ["set a timer","start the countdown","timer"]
        for phrase in TIMER:
            if phrase in query:
                speak("Enter time")
                t = takeCommand()
                countdown(int(t))
                
        SONGS = ["play music","start music","music please","music", "play song","song"]
        for phrase in SONGS:
            if phrase in query:
                speak("which song do you want me to play sir")
                content = takeCommand()
                playmusic(content)
                continue
