from base.selenium_driver import SeleniumDriver
import time
import utils.custom_logger as cl
import logging

class LogoutPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
        self.username_dropdown = "//i[@class='icon-user']"
        self.logout_click = "Logout"
        self.username_textbox = "inputEmail"

    def logout(self):
        self.elementClick(self.username_dropdown)
        time.sleep(1)
        self.elementClick(self.logout_click, locatorType="link")
        result = self.isElementPresent(self.username_textbox, locatorType="id")
        return result
