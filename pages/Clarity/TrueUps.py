from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging

class TrueUps(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

        self.trueups_click = "//a[@href='/Clarity/TrueUps']"
        self.trueups_page = "//div[@class='GridWindow']//td[@class='Text Entity Entity_Link']"
        self.defaultview = "//div[@class='toolbar']/button[@id='restore_defaults']"

    """Verify True-ups Screen"""

    def trueups_grid(self):
        self.waitForElement(self.trueups_click).click()
        result = self.waitForData(self.trueups_page)
        return result


