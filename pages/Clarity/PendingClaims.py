import time
from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging

class PendingClaims(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

        self.pendingclaims_click = "//a[@href='/Clarity/PendingClaims']"
        self.pendingclaims_page = "//td[@class='date']"
        self.pendingclaims_defaultview = "//button[contains(text(),'Default View')]"
        self.infoIcon = "//button[@icon='k-icon k-i-edit']"
        self.infoIcon_data = "//h3[contains(text(),'Script')]"
        self.infoIcon_cancel = "//button[contains(text(),'Cancel')]"

    """Verify Pending Claims"""
    def pendingclaims_grid(self):
        self.waitForElement(self.pendingclaims_click).click()
        result = self.waitForData(self.pendingclaims_page)
        return result

    def pendingClaim_infoIcon(self):
        self.waitForElement(self.infoIcon).click()
        result2 = self.waitForElement(self.infoIcon_data)
        self.elementClick(self.infoIcon_cancel)
        time.sleep(1)
        return result2





