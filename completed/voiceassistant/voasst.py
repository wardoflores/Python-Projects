#! python3
# Description: Voice Assistant that could search the web and query Wolfram Alpha.

# importing speech recognition package from google api
import speech_recognition as sr 
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
from selenium.webdriver.chrome.options import Options
from threading import Thread

num = 1
def assistant_speaks(output):
    global num
  
    # num to rename every audio file 
    # with different name to remove ambiguity
    num += 1
    print("voasst : ", output)
  
    toSpeak = gTTS(text = output, lang ='en', slow = False)
    # saving the audio file given by google text to speech
    file = str(num)+".mp3"
    toSpeak.save(file)
      
    # playsound package is used to play the same file.
    playsound.playsound(file, True) 
    os.remove(file)
  
  
  
def get_audio():
  
    rObject = sr.Recognizer()
    audio = ''
  
    with sr.Microphone() as source:
        print("Speak...")
          
        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit = 5)
    print("Stop.") # limit 5 secs
  
    try:

        text = rObject.recognize_google(audio, language ='en-US')
        print("You : ", text)
        return text
  
    except:

        assistant_speaks("Could not understand your audio, please try again!")

        with sr.Microphone() as source:
            print("Speak...")
            
            # recording the audio using speech recognition
            audio = rObject.listen(source, phrase_time_limit = 5)
            print("Stop.") # limit 5 secs

        text = rObject.recognize_google(audio, language ='en-US')
        return text

def search_web(input):

    driver_path = r"C:\webdriver\chromedriver.exe"
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    opt = Options()
    opt.binary_location = brave_path
    # opt.add_argument("--incognito") OPTIONAL
    # opt.add_argument("--headless") OPTIONAL
    opt.add_argument('--start-maximized')
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt.add_argument('--disable-blink-features=AutomationControlled')
  
    driver = webdriver.Chrome(executable_path=driver_path, options=opt)
    driver.implicitly_wait(1)

  
    if 'youtube' in input.lower():
  
        assistant_speaks("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():
  
        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return
  
    else:
  
        if 'google' in input:
  
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))
  
        elif 'search' in input:
  
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))
  
        else:
  
            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))
  
        return
  
  
# function used to open application present inside the system.
def open_application(input):
  
    if "brave" in input:
        assistant_speaks("Brave browser")
        os.startfile(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
        return
  
    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile(r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE")
        return
  
    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile(r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE")
        return
  
    else:
  
        assistant_speaks("Application not available")
        return


def process_text(input):
    try:
        if 'search' in input or 'play' in input:
            # a basic web crawler using selenium
            search_web(input)
            return
  
        elif "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am Voasst. Your personal Assistant.
            I am here to make your life easier. You can command me to perform
            various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak)
            return
  
        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Eduardo Flores."
            assistant_speaks(speak)
            return
  
        elif "calculate" in input.lower():
              
            # write your wolframalpha app_id here
            app_id = "WOLFRAMALPHA_APP_ID" 
            client = wolframalpha.Client(app_id)
  
            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return
  
        elif 'open' in input:
              
            # another function to open 
            # different application availaible
            open_application(input.lower()) 
            return
  
        else:
  
            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except :
  
        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)
  
# Driver Code
def active_process():
    if __name__ == "__main__":
        assistant_speaks("What's your name, Human?")
        # name ='Human'
        name = get_audio()
        assistant_speaks("Hello, " + name + '.')
        
        while(1):

            assistant_speaks("What can i do for you?")
            
            text = get_audio().lower()

            if text == 0:
                continue

            if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text) or "stop" in str(text):
                assistant_speaks("Ok bye, "+ name+'.')
                break

            # calling process text to process the query
            process_text(text)

Thread(target=active_process).start()




