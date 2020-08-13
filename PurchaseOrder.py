import time
from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging
from selenium.webdriver.common.action_chains import ActionChains


class PurchaseOrders(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # Locators
        self.purchasing = "//li[contains(text(),'Purchasing')]"
        self.purchasing_PO = "//a[@href='/340B/Purchases/NewPOScreen']"
        self.CreateSimulatedPOButton = "//button[starts-with(text(),'Create Simulated PO')]"
        self.CreateSimulatedPO_AccountDropDown = "//span[@class='k-icon k-i-arrow-s']"
        self.CreateSimulatedPO_AccountDropDown_Select = "ul[role='listbox'] > li:nth-of-type(2)"
        self.CreatePO_button = "//div[@id='ContentMain']//kendo-dialog//kendo-dialog-actions/button[2]"
        self.Check_NoData = "//div[1]/div[1]/table[@role='presentation']//td[i]"
        self.InfoIcon = "//i[@class='fa fa-pencil pointerCursor ng-star-inserted']"
        self.AddLineItem = ".ng-star-inserted > .buttonPrimary.k-button.ng-star-inserted"
        self.AddLineItem_NDC = "input[role='textbox']"
        self.AddLineItem_NDC_AutoSelection = "ul[role='listbox'] > li:nth-of-type(3)"
        self.AddLineItem_NDC_Quantity = "//p/input"
        self.AddLineItem_Button = "//po-line[@class='ng-star-inserted']/kendo-dialog//kendo-dialog-actions/button[2]"
        self.CreateSimulatedPO_Delete = "//po-line[@class='ng-star-inserted']/span/button[1]"
        self.CreateSimulatedPO_Delete_LineItem = "//mat-radio-button[@value='Yes']//div[@class='mat-radio-container']"
        self.CreateSimulatedPO_Delete_LineItem_CheckBox = "//input[@name='deletePOLine']"
        self.CreateSimulatedPO_Delete_LineItem_button = "//div[@id='k-tabstrip-tabpanel-0']/div[2]/button[1]"
        self.SimulatedPO_DeletionMessage = "//div[starts-with(text(),'Purchase Order Line Deleted Successfully')]"
        self.ExitDetails = "//po-line[@class='ng-star-inserted']/span/button[2]"
        self.browseButton = "//label[@id='btnBrowse']"
        self.uploadButton = "//label[@id='btnUpload']"
        self.uploadMessage = "//div[contains(text(),'loaded successfully.')]"
        self.fileUpload = "#fileUpload"
        self.submitted_PO_button = "//span[contains(text(),'Submitted Purchase Orders')]"
        self.submitted_PO_InfoIcon = "kendo-grid-list tbody > .ng-star-inserted:nth-of-type(1) .fa-info-circle"
        self.NDC_Link = "tr:nth-of-type(1) > td:nth-of-type(2) a"
        self.NDC_Data = "//h3[contains(text(),'Charge Master: NDC Detail')]"
        self.CurrentDetails_Cancel_Icon = ".fa-times"
        self.CurrentDetails_Cancel_Button = "//button[contains(text(),'Cancel')]"


    """Verify Purchase Orders Screen"""

    def createSimulatedPO(self):
        # time.sleep(2)
        actions = ActionChains(self.driver)
        activity = self.driver.find_element_by_xpath(self.purchasing)
        actions.move_to_element(activity).perform()
        self.elementClick(self.purchasing_PO)
        result = self.waitForData(self.CreateSimulatedPOButton)

        counter = len(self.driver.find_elements_by_xpath(self.Check_NoData))
        while counter > 0:
            counter -= 1
            self.elementClick(self.InfoIcon)
            time.sleep(2)
            self.elementClick(self.CreateSimulatedPO_Delete)
            time.sleep(2)
            alert_obj = self.driver.switch_to.alert
            alert_obj.accept()
            time.sleep(2)

        else:
            self.elementClick(self.CreateSimulatedPOButton)
            time.sleep(2)
            self.elementClick(self.CreateSimulatedPO_AccountDropDown)
            time.sleep(2)
            self.elementClick(self.CreateSimulatedPO_AccountDropDown_Select, locatorType="css")
            self.waitForElement(self.CreatePO_button)
            self.elementClick(self.CreatePO_button)
            return result

    def simulatedPO_AddLineItem(self):
        self.elementClick(self.InfoIcon)
        time.sleep(2)
        self.elementClick(self.AddLineItem, locatorType="css")
        time.sleep(2)
        self.sendKeys("Sodium", self.AddLineItem_NDC, locatorType="css")
        self.elementClick(self.AddLineItem_NDC_AutoSelection, locatorType="css")
        self.sendKeys("5", self.AddLineItem_NDC_Quantity)
        time.sleep(2)
        result = self.waitForData(self.AddLineItem_Button)
        self.elementClick(self.AddLineItem_Button)
        return result

    def simulatedPO_GlobalDelete(self):
        self.elementClick(self.InfoIcon)
        time.sleep(2)
        self.elementClick(self.CreateSimulatedPO_Delete)
        time.sleep(2)
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()
        time.sleep(2)
        result = self.waitForElement(self.CreateSimulatedPOButton)
        return result


    def simulatedPO_DeleteLineItem(self):
        self.elementClick(self.InfoIcon)
        time.sleep(2)
        self.elementClick(self.CreateSimulatedPO_Delete_LineItem)
        time.sleep(2)
        self.elementClick(self.CreateSimulatedPO_Delete_LineItem_CheckBox)
        time.sleep(2)
        self.elementClick(self.CreateSimulatedPO_Delete_LineItem_button)
        time.sleep(2)
        alert_obj = self.driver.switch_to.alert
        alert_obj.accept()
        time.sleep(5)
        result = self.isElementDisplayed(self.SimulatedPO_DeletionMessage)
        time.sleep(2)
        self.elementClick(self.ExitDetails)
        return result

    def upload_PO_file(self):
        self.waitForElement(self.browseButton)
        file = self.driver.find_element_by_css_selector(self.fileUpload)
        file.send_keys(r'\\nfs201\Dev\TeamCity\SileniumTesting\reports\auto_test..csv')

        self.elementClick(self.uploadButton)

        result = self.waitForData(self.uploadMessage)
        return result

    def submitted_PO(self):
        actions = ActionChains(self.driver)
        activity = self.driver.find_element_by_xpath(self.purchasing)
        actions.move_to_element(activity).perform()
        self.elementClick(self.purchasing_PO)
        self.waitForData(self.CreateSimulatedPOButton)
        self.elementClick(self.submitted_PO_button)
        self.elementClick(self.submitted_PO_InfoIcon, locatorType="css")
        self.elementClick(self.submitted_PO_InfoIcon, locatorType="css")
        self.elementClick(self.CurrentDetails_Cancel_Icon, locatorType="css")
        self.elementClick(self.submitted_PO_InfoIcon, locatorType="css")
        self.elementClick(self.CurrentDetails_Cancel_Button)
        self.elementClick(self.NDC_Link, locatorType="css")
        result = self.waitForElement(self.NDC_Data)
        return result







