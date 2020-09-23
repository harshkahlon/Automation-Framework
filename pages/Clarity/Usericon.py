import time
from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging

"""Web elements of User Icon , Password Change"""

class Usericon(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
        self.username_dropdown_click = "//i[@class='icon-user']"
        self.change_password_click = "//a[contains(text(),'Change Password')]"
        self.change_password_page = "//input[@id='OldPassword']"

    def change_password(self):
        self.elementClick(self.username_dropdown_click)
        # time.sleep(2)
        self.waitForElement(self.change_password_click)
        self.elementClick(self.change_password_click)

    def change_passwordScreen(self):
        result = self.isElementPresent(self.change_password_page)
        self.driver.back()
        return result
