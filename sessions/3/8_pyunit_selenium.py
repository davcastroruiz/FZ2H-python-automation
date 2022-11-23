# session 3

from selenium import webdriver
import datetime
from time import sleep
import unittest
from selenium.webdriver.common.by import By
import xmlrunner


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(20)
        print('-------- Test Env for Selenium created ---------')
        print('Test started at %s' %str(datetime.datetime.now()))

    def testA(self):
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        sleep(5)
        print(self.driver.title)
        text_box = self.driver.find_element(by=By.NAME, value="my-text")
        submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="button")
        text_box.send_keys("Selenium")
        submit_button.click()
        sleep(5)
        self.driver.get_screenshot_as_file('evidence.png')

    def tearDown(self):
        """Call after every test case."""
        if self.driver != None:
            print('-------- Test Env will be destroy ---------')
            self.driver.close()
            self.driver.quit()
  
if __name__ == "__main__":
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)