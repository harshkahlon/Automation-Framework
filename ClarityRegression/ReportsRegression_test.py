import pytest
import unittest
from utils.status import Status
import time
from utils import env as utils

from pages.Login.LoginPage import LoginPage
from pages.Logout.LogoutPage import LogoutPage
from pages.Clarity.Dashboard import Dashboard
from pages.Clarity.ReportCenter import ReportCenter

@pytest.mark.usefixtures("test_setup")
class TestClarityReports(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, test_setup):
        driver = self.driver
        self.lp = LoginPage(self.driver)
        self.dashboard = Dashboard(self.driver)
        self.rc = ReportCenter(self.driver)
        self.lc = LogoutPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.enterUsername(utils.adminUSERNAME)
        self.lp.enterpassword(utils.adminPASSWORD)
        self.lp.clickSignin()
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Valid Login Verification")

    @pytest.mark.run(order=2)
    def test_HRSA_AuditReport(self):
        self.rc.report_grid()
        result = self.rc.audit_support()
        self.ts.markFinal("test_ReportCenter", result, "HRSA Audit Report Verification")
    #
    # @pytest.mark.run(order=3)
    # def test_HRSA_PreAuditReport(self):
    #     result = self.rc.hrsa_pre_audit()
    #     self.ts.markFinal("test_ReportCenter", result, "HRSA Pre Audit Report Verification")
    #
    # @pytest.mark.run(order=4)
    # def test_Claims_CarvedInClaimsByEntity(self):
    #     result = self.rc.claims_carvedInClaimsByEntity()
    #     self.ts.markFinal("test_ReportCenter", result, "Carved In Claims By Entity Verification")
    #
    # @pytest.mark.run(order=5)
    # def test_Claims_CarvedInClaimsByPharmacy(self):
    #     result = self.rc.claims_carvedInClaimsByPharmacy()
    #     self.ts.markFinal("test_ReportCenter", result, "Carved In Claims By Pharmacy Verification")

    # @pytest.mark.run(order=5.1)
    # def test_Claims_CarvedInClaimsByPrescriber(self):
    #     result = self.rc.claims_carvedInClaimsByPrescriber()
    #     self.ts.markFinal("test_ReportCenter", result, "Carved In Claims By Prescriber Verification")

    # @pytest.mark.run(order=5.2)
    # def test_Claims_ClaimsByAmountPaid(self):
    #     result = self.rc.claims_claimsWithAmountPaid()
    #     self.ts.markFinal("test_ReportCenter", result, "Claims By Amount Paid Verification")
    #
    # @pytest.mark.run(order=5.3)
    # def test_Claims_EntityApprovedPendingClaims(self):
    #     result = self.rc.claims_entityApprovedPendingClaims()
    #     self.ts.markFinal("test_ReportCenter", result, "Entity Approved Pending Claims Verification")
    #
    # @pytest.mark.run(order=5.4)
    # def test_Claims_InHousePharmacyClaims(self):
    #     result = self.rc.claims_inhousePharmacyClaims()
    #     self.ts.markFinal("test_ReportCenter", result, "In House Pharmacy Claims Verification")
    #
    # @pytest.mark.run(order=6)
    # def test_Claims_CarvedOutClaims(self):
    #     result = self.rc.claims_carvedOutClaims()
    #     self.ts.markFinal("test_ReportCenter", result, "Carved Out Claims Verification")
    #
    @pytest.mark.run(order=7)
    def test_Drugs_Top10_TotalCarveIns(self):
        result = self.rc.drugs_top10_TotalCarveIns()
        self.ts.markFinal("test_DrugsReport", result, "Top 10 Drugs via Total Carves Ins Verification")

    @pytest.mark.run(order=8)
    def test_Drugs_Top10_TotalProgramRevenue(self):
        result = self.rc.drugs_top10_TotalProgremRevenue()
        self.ts.markFinal("test_DrugsReport", result, "Top 10 Drugs via Total Program Revenue Verification")

    @pytest.mark.run(order=9)
    def test_Drugs_Top10_ProgramRevenuePerScript(self):
        result = self.rc.drugs_top10_ProgramRevenuePerScript()
        self.ts.markFinal("test_DrugsReport", result, "Top 10 Drugs via Program Revenue By Script Verification")


    @pytest.mark.trylast
    def test_logout(self):
        result = self.lc.logout()
        self.ts.markFinal("test_logout", result, "Logout Verification")