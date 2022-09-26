import pyttsx3
import datetime
import webbrowser
import wikipedia 
import os
import speech_recognition as sr
import smtplib
 

dic={"tushar":"gmail@gmail.com"}
engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def sendEmail(to, content):     #to send email 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gmail@gmail.com', 'Password')#enter password
    server.sendmail('gmail@gmail.com', to, content)
    server.close()

def wishme():
 
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<=12:
      speak(" Hello sir Good morning ")
  elif hour>=12 and hour<=18:
      speak(" Hello sir Good afternoon ")
  else:
      speak(" Hello sir Good evening ")   

  speak("I am SIRI . please tell how may i help you  ")     
def speak(audio):

  engine.say(audio) 

  engine.runAndWait() #Without this command, speech will not be audible to us.

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "nonee" #None string will be returned
    return query
 
if __name__ == "__main__":
    
    wishme()
    query = takeCommand().lower() #Converting user query into lower case
    while "exit" not in query:
    # if 1:
       # query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            
              #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            url="youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            webbrowser.get(chrome_path).open(url)   
        elif 'open google' in query:
            url="google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play music' in query:
            music_dir = 'E:\VS code\songs'
            songs = os.listdir(music_dir)
            print(songs)   
            speak("which song do you want to listen sir") 
            n=takeCommand().lower()
            song=n+".mp3"
            print(song)
            if song in songs:
             indexo=songs.index(song)   
             os.startfile(os.path.join(music_dir, songs[indexo]))
             speak(f"playing.... {songs[indexo]}\n")  
            else:
                
             speak("sorry sir, i could not find this song")    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")      
        elif 'open visual code' in query:
            codePath = "C:\\Users\\Tushar Sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    
        elif ('open chrome' in query) or ('open google chrome' in query):
            codePath ="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath) 
        elif ('send email' in query) :
            try:
                speak("whom i have to send mail?")
                namae= takeCommand().lower()
                if namae in dic.keys():
                 to=dic[namae]
                 speak("What should I say?")
                 content = takeCommand()
                 # make sure your less secure apps gmail is on    
                 sendEmail(to, content)
                 speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")    

        elif ("who are you" in query) or ("who is this" in query) or ("created you" in query) or ("created siri" in query) or ("programed" in query) or ("invented" in query):
            speak("I am Siri,   a Destop assisstant created by Tushar Sharma ")               
        
        elif "open whatsapp" in query :
            url="web.whatsapp.com/"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        if "nonee" in query :  

          #speak("sir what do you want next .") 
           query = takeCommand().lower() #Converting user query into lower case
        else:
            speak("sir what do you want next .")
            query = takeCommand().lower() #Converting user query into lower case
            
    else:
     speak("ok Sir,  Thanks for your efforts")        
     
