#!/bin/zsh
# Meet automation for Windows.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
from datetime import datetime
import pyautogui
from crdntl import mail_address, passgoog
 
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver_path = r"C:\webdriver\chromedriver.exe"
 
opt = Options()
opt.binary_location = brave_path
# opt.add_argument("--incognito") OPTIONAL
# opt.add_argument("--headless") OPTIONAL
opt.add_argument('--start-maximized')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_experimental_option("prefs", {
  
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
 
driver = webdriver.Chrome(executable_path=driver_path, options=opt)
 
hour_now_format = datetime.now().isoformat(timespec='hours')   
hour_now = str(hour_now_format[11:13])
 
min_now_format = datetime.now().isoformat(timespec='minutes')   
min_now = str(min_now_format[14:16])
print("min now is: " + min_now)
 
def Glogin(mail, pswrd):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
  
    # input Gmail
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)
  
    # input Password
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(passgoog)
    driver.implicitly_wait(10)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(10)
  
    # go to google home page
    driver.get('https://google.com/')
    driver.implicitly_wait(100)
 
# explicit function to turn off mic and cam
def turnOffMicCam():
  
    # turn off Microphone
    time.sleep(2)
    pyautogui.keyDown('ctrl') # hold ctrl key
    pyautogui.press('d') # press s key
    pyautogui.keyUp('ctrl') # release ctrl key
    # driver.find_element_by_xpath( 
    #     '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.implicitly_wait(3000)
  
    # turn off camera
    time.sleep(1)
    pyautogui.keyDown('ctrl') # hold ctrl key
    pyautogui.press('e') # press s key
    pyautogui.keyUp('ctrl') # release ctrl key
    # driver.find_element_by_xpath(
    #     '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.implicitly_wait(3000)
 
def AskToJoin():
    # Ask to Join meet
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    # Ask to join and join now buttons have same xpaths
 
def joinNow():
    # Join meet
    print("...Joined Session!")
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
 
def closing():
    close = driver.close()
 
    closeprompt = pyautogui.confirm(buttons="OK, cancel")
 
    if closeprompt == "OK":
        close
    else:
        pass
 
# login to Google account
Glogin(mail_address, passgoog)
 
# If code is not constant,
# Prompt asks for meeting link (practice link: https://meet.google.com/xby-zehb-ncf)
 
# TODO: Automate scraping for meeting room code,
#  script a link scraper and append link here.
 
# pyautogui.locateOnScreen('meetingcode.png', region=(0,0,0,0))
# pyautogui.doubleClick()
# pyautogui.hotkey()
# pyautogui.typewrite() paste into input prompt
 
# If code is constant,
# Comment 1st meetinglink variable, and uncomment 2nd meetinglink variable.
 
# meetinglink = pyautogui.prompt(title="Google meet automation", text="Input meeting link:")
 
meetinglink1 = "https://meet.google.com/ojc-ykmb-wph" # Monday Tuesday
meetinglink2 = "https://meet.google.com/hdi-yygo-sye" # Monday Tuesday
meetinglink3 = "https://meet.google.com/amd-opoq-bwb" # Monday Tuesday
meetinglink4 = "https://meet.google.com/hdi-yygo-sye" # Monday Tuesday
 
meetinglink5 = "https://meet.google.com/pai-bfzd-rdr" # Wednesday Thursday
 
meetinglink6 = "https://meet.google.com/oow-njwy-oho" # Wednesday
 
meetinglink7 = "https://meet.google.com/sbk-jswq-rpm" # Thursday
 
meetinglink8 = "https://meet.google.com/amd-opoq-bwb" # Friday
 
def first_mon_sub():
    if datetime.today().weekday() == 0: # Monday
        if hour_now == "08": # 8am
            driver.get(meetinglink1) # 8am to 10am
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
        if hour_now == "10": # 10am - 12:00pm
            driver.get(meetinglink2)
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
        if hour_now == "13": # 1:30pm - 2:30pm
            driver.get(meetinglink3) 
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
        if hour_now == "14": # 2:30pm - 4:30pm
            driver.get(meetinglink4)
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
 
def first_tue_sub():
    if datetime.today().weekday() == 1: # Tuesday
         if hour_now == "08": # 8am to 10am
            driver.get(meetinglink1)
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
         if hour_now == "10": # 10am - 12:00pm
            driver.get(meetinglink2)
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
         if hour_now == "13": # 1:30pm - 2:30pm
            driver.get(meetinglink3)
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
         if hour_now == "14": # 2:30pm - 4:30pm
            driver.get(meetinglink4)
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
 
def first_wed_sub():
    if datetime.today().weekday() == 2: # Wednesday
         if hour_now == "08": # 8am - 9am
            driver.get(meetinglink6)
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
         if hour_now == "08": # 12:30pm
            driver.get(meetinglink5)
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
 
def first_thur_sub():
    if datetime.today().weekday() == 3: # Thursday
         if hour_now == "14": # 2:30pm to 4:30pm
            driver.get(meetinglink7)
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
 
def first_fri_sub():
    if datetime.today().weekday() == 4: # Friday
         if hour_now == "08": # 8am to 10pm
            driver.get(meetinglink8)
            turnOffMicCam()
            AskToJoin()
            joinNow()
            closing()
 
first_mon_sub()
first_tue_sub()
first_wed_sub()
first_thur_sub()
first_fri_sub()
