from selenium import webdriver
import time

driver_path = r"C:\webdriver\chromedriver.exe"
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

opt = Options()
opt.binary_location = brave_path
# opt.add_argument("--incognito") OPTIONAL
# opt.add_argument("--headless") OPTIONAL
opt.add_argument('--start-maximized')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
opt.add_argument('--disable-blink-features=AutomationControlled')

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, options=opt)

browser.get("https://www.google.com")

time.sleep(2)

browser.close()