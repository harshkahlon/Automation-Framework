from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging

class Accumulator(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

        self.accumulator_click = "//a[@href='/Clarity/Accumulator']"
        self.accumulator_page = "//td[@class='Text Entity Entity_Link']"
        self.defaultview = "//div[@class='toolbar']/button[@id='restore_defaults']"

    """Verify Accumulator Scrren"""

    def accumulator_grid(self):
        self.waitForElement(self.accumulator_click).click()
        result = self.waitForDelayData(self.accumulator_page)
        return result
