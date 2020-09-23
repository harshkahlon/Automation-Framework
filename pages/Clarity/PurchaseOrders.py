from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging

class PurchaseOrders(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

        self.purchaseorders_grid_click = "//a[@href='/Clarity/PurchaseOrders']"
        self.purchaseorders_grid_page = "//div[@class='GridWindow']//td[@class='Text PO PO_Link']"
        self.defaultview = "//div[@class='toolbar']/button[@id='restore_defaults']"

    """Verify Purchase Order Screen"""

    def purchaseorders_grid(self):
        self.waitForElement(self.purchaseorders_grid_click).click()
        result = self.waitForElement(self.purchaseorders_grid_page)
        return result
