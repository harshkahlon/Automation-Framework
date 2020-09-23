from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging
import time

"""This Class have all web elements related to Clarity Dashboard Grid"""

class Dashboard(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
        self.dashboard_title = "icon-home"
        self.dashboard_page = "//div[@id='top5']//a"
        self.netClaims_count = "//h2[starts-with(text(),'0')]"
        self.top5drugs = "//td[@class='Drug_Link']"
        self.top5url_data = "//div[@class='modal-body']"
        self.top5_close = "//button[@class='close']"
        self.top5Pharmacies = "//td[@class='Pharmacy_Link']"
        self.top5Prescribers = "//td[@class='Prescriber_Link']"

    """Verify Clarity Dashboard"""

    def dashboard_top5(self):
        # time.sleep(2)
        result = self.waitForElement(self.dashboard_page)
        return result

    def netClaims_Count(self):
        error = len(self.driver.find_elements_by_xpath(self.netClaims_count))
        if error > 0:
            return False
        else:
            if error == 0:
                return True

    def top5drugsClaims(self):
        self.elementClick(self.top5drugs)
        result = self.waitForElement(self.top5url_data)
        time.sleep(1)
        self.elementClick(self.top5_close)
        return result

    def top5pharmacies(self):
        self.elementClick(self.top5Pharmacies)
        result = self.waitForElement(self.top5url_data)
        time.sleep(1)
        self.elementClick(self.top5_close)
        return result

    def top5prescribers(self):
        self.elementClick(self.top5Prescribers)
        result = self.waitForElement(self.top5url_data)
        time.sleep(1)
        self.elementClick(self.top5_close)
        return result
