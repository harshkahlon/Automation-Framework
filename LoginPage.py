from base.selenium_driver import SeleniumDriver
import time
import utils.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
        self.username_field = "inputEmail"
        self.password_field = "inputPassword"
        self.signin_button = "//button[@type='submit']"
        self.resetpasswrod_url = "//a[contains(text(),'Click here to reset it.')]"
        self.loginFail = "// div[contains(text(),'Username or password does not match our records. Please try again.')]"
        self.resetPassword = "//img[@class='BDC_CaptchaImage']"
        self.homeicon = "//i[@class='icon-home']"

    def enterUsername(self, username):
        self.sendKeys(username, self.username_field, locatorType="id")

    def enterpassword(self, password):
        self.sendKeys(password, self.password_field, locatorType="id")

    def clickSignin(self):
        self.elementClick(self.signin_button)

    def login(self, username, password):
        self.enterUsername(username)
        self.enterpassword(password)
        self.clickSignin()

    def verifyLoginSuccessful(self):
        result = self.waitForElement(self.homeicon)
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self.loginFail)
        return result

    def verifyResetPassword(self):
        self.elementClick(self.resetpasswrod_url)
        time.sleep(2)
        result = self.isElementPresent(self.resetPassword)
        return result



