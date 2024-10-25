import time
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipediaapi
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listering...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

#To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir. please tell me how can i help you")


#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ashupatil2144@gmail.com','voiw axgg hblr tpbc')
    server.sendmail('ashupatil2144@gmail.com',to,content)
    server.close()


#to read pdf
#def pdf_reader():
 #   book = open('jarvis report (1) (3).pdf', 'rb')
  #  pdfReader = PyPDF2.PdfFileReader(book)
   # pages = pdfReader.numPages
    #speak(f"Total number of pages in this book: {pages}")
    #speak("Sir, please enter the page number I have to read.")
    #pg = int(input("Please enter the page number: "))

#    if 0 <= pg < pages:  # Ensure the page number is valid
 #       page = pdfReader.getPage(pg)
      #  text = page.extractText()
  #    speak(text)
   # else:
    #    speak("Sorry, that page number is out of range.")
    #book.close() # Don't forget to close the file
   # if some_condition:  # Replace with your actual condition
    #    pdf_reader()


if __name__ =="__main__":
    wish()
    while True:
    #if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir =music_dir = r'C:\Users\ASHISH\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP addtess is {ip}")


                    # Initialize the Wikipedia API with a user agent
            user_agent = "YourBot/1.0 (http://yourwebsite.com; yourname@example.com)"
            wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI,
            user_agent=user_agent
                )

            # Initialize the text-to-speech engine
            engine = pyttsx3.init()

            # Example query
            query = "Python (programming language)"
            #query ="google"
            page = wiki_wiki.page(query)

            if page.exists():
                summary = page.summary[:200]  # Get the first 200 characters
                print("Summary:", summary)  # Print the summary
                engine.say(summary)  # Speak the summary
                engine.runAndWait()  # Wait for the speaking to finish
            else:
                print("Page not found.")
                engine.say("Sorry, I couldn't find any information on that topic.")
                engine.runAndWait()  # Wait for the speaking to finish


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open amazon" in query:
            webbrowser.open("www.amazon.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message to ashish" in query:

            now = datetime.datetime.now()
            kit.sendwhatmsg("+918591060961", "this is testing protocol", now.hour, now.minute + 1)

        elif "send message to sakshi" in query:

            now = datetime.datetime.now()
            kit.sendwhatmsg("+919146023909", "what are you doing", now.hour, now.minute + 1)

        elif "send message to kritika" in query:

            now = datetime.datetime.now()
            kit.sendwhatmsg("+917039417717", "you are cute", now.hour, now.minute + 1)

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")

        elif "email to sairaj" in query:
            try:
                speak("What should I say?")
                content = takecommand().lower()
                to = "sairajvichare876@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to Aashish")

            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this mail to Ashish.")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

#to close any application
        elif "close notepad" in query:
           speak("okay sir, closing notepad")
           os.system("taskkill /f /im notepad.exe")

        elif "close command prompt" in query:
           speak("okay sir, closing command prompt")
           os.system("TASKKILL /IM cmd.exe /F")

        elif "close camera" in query:
           speak("okay sir, closing camera")
           os.system("TASKKILL /IM camera.exe /F")


#to find a joke
        elif "tell me a joke" in query:

            joke = pyjokes.get_joke()
            speak(joke)

        elif "Another joke" in query:

            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rund1132.exe powrprof.dil,SetsuspendState 0,1,0")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "where i am" in query or "where we are" in query:
            speak("wait sir,let me check")
            try:
                ipAdd ='49.32.150.70'
                print(ipAdd)
                url = f'https://get.geojs.io/v1/ip/geo/{ipAdd}.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure,but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are.")
                pass
        speak("sir,do you have any other work")




