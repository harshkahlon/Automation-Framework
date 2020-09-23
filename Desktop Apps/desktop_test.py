import unittest
from appium import webdriver
import time

class desktopPOC(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps["app"] = r"C:\Users\Hkahlon\Desktop\340B app\340b Ref2\WP340BStart.exe"
        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", desired_capabilities=desired_caps)

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_initialize(self):
        dataadmin = self.driver.find_element_by_name("Data Admin")
        dataadmin.click()
        time.sleep(2)
        self.driver.find_element_by_name("Agreement").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name("Enter date").click()
        # self.driver.find_element_by_name("Enter date").send_keys("1/1/2020")
        self.driver.find_element_by_name("PART_DropDownButton").click()
        self.driver.find_element_by_name("1").click()
        # webdriver.RemoteWebElement element = session.FindElementByName("Document1")
        time.sleep(2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(desktopPOC)
    unittest.TextTestRunner(verbosity=2).run(suite)


