from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging
import time

class Finance(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
        self.finance_click = "//a[@href='/Clarity/Vouchers']"
        self.finance_wellpartner_page = "//td[@class='Text StatementNo StatementNo_Link']"
        self.finance_pharmacy_click = "//div[@class='span12']//*[contains(text(),'Pharmacy Vendor Statements')]"
        self.finance_pharmacy_page = "//td[@class='Currency ARR ARR_Link']"
        self.finance_replenishment_click = "//div[@class='span12']//*[contains(text(),'Replenishment Status')]"
        self.finance_paymentRemittance_click = "//div[@class='span12']//*[contains(text(),'Payment Remittance')]"
        self.finance_paymentRemittance_page = "//td[@class='Text PaymentTo PaymentTo_Link']"
        self.defaultview = "//div[@class='toolbar']/button[@id='restore_defaults']"

        """Verify Finance Screen"""

    def finance_grid(self):
        self.elementClick(self.finance_click)
        result = self.waitForData(self.finance_wellpartner_page)
        return result

    def pharmacyStatements(self):
        self.waitForElement(self.finance_pharmacy_click).click()
        result2 = self.waitForData(self.finance_pharmacy_page)
        return result2

    def paymentRemittance(self):
        time.sleep(1)
        self.elementClick(self.finance_paymentRemittance_click)
        result3 = self.waitForDelayData(self.finance_paymentRemittance_page)
        return result3
