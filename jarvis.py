import pyttsx3  # It is a text-to-speech conversion library in Python. it works offline. 
import speech_recognition as sr # module import to recognise & translate speech-text & text-speech.
import datetime
import wikipedia
import webbrowser
import random
import os
import smtplib

engine = pyttsx3.init('sapi5')  # sapi5 is an API developed to allow speech recognition & synthesis within windows application.
voices = engine.getProperty('voices') # gets the current value of an engine property. 
# print(voices)
engine.setProperty('voice',voices[0].id) # here voice is a property and we have set its value as voices[0].id. 
# print(voices[0].id)

def speak(audio):
    engine.say(audio) # Queues a command to speak text according to what properties were set above the command.
    engine.runAndWait() # Blocks while processing all the currently queued commands.

def wishMe():
    
    # hr = datetime.datetime.now()  
    # print(hr)

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!! Wake Up.")
    elif hour >= 12 and hour < 17:
        speak("Good Noon!! Complete Your Daily Targets")
    elif hour >= 17 and hour < 18 :
        speak("Good Evening !! Have Your Snacks")
    else:
        speak("Good Night !! Let's Sleep")
    speak(" Your Desktop Assistant is Here!! How May I Help You? ")

def takeCommand():
    
    # It takes microphone input from user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening To Audio...")
        r.pause_threshold = 1        # press Ctrl and click to check other parameters and know about them.
        r.energy_threshold = 100
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("code.achalesh@gmail.com",password)
    server.sendmail("code.achalesh@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    # speak("Hello Ji, What's Up")
    wishMe()
    # takeCommand()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on input query
        if "wikipedia" in query:
            speak("Searching Wikipedia....")
            speak("Please Wait !!")
            query = query.replace("wikipedia","",1)
            results = wikipedia.summary(query, sentences = 3)
            speak("According To Wikipedia")
            print(results)
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")
        
        elif "open github" in query:
            webbrowser.get("google-chrome").open("github.com")

        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")
        
        elif "open linkedin" in query:
            webbrowser.open("linkedin.com")
        
        elif "open ram" in query:
            webbrowser.open("https://www.rakshatpa.com/")

        elif "play music" in query:
            music_dir = "C:\\Users\\Achalesh Lakhotiya\\Desktop\\Music"
            songs = os.listdir(music_dir)
            song = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_dir,song))
        
        elif "open vs code" in query:
            codepath = "C:\\Users\\Achalesh Lakhotiya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"It's {strTime} right now")
            print(strTime)
            
        elif "mail" in query:
            try:
                speak("What should I convey ?")
                content = takeCommand()
                to = "dars2427@gmail.com"
                speak("Enter password")
                password = str(input("Enter password: \n"))
                sendEmail(to, content,password)
                speak(" Your Email has been successfully delivered.")
                print("Your Email has been successfully delivered.")
            except:
                speak("Sorry, Email can't delivered.")
                
        elif "quit" in query:
            speak(" Thanks for accessing service! Have a good day.")
            exit()
