import time
from random import randint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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

def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.01)

scam_site = 'https://commerzbank-phototan-89fz0.web.app/'
FIRST_NAMES = ["Anna", "Bella", "Christopher", "Denis", "Emily", "Fred", "Gino", "Lukas", "Julian", "Isabelle", "Jonas"]
LAST_NAMES = ["Axel", "Born", "Callen", "Doritus", "Evans", "Feldmann", "Schmidt", "Scheider", "Fischer", "Meyer", "Hofmann"]
MOBILE_PRE = ["01520", "01522", "01523", "01525", "0162", "0172", "0173"]
EMAIL_PROVIDERS = ["gmail.com", "web.de", "gmx.de", "hotmail.de"]

def rand_select(array):
    return array[randint(0, len(array)-1)]

def generate_random_number(num):
    random_user = ""
    for i in range(num):
        random_user = random_user + str(randint(0,9))
    return random_user

def generate_birth_day():
    day = str(randint(1, 9)).zfill(2)
    month = str(randint(1, 9)).zfill(2)
    year = str(randint(1950, 2000))
    return day+month+year

def gererate_phone():
    return rand_select(MOBILE_PRE) + "/"+ generate_random_number(randint(8,12))

def generate_email(fname, lname):
    return fname + "." + lname + "@" + rand_select(EMAIL_PROVIDERS)


while(True):
    try:
        driver = webdriver.Chrome(executable_path=driver_path, options=opt)
        driver.get(scam_site)
        time.sleep(1)


        ### First page - Login
        user = driver.find_element_by_id('teilnehmer')
        slow_typing(user, generate_random_number(8))
        pin = driver.find_element_by_id('pin')
        slow_typing(pin, generate_random_number(6))
        login_button = driver.find_element_by_id('loginLoaderText')
        login_button.click()

        time.sleep(1.0)

        ### Second page - Personal info
        first_name = driver.find_element_by_id('param4')
        fname = rand_select(FIRST_NAMES)
        slow_typing(first_name, fname)

        last_name = driver.find_element_by_id('param5')
        lname = rand_select(LAST_NAMES)
        slow_typing(last_name, lname)

        birth_date = driver.find_element_by_id('param6')
        bday = generate_birth_day()
        ActionChains(driver).move_to_element(birth_date).click().send_keys(bday).perform()

        phone = driver.find_element_by_id('param7')
        slow_typing(phone, gererate_phone())

        email = driver.find_element_by_id('param8')
        slow_typing(email, generate_email(fname, lname))

        login_button = driver.find_element_by_id('loginLoaderText')
        login_button.click()

        time.sleep(2.0)

        ### Third page - Upload image
        choose_file = driver.find_element_by_id("file")
        if randint(2,3) == 1:
            choose_file.send_keys(f"/home/konartist/Desktop/projects/commerz_scam/phototan1.jpg")
            time.sleep(15.0)
        else:
            choose_file.send_keys(f"/home/konartist/Desktop/projects/commerz_scam/phototan2.png")
            time.sleep(3.0)

        login_button = driver.find_element_by_id('loginLoaderText')
        login_button.click()

        time.sleep(2.0)

        driver.quit()
    except:
        print("Warning something went wrong")
        driver.quit()
