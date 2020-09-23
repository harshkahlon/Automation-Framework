import time
from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging

class ProgramConfiguration(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

        self.pc_click = "//a[@href='/Clarity/ClientConfig']"
        self.defaultview = "//div[@class='toolbar']/button[@id='restore_defaults']"
        self.clinics_click = "//li[@id='EntityClinicsTab']"
        self.clinics_page = "//td[@class='Text ClinicCode ClinicCode_Link']"
        self.clinics_InfoIcon = "//td[@class='Text EntityClinicDetailButton EntityClinicDetailButton_Link']"
        self.clinics_Info_Window = "//div[@class='modal-header']"
        self.clinics_Info_Close = "//button[@class='close']"
        self.patients_click = "//li[@id='EntityPatientsTab']"
        self.prescribers_click = "//li[@class='k-item k-state-default']//*[contains(text(),'Prescribers')]"
        self.prescribers_page = "//td[@class='TEXT PrescriberCode PrescriberCode_Link']"
        self.prescribers_Info_Icon = "//td[@class='Text EntityPrescriberDetailButton EntityPrescriberDetailButton_Link']"
        self.prescribers_Info_Window = "//div[@class='modal-header']"
        self.prescribers_Info_Close = "//button[@class='close']"
        self.agreementFeeStructure_click = "//li[@id='AgreementFeeStructureTab']"
        self.agreementFeeStructure_page = "//td[@class='Text ContractPharmacy ContractPharmacy_Link']"
        self.agreementFeeStructure_Info_Icon = "//i[@class='grid-detail-button grid-agreement-detail-button icon-info-sign']"
        self.agreementFeeStructure_Info_Window = "//div[@class='modal-header']"
        self.agreementFeeStructure_Info_close = "//button[@class='close']"
        self.carveInRules_click = "//li[@id='CarveInRuleTab']"
        self.carveInRules_page = "//div[@id='CarveInRulesGrid']"
        self.inventory_click = "//li[@id='InventoryAndPaymentManagementTab']"
        self.inventory_page = "//div[@id='ProgramConfigInventoryAndPaymentManagementGrid']"

    def pc_grid(self):
        self.waitForElement(self.pc_click).click()
        self.waitForData(self.clinics_page)
        result = self.waitForData(self.clinics_page)
        return result

    def prescribers(self):
        self.waitForElement(self.prescribers_click).click()
        self.waitForData(self.prescribers_page)
        self.elementClick(self.prescribers_Info_Icon)
        result2 = self.waitForData(self.prescribers_Info_Window)
        self.elementClick(self.prescribers_Info_Close)
        return result2

    def agreementFeeStructure(self):
        self.waitForElement(self.agreementFeeStructure_click).click()
        self.waitForData(self.agreementFeeStructure_page)
        self.elementClick(self.agreementFeeStructure_Info_Icon)
        result3 = self.waitForData(self.agreementFeeStructure_Info_Window)
        self.elementClick(self.agreementFeeStructure_Info_close)
        return result3

    def carveInRules(self):
        self.waitForElement(self.carveInRules_click).click()
        result4 = self.waitForData(self.carveInRules_page)
        return result4

    def inventoryPayment(self):
        self.waitForElement(self.inventory_click).click()
        result5 = self.waitForData(self.inventory_page)
        return result5


