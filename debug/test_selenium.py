from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.unitedstateszipcodes.org/20036/")

# Get the page source after JavaScript execution
html_content = driver.page_source
print(html_content)

# Close the browser
driver.quit()