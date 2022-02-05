#!/bin/zsh
# Source: https://chromedriver.chromium.org/getting-started

# --- test 1

import time

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

options = Options()

options.binary_location = "/usr/share/applications/google-chrome.google-chrome.desktop"

driver = webdriver.Chrome() # '/usr/bin/chromedriver' # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()

# --- test 2

# import time

# from selenium import webdriver

# from selenium.webdriver.chrome.service import Service

# ChromeOptions options = new ChromeOptions();

# options.setBinary("/path/to/other/chrome/binary");

# service = Service('/home/joey/Drivers/chromedriver')

# service.start()

# driver = webdriver.Remote(service.service_url)

# driver.get('http://www.google.com/');

# time.sleep(5) # Let the user actually see something!

# driver.quit()

# --- test 3

# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("http://www.google.com")
# print(driver.page_source.encode('utf-8'))
# driver.quit()

# --- test 4

# DefaultSelenium selenium = new DefaultSelenium("localhost", 4444, "*custom path/to/chromium" , "www.google.com");
# selenium.start();