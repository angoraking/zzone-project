# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))
display.start()
chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
options = [
    # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors"

    # "--headless",
    # "--disable-gpu",
    # "--window-size=1920,1200",
    # "--ignore-certificate-errors",
    # "--disable-extensions",
    # "--no-sandbox",
    # "--disable-dev-shm-usage",
    # '--remote-debugging-port=9222'
]
for option in options:
    chrome_options.add_argument(option)


# Create a new instance of the Chrome driver
# I tried, the headless driver doesn't work
driver = webdriver.Chrome(options = chrome_options)

# Navigate to the website
driver.get("https://www.unitedstateszipcodes.org/20036/")

# Get the page source after JavaScript execution
html_content = driver.page_source
print(html_content)

# Close the browser
driver.quit()
