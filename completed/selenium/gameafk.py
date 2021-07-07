import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_path = r"C:\webdriver\chromedriver.exe"
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

opt = Options()
opt.binary_location = brave_path
# opt.add_argument("--incognito") OPTIONAL
# opt.add_argument("--headless") OPTIONAL
opt.add_argument('--start-maximized')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])
opt.add_argument('--disable-blink-features=AutomationControlled')

# Create new Instance of Brave
driver = webdriver.Chrome(executable_path=driver_path, options=opt)

# driver.get("https://www. .com")
driver.get("https://www.gamesite.com")

time.sleep(1)
driver.find_element_by_xpath(
    'PUT XPATH HERE').click()
driver.implicitly_wait(3000)
time.sleep(1)
driver.find_element_by_xpath(
    'PUT XPATH HERE').click()
driver.implicitly_wait(3000)
time.sleep(1)
driver.find_element_by_xpath(
    'PUT XPATH HERE').click()
driver.implicitly_wait(3000)
time.sleep(1)
driver.find_element_by_xpath(
    'PUT XPATH HERE').click()
driver.implicitly_wait(3000)
time.sleep(1)
driver.find_element_by_xpath(
    'PUT XPATH HERE').click()
driver.implicitly_wait(3000)