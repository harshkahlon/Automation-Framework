import unittest
from appium import webdriver
import time

class desktopPOC(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps["app"] = r"C:\Windows\notepad.exe"
        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", desired_capabilities=desired_caps)

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_initialize(self):
        dataadmin = self.driver.find_element_by_name("File")
        dataadmin.click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name("Text Editor").click()
        self.driver.find_element_by_name("Text Editor").send_keys("Desktop Automation test for Notepad")
        time.sleep(2)
        self.driver.find_element_by_name("Close").click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("CommandButton_7").click()

        time.sleep(2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(desktopPOC)
    unittest.TextTestRunner(verbosity=2).run(suite)


