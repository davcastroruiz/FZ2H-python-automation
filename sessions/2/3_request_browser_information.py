'''
There are a bunch of types of information about the browser you can request, including window handles, browser size / position, cookies, alerts, etc.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1) start a session
driver = webdriver.Chrome()

# 2) I have a browser, now what?
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 3) request browser information
title = driver.title
assert title == "Web form"

# 4) sometimes we would like to wait a few seconds, so let's use a waiting strategy to wait the sync the code.
driver.implicitly_wait(0.5)

# 5) find element
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# 6) I have my elements, what's next?
text_box.send_keys("Selenium")
submit_button.click()

# 7) request element information
message = driver.find_element(by=By.ID, value="message")
value = message.text
assert value == "Received!"

# 8) finish your session!!
driver.quit()
