#!/bin/zsh
# Adapted for Linux systems, still doesn't work for it though.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
import datetime
from datetime import datetime
import pyautogui
from crdntl import mail_address, passgoog

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Task Scheduler")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

titleframe = ttk.Frame(mainframe).grid(column=1, row=1, sticky=(N))
label = ttk.Label(titleframe, text='Task Scheduler').grid()

# Change the Meeting links every week, check for new links.

# Monday Tuesday

meetinglink1 = StringVar()
meetinglink1_entry = ttk.Entry(mainframe, width=7, textvariable=meetinglink1)
meetinglink1_entry.grid(column=2, row=1, sticky=(W, E))

meetinglink1 = "https://meet.google.com/byh-sezu-gnz"
meetinglink2 = "https://meet.google.com/hdi-yygo-sye"
meetinglink3 = "https://meet.google.com/amd-opoq-bwb"
meetinglink4 = "https://meet.google.com/hdi-yygo-sye"

# Wednesday Thursday
meetinglink5 = "https://meet.google.com/pai-bfzd-rdr"

# Wednesday
meetinglink6 = "https://meet.google.com/oow-njwy-oho"

# Thursday
meetinglink7 = "https://meet.google.com/sbk-jswq-rpm"

# Friday 
meetinglink8 = "https://meet.google.com/amd-opoq-bwb"

# Selenium Driver variables

CHROMEDRIVER_PATH = "/usr/bin/chromedriver"
brave_path = "/usr/share/applications/google-chrome.desktop"

opt = Options()
# opt = webdriver.ChromeOptions()
opt.binary_location = brave_path
# opt.add_argument("--incognito") OPTIONAL
# opt.add_argument("--headless") OPTIONAL
opt.add_argument('--start-maximized')
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-dev-shm-usage')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_experimental_option("prefs", {
  
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})

opt1 = Options()

opt1.binary_location = brave_path

# s=Service(ChromeDriverManager().install())

service = ChromeService(executable_path=CHROMEDRIVER_PATH)

driver = webdriver.Chrome(options=opt1) # service=service, options=opt

# driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

# driver = webdriver.Chrome(executable_path=bdriver_path, options=opt)

# Datetime Variables

hour_now_format = datetime.now().isoformat(timespec='hours')   
hour_now = str(hour_now_format[11:13])

min_now_format = datetime.now().isoformat(timespec='minutes')   
min_now = str(min_now_format[14:16])

# Google Meet Functions

def Glogin(mail, pswrd):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
  
    # input Gmail
    driver.implicitly_wait(10)
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
  
    # input Password
    driver.implicitly_wait(10)
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(passgoog)
    driver.find_element_by_id("passwordNext").click()
  
    # go to google home page to keep login Wheen redirected to Meet.
    driver.get('https://google.com/')
    pyautogui.press("F11")

# explicit function to turn off mic and cam
def turnOffMicCam():
  
    # turn off Microphone
    driver.implicitly_wait(10)
    pyautogui.keyDown('ctrl') # hold ctrl key
    pyautogui.press('d') # press d key
    pyautogui.keyUp('ctrl') # release ctrl key
    # driver.find_element_by_xpath( 
    #     '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
  
    # turn off camera
    pyautogui.keyDown('ctrl') # hold ctrl key
    pyautogui.press('e') # press e key
    pyautogui.keyUp('ctrl') # release ctrl key
    # driver.find_element_by_xpath(
    #     '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()

def AskToJoin():
    # Ask to Join meet
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    # Ask to join and join now buttons have same xpaths

def joinNow():
    # Join meet
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

def closing():

    closeprompt = pyautogui.confirm(text="Click Ok to end session.", title="End session?", buttons=['OK', 'Cancel'])

    if closeprompt == "OK":
        close = driver.close()
        close
        pyautogui.alert(text="Bye! Have a nice day!", title="Session ended.")
    elif closeprompt == "Cancel":
        return closeprompt
    else:
        pass

def first_mon_sub():
    if datetime.today().weekday() == 0: # Monday
        if hour_now == "08" or hour_now == "09": # 8am to 10am
            Glogin(mail_address, passgoog)
            driver.get(meetinglink1)
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        if hour_now == "10" or hour_now == "11": # 10am - 12:00pm
            Glogin(mail_address, passgoog)
            driver.get(meetinglink2)
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        if hour_now == "13" or hour_now == "14" and min_now <= "29": # 1:30pm - 2:30pm
            Glogin(mail_address, passgoog)
            driver.get(meetinglink3) 
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        if hour_now == "14" and min_now >= "30" or hour_now == "15" or hour_now == "16" and min_now <= "30": # 2:30pm - 4:30pm
            Glogin(mail_address, passgoog)
            driver.get(meetinglink4)
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        else:
            driver.close()
            return pyautogui.alert(text="Bye! Have a nice day!", title="No sessions for now.")

def first_tue_sub():
    if datetime.today().weekday() == 1: # Tuesday
        if hour_now == "08" or hour_now == "09": # 8am to 10am
            Glogin(mail_address, passgoog)
            driver.get(meetinglink1)
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        if hour_now == "10" or hour_now == "11": # 10am - 12:00pm
            Glogin(mail_address, passgoog)
            driver.get(meetinglink2)
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        if hour_now == "13" or hour_now == "14" and min_now <= "29": # 1:30pm - 2:30pm
            Glogin(mail_address, passgoog)
            driver.get(meetinglink3)
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        if hour_now == "14" and min_now >= "30" or hour_now == "15" or hour_now == "16" and min_now <= "30": # 2:30pm - 4:30pm
            Glogin(mail_address, passgoog)
            driver.get(meetinglink4)
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        else:
            driver.close()
            return pyautogui.alert(text="Bye! Have a nice day!", title="No sessions for now.")

def first_wed_sub():
    if datetime.today().weekday() == 2: # Wednesday
        if hour_now == "08": # 8am - 9am
            Glogin(mail_address, passgoog)
            driver.get(meetinglink6)
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        if hour_now == "12": # 12:30pm
            Glogin(mail_address, passgoog)
            driver.get(meetinglink5)
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        else:
            driver.close()
            return pyautogui.alert(text="Bye! Have a nice day!", title="No sessions for now.")

def first_thur_sub():
    if datetime.today().weekday() == 3: # Thursday
        if hour_now == "14" or hour_now == "15" or hour_now == "16": # 2:30pm to 4:30pm
            Glogin(mail_address, passgoog)
            driver.get(meetinglink7)
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        else:
            driver.close()
            return pyautogui.alert(text="Bye! Have a nice day!", title="No sessions for now.")

def first_fri_sub():
    if datetime.today().weekday() == 4: # Friday
        if hour_now == "08" or hour_now == "09": # 8am to 10pm
            Glogin(mail_address, passgoog)
            driver.get(meetinglink8)
            turnOffMicCam()
            AskToJoin()
            # joinNow()
            closing()
        else:
            driver.close()
            return pyautogui.alert(text="Bye! Have a nice day!", title="No sessions for now.")

first_mon_sub()
first_tue_sub()
first_wed_sub()
first_thur_sub()
first_fri_sub()