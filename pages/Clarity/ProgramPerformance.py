from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging

"""This Class have all web elements related to Clarity Program Performance Grid"""

class ProgramPerformance(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

        self.pp_click = "//a[@href='/Clarity/ProgramPerformance']"
        self.summary_page = "//div[@id='gridFinancialSummary']/div[3]/table[@role='grid']/tbody/tr[2]/td[3]"
        self.pharmacy_click = "//*[contains(text(),' Program Results by Pharmacy Affiliation')]"
        self.pharmacy_page = "//table[@role='grid']/tbody/tr[1]/td[contains(text(),' 0')]"

    """Verify Program Performance Screen"""

    def summary(self):
        self.elementClick(self.pp_click)
        result = self.waitForData(self.summary_page)
        return result

    def pharmacy(self):
        # self.elementClick(self.pharmacy_click)
        # result2 = self.waitForData(self.pharmacy_page)
        # return result2

        error = len(self.driver.find_elements_by_xpath(self.pharmacy_page))
        if error > 0:
            return False
        else:
            if error == 0:
                return True
