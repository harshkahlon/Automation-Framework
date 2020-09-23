import pytest
import unittest
from utils.status import Status
import time
from utils import env as utils

from pages.Login.LoginPage import LoginPage
from pages.Logout.LogoutPage import LogoutPage
from pages.Clarity.Dashboard import Dashboard
from pages.Clarity.Claims import Claims
from pages.Clarity.Reversals import Reversals
from pages.Clarity.Usericon import Usericon
from pages.Clarity.CarveOuts import CarveOuts
from pages.Clarity.PendingClaims import PendingClaims
from pages.Clarity.PurchaseOrders import PurchaseOrders
from pages.Clarity.TrueUps import TrueUps
from pages.Clarity.Accumulator import Accumulator
from pages.Clarity.Finance import Finance
from pages.Clarity.EDI import EDI
from pages.Clarity.ProgramConfiguration import ProgramConfiguration
from pages.Clarity.ProgramPerformance import ProgramPerformance
from pages.Clarity.ReportCenter import ReportCenter

@pytest.mark.usefixtures("test_setup")
class TestEntityWithPHIAccess(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, test_setup):
        driver = self.driver
        self.lp = LoginPage(self.driver)
        self.dashboard = Dashboard(self.driver)
        self.claims = Claims(self.driver)
        self.reversals = Reversals(self.driver)
        self.usericon = Usericon(self.driver)
        self.carveouts = CarveOuts(self.driver)
        self.pendingclaims = PendingClaims(self.driver)
        self.purchaseorders = PurchaseOrders(self.driver)
        self.trueups = TrueUps(self.driver)
        self.accumulator = Accumulator(self.driver)
        self.finance = Finance(self.driver)
        self.edi = EDI(self.driver)
        self.pc = ProgramConfiguration(self.driver)
        self.pp = ProgramPerformance(self.driver)
        self.rc = ReportCenter(self.driver)
        self.lc =LogoutPage(self.driver)

        self.ts = Status(self.driver)


    # @pytest.mark.run(order=2)
    # def test_invalidLogin(self):
    #     self.lp.enterUsername(utils.wrongUSERNAME)
    #     self.lp.enterpassword(utils.wrongPASSWORD)
    #     self.lp.clickSignin()
    #     result = self.lp.verifyLoginFailed()
    #     self.ts.markFinal("test_invalidLogin", result, "In Valid Login Verification")
    #     time.sleep(2)
    #
    # @pytest.mark.run(order=1)
    # def test_passwordReset(self):
    #     result = self.lp.verifyResetPassword()
    #     self.ts.markFinal("test_passwordReset", result, "Password Reset Verification")
    #     self.driver.back()

    @pytest.mark.run(order=3)
    def test_validLogin(self):
        self.lp.enterUsername(utils.entityUSERNAME)
        self.lp.enterpassword(utils.entityPASSWORD)
        self.lp.clickSignin()
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Valid Login Verification")

    @pytest.mark.run(order=4)
    def test_Dashboard_Top5(self):
        result = self.dashboard.dashboard_top5()
        self.ts.markFinal("test_Dashboard", result, "Dashboard Top 5 Columns Verification")

    @pytest.mark.run(order=5)
    def test_Dashboard_NetClaims(self):
        result2 = self.dashboard.netClaims_Count()
        self.ts.markFinal("test_Dashboard", result2, "Dashboard Net Claims Count Verification")

    @pytest.mark.run(order=5.1)
    def test_Dashboard_Top5DrugsURL(self):
        result = self.dashboard.top5drugsClaims()
        self.ts.markFinal("test_Dashboard", result, "Top 5 Drugs URL Verification")

    @pytest.mark.run(order=5.2)
    def test_Dashboard_Top5PharmaciesURL(self):
        result = self.dashboard.top5pharmacies()
        self.ts.markFinal("test_Dashboard", result, "Top 5 Pharmacies URL Verification")

    @pytest.mark.run(order=5.3)
    def test_Dashboard_Top5PrescribersURL(self):
        result = self.dashboard.top5prescribers()
        self.ts.markFinal("test_Dashboard", result, "Top 5 Prescribers Verification")

    @pytest.mark.run(order=6)
    def test_ChangePassword(self):
        self.usericon.change_password()
        result = self.usericon.change_passwordScreen()
        self.ts.markFinal("test_ChangePasswordScreen", result, "Password Change Verification")

    @pytest.mark.run(order=7)
    def test_ClaimsGrid(self):
        result = self.claims.claim_grid()
        self.ts.markFinal("test_Claims Screen", result, "Claims Verification")

    @pytest.mark.run(order=7.1)
    def test_Claims_InfoIcon(self):
        result2 = self.claims.claim_infoIcon()
        self.ts.markFinal("test_ClaimsGrid", result2, "Claims Info Icon Verification")

    @pytest.mark.run(order=7.2)
    def test_Claims_InfoIcon_Finance(self):
        result3 = self.claims.claim_finance()
        self.ts.markFinal("test_ClaimsGrid", result3, "Finance Tab Verification")
        self.ts.mark( result3, "Finance Tab Verification")

    @pytest.mark.run(order=7.3)
    def test_Claims_InfoIcon_Qualification(self):
        result4 = self.claims.claim_qualification()
        self.ts.markFinal("test_ClaimsGrid", result4, "Qualification Tab Verification")

    @pytest.mark.run(order=7.4)
    def test_Claims_InfoIcon_RxHistory(self):
        result5 = self.claims.claim_rxHistory()
        self.ts.markFinal("test_ClaimsGrid", result5, "RxHistory Tab Verification")

    @pytest.mark.run(order=8)
    def test_Reversals(self):
        result = self.reversals.reversals_grid()
        self.ts.markFinal("test_ReversalsData", result, "Reversals Verification")

    @pytest.mark.run(order=9)
    def test_CarveOuts(self):
        result = self.carveouts.carveouts_grid()
        self.ts.markFinal("test_CarveOutsData", result, "CarveOuts Verification")

    @pytest.mark.run(order=10)
    def test_PendingClaims(self):
        result = self.pendingclaims.pendingclaims_grid()
        self.ts.markFinal("test_PendingClaims", result, "Pending Claims Verification")

    @pytest.mark.run(order=10.1)
    def test_PendingClaims_InfoIcon(self):
        result2 = self.pendingclaims.pendingClaim_infoIcon()
        self.ts.markFinal("test_InfoIcon", result2, "Pending Claims InfoIcon Verification")

    @pytest.mark.run(order=11)
    def test_PurchaseOrders(self):
        result = self.purchaseorders.purchaseorders_grid()
        self.ts.markFinal("test_PurchaseOrdersData", result, "Purchase Orders Verification")

    @pytest.mark.run(order=12)
    def test_TrueUps(self):
        result = self.trueups.trueups_grid()
        self.ts.markFinal("test_TrueUps", result, "True-Ups Verification")

    @pytest.mark.run(order=13)
    def test_Accumulator(self):
        result = self.accumulator.accumulator_grid()
        self.ts.markFinal("test_Accumulator", result, "Accumulator Verification")

    @pytest.mark.run(order=14)
    def test_Finance_WellPartnerStatements(self):
        result = self.finance.finance_grid()
        self.ts.markFinal("test_Finance_PaymentRemittance", result, "WellPartner Statements Verification")

    @pytest.mark.run(order=14.1)
    def test_Finance_PharmacyStatements(self):
        result2 = self.finance.pharmacyStatements()
        self.ts.markFinal("test_Finance_PaymentRemittance", result2, "Pharmacy Statements Verification")

    @pytest.mark.run(order=14.2)
    def test_Finance_PaymentRemittance(self):
        result3 = self.finance.paymentRemittance()
        self.ts.markFinal("test_Finance_PaymentRemittance", result3, "Payment Remittance Verification")

    @pytest.mark.run(order=15)
    def test_EDI(self):
        result = self.edi.edi_grid()
        self.ts.markFinal("test_EDI", result, "EDI Data Verification")

    @pytest.mark.run(order=16)
    def test_ProgramConfiguration(self):
        result = self.pc.pc_grid()
        self.ts.markFinal("test_ProgramConfiguration", result, "Program Configuration Verification")

    @pytest.mark.run(order=16.1)
    def test_ProgramConfiguration_Prescribers(self):
        result2 = self.pc.prescribers()
        self.ts.markFinal("test_ProgramConfiguration", result2, "Prescribers Verification")

    @pytest.mark.run(order=16.2)
    def test_ProgramConfiguration_AgreementFeeStructure(self):
        result3 = self.pc.agreementFeeStructure()
        self.ts.markFinal("test_ProgramConfiguration", result3, "Agreement Fee Structure Verification")

    @pytest.mark.run(order=16.3)
    def test_ProgramConfiguration_CarveInRules(self):
        result4 = self.pc.carveInRules()
        self.ts.markFinal("test_ProgramConfiguration", result4, "Carve in Rules Verification")

    @pytest.mark.run(order=16.4)
    def test_ProgramConfiguration_Inventory(self):
        result5 = self.pc.inventoryPayment()
        self.ts.markFinal("test_ProgramConfiguration", result5, "Inventory and Payment Management Verification")

    @pytest.mark.run(order=17)
    def test_ProgramPerformance(self):
        result = self.pp.summary()
        self.ts.mark( result, "Program Financial Summary Data Verification")
        result2 = self.pp.pharmacy()
        self.ts.markFinal("test_ProgramPerformance", result2, "Pharmacy Affiliation Data Verification")

    @pytest.mark.run(order=18)
    def test_ReportCenter_HRSA_AuditReport(self):
        self.rc.report_grid()
        result = self.rc.audit_support()
        self.ts.markFinal("test_ReportCenter", result, "HRSA Audit Report Data Verification")

    @pytest.mark.trylast
    def test_logout(self):
        result = self.lc.logout()
        self.ts.markFinal("test_logout", result, "Logout Verification")

