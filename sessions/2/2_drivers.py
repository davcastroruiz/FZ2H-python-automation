# day of 2
''' Selenium supports automation of all the major browsers in the market through the use of WebDriver. 
WebDriver is an API and protocol that defines a language-neutral interface for controlling the behavior of web browsers. 

Each browser is backed by a specific WebDriver implementation, called a driver. 
The driver is the component responsible for delegating down to the browser, and handles communication to and from Selenium and the browser.

Selenium setup is quite different from the setup of other commercial tools. 
Before you can start writing Selenium code, you have to install the language bindings libraries for your language of choice, the browser you want to use, and the driver for that browser.

Today we want to install a few dependencies 
# pip install selenium
# pip install pandas
# pip install matplotlib
# pip install webdriver-manager
# '''

# (1) ---------- using the web driver manager to install the chrome driver --------
# Import WebDriver Manager for Python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Use install() to get the location used by the manager and pass it to the driver in a service class instance:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(2)
driver.quit()

# (2) ---------- using the hard coded location path -----------
'''
from selenium import webdriver
driver = webdriver.Chrome('/home/user/drivers/chromedriver')
'''

'''
Finding a single element with findElement*

driver.find_element(By.CLASS_NAME("className"));
driver.find_element(By.CSS_SELECTOR(".className"));
driver.find_element(By.ID("elementId"));
driver.find_element(By.LINK_TEXT("linkText"));
driver.find_element(By.NAME("elementName"));
driver.find_element(By.PARTIAL_LINK_TEXT("partialText"));
driver.find_element(By.TAG_NAME("elementTagName"));
driver.find_element(By.X_PATH("xPath"));

Finding a multiple elements with findElements*

driver.find_elements" ";
'''