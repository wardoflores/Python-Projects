import os
import pyautogui
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech

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

while True:
    
    try:

        text = pyautogui.prompt(title="Text to Speech", text="Add text here: ")

        assistant_speaks(text)

    except AssertionError:

        exit()


