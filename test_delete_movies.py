from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_untitled(self):
        try:
            driver = self.driver
            driver.get(self.base_url + "/php4dvd/")
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys("admin")
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys("admin")
            driver.find_element_by_name("submit").click()
            driver.find_element_by_css_selector("div.nocover").click()
            time.sleep(1)
            driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
            self.assertRegex(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
        except Exception as e:
            print(type(e))
            print(e.msg)







    def is_alert_present(self):
        try: self.driver.switch_to.alert
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    i = 0
    print('1')
    unittest.main()
