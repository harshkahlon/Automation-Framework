import time
from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging

"""This class have all web elements of Clarity Claims Grid"""

class Claims(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
        self.change_password_click = "//a[@href='/security/authentication/changepassword']"
        self.change_password_page = "//input[@id='OldPassword']"
        self.claim_grid_click = "//a[@href='/Clarity/Claims']"
        self.defaultview = "//div[@class='toolbar']/button[@id='restore_defaults']"
        self.claim_page = "//td[@class='Text NPI NPI_Link']"
        self.claim_info_icon = "//i[@class='grid-detail-button icon-info-sign']"
        self.info_icon_page = "//div[@class='modal-header']"
        self.claim_info_window = "//div[@class='modal-body']"
        self.infoWindow_close = "//button[@class='close']"
        self.finance = "//a[@id='FinancialTab']"
        self.finance_data = "//td[contains(text(),'Est 340B Cost')]"
        self.qualification = "//a[contains(text(),'Qualification Detail')]"
        self.qualification_data = ".alert"
        self.rxHistory = "//a[@id='RxHistoryTab']"
        self.rxHistory_data = "//th[@data-field='Fill']"
        self.error = "//h2[contains(text(),' Sorry, an error occurred while processing your request.')]"


    """Verify Claims Screen"""
    def claim_grid(self):
        self.elementClick(self.claim_grid_click)
        error = len(self.driver.find_elements_by_xpath(self.error))
        if error > 0:
            self.screenShot("Claims Screen Error")
            self.driver.back()
            return False
        else:
            self.waitForData(self.claim_page)
            return True

    def claim_infoIcon(self):
        self.elementClick(self.claim_info_icon)
        result2 = self.waitForElement(self.info_icon_page)
        return result2

    def claim_finance(self):
        self.waitForElement(self.finance).click()
        result3 = self.waitForElement(self.finance_data)
        return result3

    def claim_qualification(self):
        self.waitForElement(self.qualification).click()
        result4 = self.waitForElement(self.qualification_data, locatorType="css")
        return result4

    def claim_rxHistory(self):
        self.waitForElement(self.rxHistory).click()
        time.sleep(1)
        result5 = self.waitForElement(self.rxHistory_data)
        self.elementClick(self.infoWindow_close)
        return result5







