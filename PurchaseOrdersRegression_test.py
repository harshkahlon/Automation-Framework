import pytest
import unittest
from utils.status import Status
import time
from utils import env as utils
from pages.Login.LoginPage import LoginPage
from pages.Smart.WelcomeSmart import WelcomeSmart
from pages.Smart.FacilityDropdown import FacilityDropdown
from pages.Smart.Graphs import Graphs
from pages.Smart.PurchaseOrder import PurchaseOrders
from pages.Logout.SmartLogoutPage import SmartLogoutPage


@pytest.mark.usefixtures("test_setup")
class TestSmartPHIAccess(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, test_setup):
        driver = self.driver
        self.lp = LoginPage(self.driver)
        self.ws = WelcomeSmart(self.driver)
        self.fd = FacilityDropdown(self.driver)
        self.gs = Graphs(self.driver)
        self.purchase = PurchaseOrders(self.driver)
        self.lg = SmartLogoutPage(self.driver)
        self.ts = Status(self.driver)



    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.enterUsername(utils.adminUSERNAME)
        self.lp.enterpassword(utils.adminPASSWORD)
        self.lp.clickSignin()
        result = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result, "Valid Login Verification")

    @pytest.mark.run(order=2)
    def test_SmartWelcomePage(self):
        result = self.ws.welcome_smart()
        self.ts.markFinal("test_SmartWelcomePage", result, "Smart Welcome Page Verification")

    @pytest.mark.run(order=3)
    def test_FacilityDropDown(self):
        result = self.fd.facility_dropdown()
        self.ts.markFinal("test_FacilityDropDown", result, "Facility: and Alert box Verification")

    @pytest.mark.run(order=4)
    def test_SimulatedPO_Create(self):
        result = self.purchase.createSimulatedPO()
        self.ts.markFinal("test_NewPurchaseOrder", result, "Create Simulated PO Verification")

    @pytest.mark.run(order=5)
    def test_SimulatedPO_AddLineItem(self):
        result = self.purchase.simulatedPO_AddLineItem()
        self.ts.markFinal("test_NewPurchaseOrder", result, "Simulated PO Add Line Item Verification")

    @pytest.mark.run(order=6)
    def test_SimulatedPO_DeleteLineItem(self):
        result = self.purchase.simulatedPO_DeleteLineItem()
        self.ts.markFinal("test_NewPurchaseOrder", result, "Delete Simulated PO Line Item Verification")

    @pytest.mark.run(order=7)
    def test_SimulatedPO_GlobalDelete(self):
        result = self.purchase.simulatedPO_GlobalDelete()
        self.ts.markFinal("test_NewPurchaseOrder", result, "Global Delete Simulated PO Verification")

    @pytest.mark.run(order=8)
    def test_UploadPO_File(self):
        result = self.purchase.upload_PO_file()
        self.ts.markFinal("test_NewPurchaseOrder", result, "Upload PO File Verification")

    @pytest.mark.trylast
    def test_logout(self):
        result = self.lg.smart_logout()
        self.ts.markFinal("test_SmartLogout", result, "Smart Log Out Successful")