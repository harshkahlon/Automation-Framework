from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging

class EDI(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

        self.edi_click = "//a[@href='/Clarity/Edi']"
        self.edi_page = "//td[@class='Text Entity Entity_Link']"
        self.defaultview = "//div[@class='toolbar']/button[@id='restore_defaults']"

    def edi_grid(self):
        self.waitForElement(self.edi_click).click()
        result = self.waitForData(self.edi_page)
        return result
