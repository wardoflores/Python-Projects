#!/bin/zsh
# Description: Voice assistant that types out what you say.

# importing speech recognition package from google api
import speech_recognition as sr 
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import pyautogui as gui # To type out speech
import wolframalpha # to calculate strings into formula
# from selenium import webdriver # to control browser operations
# from selenium.webdriver.chrome.options import Options

def assistant_speaks(output):
    num = 1
  
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

assistant_speaks("What's your name, Human?")
name = get_audio()
assistant_speaks("Hello, " + name + '.')

while(1):

        assistant_speaks("Say 'type' plus the words you want to type.")
        text = get_audio().lower()

        if text == 0:
            continue

        if "type" in str(text):
            assistant_speaks(text)
            gui.typewrite(text[5:])


        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text) or "stop" in str(text):
            assistant_speaks("Ok bye, "+ name+'.')
            break

