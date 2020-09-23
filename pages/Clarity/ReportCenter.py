from base.selenium_driver import SeleniumDriver
import utils.custom_logger as cl
import logging
import time
from selenium.webdriver.common.keys import Keys
"""This Class have all web elements related to Clarity Report Center Grid"""

class ReportCenter(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

        self.report_click = "//a[@href='/Clarity/RptViewer/Index.aspx']"
        self.audit_click = "//a[contains(text(),'Audit Support')]"
        self.hrsaReport = "//li[@class='1 rptli']/a[contains(@title,'Pre-formed audit report')]"
        self.hrsaPreAudit = "//li[@class='1 rptli']/a[contains(@title,'The HRSA Audit report appended')]"
        self.begin_calander = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl03$ddDropDownButton']"
        self.begin_dateBox = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl03$txtValue']"
        self.begin2_dateBox = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl07$txtValue']"
        self.end_calander = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl05$ddDropDownButton']"
        self.end_dateBox = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl05$txtValue']"
        self.end2_dateBox = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl09$txtValue']"
        self.entity_dropdown = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl07$ddDropDownButton']"
        self.selectUCSF = "//label[contains(text(),'University of California San Francisco')]"
        self.selectPresb = "//label[contains(text(),'Presbyterian Hospital (Presb)')]"
        self.selectAll = "//label[contains(text(),'(Select All)')]"
        self.pharmacy_dropdown = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl09$ddDropDownButton']"
        self.pharmacy_selectAll = "//input[@id='ctl00_MainContent_ReportViewer1_ctl04_ctl09_divDropDown_ctl00']"
        self.reversal_dropdown = "//select[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl11$ddValue']"
        self.reversal_selectClaims = "//select[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl11$ddValue']/option[@value='2']"
        self.reportView_click = "//input[@value='View Report']"
        self.pageBox = "//input[@name='ctl00$MainContent$ReportViewer1$ctl05$ctl00$CurrentPage']"
        self.nextPage = "//input[@name='ctl00$MainContent$ReportViewer1$ctl05$ctl00$Next$ctl00$ctl00']"
        self.lastPage = "//input[@name='ctl00$MainContent$ReportViewer1$ctl05$ctl00$Last$ctl00$ctl00']"
        self.hrsa_auditReport_data = "//div[contains(text(),'8344')]"
        self.hrsa_preAuditReport_data = "//div[contains(text(),'9656')]"
        self.claimReport = "//a[@class='toggle'][contains(text(),'Claim')]"
        self.carvedInClaimsByEntity = "//div[@id='report-list']/ul/li[11]"
        self.carvedInClaimsByEntity_Data = "//div[contains(text(),'18016')]"
        self.carvedInClaimsByPharmacy = "//div[@id='report-list']/ul/li[12]"
        self.carvedInClaimsByPharmacy_Data = "//div[contains(text(),'768,991.6')]"
        self.carvedInClaimsByPrescriber = "//div[@id='report-list']/ul/li[13]"
        self.carvedInClaimsByPrescriber_Data = "//div[contains(text(),'12,291')]"
        self.claimsByAmountPaid = "//div[@id='report-list']/ul/li[19]"
        self.claimsByAmountPaid_Data = "//div[contains(text(),'1837')]"
        self.entityApprovedPendingClaims = "//div[@id='report-list']/ul/li[20]"
        self.entityApprovedPendingClaims_Data = "//div[contains(text(),'$163,457.52')]"
        self.inhousePharmacyClaims = "//div[@id='report-list']/ul/li[22]"
        self.inhousePharmacyClaims_UCSF = "//label[contains(text(),'UCSF Medical Center In House Pharmacy')]"
        self.inhousePharmacyClaims_All = "//option[contains(text(),'All')]"
        self.inhousePharmacyClaims_All_Data = "//div[contains(text(),'831')]"
        self.claims_entitydropdown = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl03$ddDropDownButton']"
        self.claims_beginDate = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl05$txtValue']"
        self.claims_endDate = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl07$txtValue']"
        self.carvedOutClaims = "//div[@id='report-list']/ul/li[14]"
        self.carvedOutClaims_Data = "//div[contains(text(),'57458')]"
        self.CBPClaimsVsStandard = "//div[@id='report-list']/ul/li[15]"
        self.CBP_entityDropDown = "//select[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl03$ddValue']"
        self.CPB_entitySelect = "//option[contains(text(),'Presbyterian Hospital (Presb)')]"
        self.CPP_beginDate = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl05$txtValue']"
        self.CBP_endDate = "//input[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl07$txtValue']"
        self.drugReport = "//a[@class='toggle'][contains(text(),'Drug')]"
        self.drug_top10CarvedIn = "//div[@id='report-list']/ul/li[37]/a[starts-with(@title,'Top 10 Drugs carved')]"
        self.top10_Select = "//select[@name='ctl00$MainContent$ReportViewer1$ctl04$ctl09$ddValue']"
        self.top10_select_totalCarveIns = "//option[contains(text(),'Total Carve Ins')]"
        self.top10CarveIns_Data = "//div[contains(text(),'1,614')]"
        self.top10_select_totalProgramRevenue = "//option[contains(text(),'Total Program Revenue')]"
        self.top10_select_totalProgramRevenue_Data = "//div[contains(text(),'$1,921,888.93')]"
        self.top10_select_progemRevenueByScripts = "//option[contains(text(),'Program Revenue per Script')]"
        self.top10_select_progemRevenueByScripts_Data = "//div[contains(text(),'$395,900.28')]"



    """Verify Report Center Screen"""

    def report_grid(self):
        self.waitForElement(self.report_click).click()

    def audit_support(self):
        self.waitForElement(self.audit_click).click()
        time.sleep(1)
        self.elementClick(self.hrsaReport)
        self.sendKeys("02/01/2020", self.begin_dateBox)
        self.sendKeys("02/15/2020", self.end_dateBox)
        self.elementClick(self.entity_dropdown)
        time.sleep(2)
        self.elementClick(self.selectPresb)
        self.elementClick(self.entity_dropdown)
        time.sleep(1)
        self.waitForElement(self.pharmacy_dropdown)
        self.elementClick(self.pharmacy_dropdown)
        self.waitForElement(self.selectAll)
        self.elementClick(self.selectAll)
        self.elementClick(self.reversal_dropdown)
        self.elementClick(self.reversal_selectClaims)
        self.elementClick(self.reportView_click)
        self.waitForDelayData(self.lastPage)
        self.elementClick(self.lastPage)
        result = self.waitForData(self.hrsa_auditReport_data)
        return result

    def hrsa_pre_audit(self):
        self.elementClick(self.hrsaPreAudit)
        self.sendKeys("01/01/2020", self.begin_dateBox)
        self.sendKeys("01/15/2020", self.end_dateBox)
        self.elementClick(self.entity_dropdown)
        self.waitForElement(self.selectPresb)
        self.elementClick(self.selectPresb)
        self.elementClick(self.entity_dropdown)
        time.sleep(1)
        self.waitForElement(self.pharmacy_dropdown)
        self.elementClick(self.pharmacy_dropdown)
        self.waitForElement(self.selectAll)
        self.elementClick(self.selectAll)
        self.elementClick(self.reversal_dropdown)
        self.elementClick(self.reversal_selectClaims)
        self.elementClick(self.reportView_click)
        self.waitForDelayData(self.lastPage)
        self.elementClick(self.lastPage)
        result = self.waitForDelayData(self.hrsa_preAuditReport_data)
        return result

    def claims_carvedInClaimsByEntity(self):
        self.elementClick(self.claimReport)
        time.sleep(2)
        self.elementClick(self.carvedInClaimsByEntity)
        self.sendKeys("01/01/2020", self.begin_dateBox)
        self.sendKeys("01/31/2020", self.end_dateBox)
        self.elementClick(self.entity_dropdown)
        self.waitForElement(self.selectPresb)
        self.elementClick(self.selectPresb)
        self.elementClick(self.entity_dropdown)
        time.sleep(1)
        self.waitForElement(self.pharmacy_dropdown)
        self.elementClick(self.pharmacy_dropdown)
        self.waitForElement(self.selectAll)
        self.elementClick(self.selectAll)
        self.elementClick(self.reportView_click)
        self.waitForDelayData(self.lastPage)
        self.elementClick(self.lastPage)
        result = self.waitForDelayData(self.carvedInClaimsByEntity_Data)
        return result

    def claims_carvedInClaimsByPharmacy(self):
        self.elementClick(self.carvedInClaimsByPharmacy)
        self.sendKeys("01/01/2020", self.begin_dateBox)
        self.sendKeys("01/31/2020", self.end_dateBox)
        self.elementClick(self.entity_dropdown)
        self.waitForElement(self.selectPresb)
        self.elementClick(self.selectPresb)
        self.elementClick(self.entity_dropdown)
        time.sleep(1)
        self.waitForElement(self.pharmacy_dropdown)
        self.elementClick(self.pharmacy_dropdown)
        self.waitForElement(self.selectAll)
        self.elementClick(self.selectAll)
        self.elementClick(self.reportView_click)
        self.waitForDelayData(self.lastPage)
        self.elementClick(self.lastPage)
        result = self.waitForDelayData(self.carvedInClaimsByPharmacy_Data)
        return result

    def claims_carvedInClaimsByPrescriber(self):
        self.elementClick(self.carvedInClaimsByPrescriber)
        self.waitForElement(self.claims_entitydropdown)
        self.elementClick(self.claims_entitydropdown)
        time.sleep(1)
        self.elementClick(self.selectPresb)
        self.elementClick(self.claims_entitydropdown)
        self.sendKeys("01/01/2020", self.claims_beginDate)
        self.sendKeys("01/31/2020", self.claims_endDate)
        self.elementClick(self.reportView_click)
        self.waitForDelayData(self.lastPage)
        self.elementClick(self.lastPage)
        result = self.waitForDelayData(self.carvedInClaimsByPrescriber_Data)
        return result


    def claims_carvedOutClaims(self):
        self.elementClick(self.carvedOutClaims)
        self.sendKeys("01/01/2020", self.begin_dateBox)
        self.sendKeys("01/31/2020", self.end_dateBox)
        self.elementClick(self.entity_dropdown)
        self.waitForElement(self.selectPresb)
        self.elementClick(self.selectPresb)
        self.elementClick(self.entity_dropdown)
        time.sleep(1)
        self.waitForElement(self.pharmacy_dropdown)
        self.elementClick(self.pharmacy_dropdown)
        self.waitForElement(self.selectAll)
        self.elementClick(self.selectAll)
        self.elementClick(self.reportView_click)
        self.waitForDelayData(self.lastPage)
        self.elementClick(self.lastPage)
        result = self.waitForDelayData(self.carvedOutClaims_Data)
        return result

    def claims_claimsWithAmountPaid(self):
        self.elementClick(self.claimsByAmountPaid)
        self.sendKeys("01/01/2020", self.begin_dateBox)
        self.sendKeys("01/31/2020", self.end_dateBox)
        self.elementClick(self.entity_dropdown)
        self.elementClick(self.selectPresb)
        self.elementClick(self.entity_dropdown)
        self.waitForElement(self.pharmacy_dropdown)
        self.elementClick(self.pharmacy_dropdown)
        self.waitForElement(self.pharmacy_selectAll)
        self.elementClick(self.pharmacy_selectAll)
        self.elementClick(self.reportView_click)
        self.waitForDelayData(self.lastPage)
        self.elementClick(self.lastPage)
        result = self.waitForDelayData(self.claimsByAmountPaid_Data)
        return result

    def claims_entityApprovedPendingClaims(self):
        self.elementClick(self.entityApprovedPendingClaims)
        self.waitForElement(self.begin_calander)
        self.elementClick(self.begin_calander)
        self.elementClick(self.selectPresb)
        self.elementClick(self.begin_calander)
        self.waitForElement(self.end_calander)
        self.elementClick(self.end_calander)
        self.elementClick(self.selectAll)
        self.elementClick(self.end_calander)
        time.sleep(1)
        self.sendKeys("01/01/2020", self.begin2_dateBox)
        self.sendKeys("01/31/2020", self.end2_dateBox)
        self.elementClick(self.reportView_click)
        self.waitForDelayData(self.lastPage)
        self.clearField(self.pageBox)
        self.sendKeys("3", self.pageBox)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.pageBox).send_keys(Keys.ENTER)
        time.sleep(1)
        result = self.waitForDelayData(self.entityApprovedPendingClaims_Data)
        return result

    def claims_inhousePharmacyClaims(self):
        self.elementClick(self.inhousePharmacyClaims)
        self.waitForElement(self.begin_calander)
        self.elementClick(self.begin_calander)
        self.elementClick(self.inhousePharmacyClaims_UCSF)
        self.elementClick(self.begin_calander)
        self.sendKeys("01/01/2020", self.claims_beginDate)
        self.sendKeys("01/15/2020", self.claims_endDate)
        time.sleep(1)
        self.elementClick(self.top10_Select)
        time.sleep(1)
        self.elementClick(self.inhousePharmacyClaims_All)
        self.elementClick(self.reportView_click)
        self.waitForDelayData(self.lastPage)
        self.elementClick(self.lastPage)
        result = self.waitForDelayData(self.inhousePharmacyClaims_All_Data)
        return result

    def drugs_top10_TotalCarveIns(self):
        self.elementClick(self.drugReport)
        time.sleep(2)
        self.elementClick(self.drug_top10CarvedIn)
        self.elementClick(self.claims_entitydropdown)
        self.waitForElement(self.selectPresb)
        self.elementClick(self.selectPresb)
        self.elementClick(self.claims_entitydropdown)
        self.sendKeys("01/01/2020", self.claims_beginDate)
        self.sendKeys("01/31/2020", self.claims_endDate)
        self.elementClick(self.top10_Select)
        self.elementClick(self.top10_select_totalCarveIns)
        self.elementClick(self.reportView_click)
        result = self.waitForDelayData(self.top10CarveIns_Data)
        return result

    def drugs_top10_TotalProgremRevenue(self):
        self.elementClick(self.top10_Select)
        self.elementClick(self.top10_select_totalProgramRevenue)
        self.elementClick(self.reportView_click)
        result = self.waitForDelayData(self.top10_select_totalProgramRevenue_Data)
        return result

    def drugs_top10_ProgramRevenuePerScript(self):
        self.elementClick(self.top10_Select)
        self.elementClick(self.top10_select_progemRevenueByScripts)
        self.elementClick(self.reportView_click)
        result = self.waitForDelayData(self.top10_select_progemRevenueByScripts_Data)
        return result




















