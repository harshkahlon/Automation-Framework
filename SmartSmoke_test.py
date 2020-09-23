import pytest
import unittest
from utils.status import Status
import time
from utils import env as utils
from pages.Login.LoginPage import LoginPage
from pages.Smart.WelcomeSmart import WelcomeSmart
from pages.Smart.FacilityDropdown import FacilityDropdown
from pages.Smart.Graphs import Graphs
from pages.Logout.SmartLogoutPage import SmartLogoutPage
from pages.Smart.ErrorsDetection import ErrorDetection
from pages.Smart.GlobalSettings import GlobalSets
from pages.Smart.Settings import UserSets
from pages.Smart.ReportCenter import RepoCntr
from pages.Smart.Actvty import Actvty
from pages.Smart.ChargeMaster import ChargeMaster
from pages.Smart.Purchasing import Purchase
from pages.Smart.DispenseHistory import DispenseHistory

@pytest.mark.usefixtures("test_setup")
class TestSmartPHIAccess(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, test_setup):
        driver = self.driver
        self.lp = LoginPage(self.driver)
        self.ws = WelcomeSmart(self.driver)
        self.fd = FacilityDropdown(self.driver)
        self.gs = Graphs(self.driver)
        self.ts = Status(self.driver)
        self.ed = ErrorDetection(self.driver)
        self.gb = GlobalSets(self.driver)
        self.us = UserSets(self.driver)
        self.rs = RepoCntr(self.driver)
        self.act = Actvty(self.driver)
        self.cm = ChargeMaster(self.driver)
        self.pr = Purchase(self.driver)
        self.dh = DispenseHistory(self.driver)

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
    def test_Graphs(self):
        result = self.gs.facility_graphs()
        self.ts.markFinal("test_Graphs", result, "Entity Graphs Chart Verification")

    @pytest.mark.run(order=5)
    def test_ChargeMaster_Mapping_Grid(self):
        result = self.cm.Mapping_Grid()
        self.ts.markFinal("test_ChargeMaster", result, "Mapping Grid Data Verification")

    @pytest.mark.run(order=6)
    def test_ChargeMaster_Charge_Code_Detail(self):
        result = self.cm.Charge_Code_Detail()
        self.ts.markFinal("test_ChargeMaster", result, "Charge Cod Detail Grid Data Verification")

    @pytest.mark.run(order=7)
    def test_ChargeMaster_NDC_Detail(self):
        result = self.cm.NDC_Detail()
        self.ts.markFinal("test_ChargeMaster", result, "NDC Detail Grid Data Verification")

    @pytest.mark.run(order=8)
    def test_ChargeMaster_Unmapped_Charge_Code(self):
        result = self.cm.Unmapped_Charge_Code()
        self.ts.markFinal("test_ChargeMaster", result, "Unmapped Charge Code Grid Data Verification")

    @pytest.mark.run(order=9)
    def test_ChargeMaster_Unmapped_NDCs(self):
        result = self.cm.Unmapped_NDCs()
        self.ts.markFinal("test_ChargeMaster", result, "Unmapped NDC Grid Data Verification")

    @pytest.mark.run(order=10)
    def test_ChargeMaster_Blocked_NDC_List(self):
        result = self.cm.Blocked_NDC_List()
        self.ts.markFinal("test_ChargeMaster", result, "Blocked NDC Grid Data Verification")

    @pytest.mark.run(order=11)
    def test_Activty_Purchase_History(self):
        result = self.act.Purchase_History()
        self.ts.markFinal("test_Activty", result, "Activity Data Verification")

    @pytest.mark.run(order=11.1)
    def test_Activity_DispenseHistory(self):
        result = self.dh.dispense_history()
        self.ts.markFinal("test_Dispense History", result, "Dispense History Verification")

    @pytest.mark.run(order=11.2)
    def test_Activity_DispenseHistory_InfoIcon(self):
        result = self.dh.info_icon()
        self.ts.markFinal("test_Dispense History", result, "Dispense History Info Icon Tab's Verification")

    @pytest.mark.run(order=12)
    def test_Activty_Patient_Details(self):
        result = self.act.Patient_Details()
        self.ts.markFinal("test_Activty", result, "Activity Patient Details Data Verification")

    @pytest.mark.run(order=13)
    def test_Activty_Prescriber_Details(self):
        result = self.act.Prescriber_Details()
        self.ts.markFinal("test_Activty", result, "Activity Prescriber Details Data Verification")

    @pytest.mark.run(order=14)
    def test_Activty_Drug_Dispense(self):
        result = self.act.Drug_Dispense()
        self.ts.markFinal("test_Activity", result, "Activity Drug Dispense Data Verification")

    @pytest.mark.run(order=15)
    def test_Purchase_Accum(self):
        result = self.pr.Accum()
        self.ts.markFinal("test_Purchase_Accumulator", result, "Accumulator Data Verification")

    @pytest.mark.run(order=16)
    def test_Purchase_Penny_Buys(self):
        result = self.pr.Penny_Buys()
        self.ts.markFinal("test_Purchase_Penny_Buys", result, "Penny Buys Data Verification")

    @pytest.mark.run(order=17)
    def test_Purchase_Direct_Purchase_Entry(self):
        result = self.pr.Direct_Purchase_Entry()
        self.ts.markFinal("test_Purchase_Direct_Purchase_Entry", result, "Direct Purchase Entry Data Verification")

    @pytest.mark.run(order=18)
    def test_Settings_Dispense_Location_Setup(self):
        result = self.us.Dispense_Location_Setup()
        self.ts.markFinal("test_Settings", result, "Dispense Location Setup Data Verification")

    @pytest.mark.run(order=19)
    def test_Settings_Dispense_Location_Show_Inactive(self):
        result = self.us.Dispense_Location_setup_ShowInactive()
        self.ts.markFinal("test_Settings", result, "Patient Visit Location Inactive Data Verification")

    @pytest.mark.run(order=20)
    def test_Settings_Dispense_Location_ShowAll(self):
        result = self.us.Dispense_Location_ShowAll()
        self.ts.markFinal("test_Settings", result, "Dispense Location All Data Verification")

    @pytest.mark.run(order=21)
    def test_Settings_Prescriber_Setup(self):
        result = self.us.Prescriber_Setup()
        self.ts.markFinal("test_Settings", result, "Prescriber Setup Data Verification")

    @pytest.mark.run(order=22)
    def test_Settings_Prescriber_Setup_Inelig(self):
        result = self.us.Prescriber_Setup_Ineligilible()
        self.ts.markFinal("test_Settings", result, "Ineligible Prescriber Data Verification")

    @pytest.mark.run(order=23)
    def test_Settings_Prescriber_SetupAll(self):
        result = self.us.Prescriber_Setup_all()
        self.ts.markFinal("test_Settings", result, "All Prescriber Data Verification")

    @pytest.mark.run(order=24)
    def test_Settings_Patient_Visit_Location_Setup(self):
        result = self.us.Patient_Visit_Location_Setup()
        self.ts.markFinal("test_Settings", result, "Patient Visit Location Setup Data Verification")

    @pytest.mark.run(order=25)
    def test_Settings_Patient_Visit_Location_Show_Inactive(self):
        result = self.us.Patient_Visit_location_ShowInactive()
        self.ts.markFinal("test_Settings", result, "Patient Visit Location Inactive Data Verification")

    @pytest.mark.run(order=26)
    def test_Settings_Patient_Visit_Location_ShowAll(self):
        result = self.us.Patient_Visit_Location_ShowAll()
        self.ts.markFinal("test_Settings", result, "Patient Visit Show All Data Verification")

    @pytest.mark.run(order=27)
    def test_Settings_Patient_Class_Setup(self):
        result = self.us.Patient_Class_Setup()
        self.ts.markFinal("test_Settings", result, "Patient Class Setup Data Verification")

    @pytest.mark.run(order=28)
    def test_Settings_Blocked_NDC_Setup(self):
        result = self.us.Blocked_NDC_Setup()
        self.ts.markFinal("test_Settings", result, "Blocked NDC Setup Data Verification")

    @pytest.mark.run(order=29)
    def test_Settings_PayerCode_Setup(self):
        result = self.us.Payer_Code_Setup()
        self.ts.markFinal("test_Settings", result, "Payer Code Setup Data Verification")

    @pytest.mark.run(order=30)
    def test_ErrorDetection_Unrecognized_Prescribers(self):
        result = self.ed.Unrecognized_Prescribers()
        self.ts.markFinal("test_ErrorDetection", result, "Unrecognized Prescribers Data Verification")

    @pytest.mark.run(order=31)
    def test_ErrorDetection_Unrecognized_Payer(self):
        result = self.ed.Unrecognized_Payers()
        self.ts.markFinal("test_ErrorDetection", result, "Unrecognized Payers Data Verification")

    @pytest.mark.run(order=32)
    def test_ErrorDetection_Pending_Accumulation(self):
        result = self.ed.Pending_Accumulation_Queue()
        self.ts.markFinal("test_ErrorDetection", result, "Pending Accumulation Data Verification")

    @pytest.mark.run(order=33)
    def test_ReportCenter(self):
        result = self.rs.Reporting_Dropdown()
        self.ts.markFinal("test_ReportCenter", result, "User History By Facility Data Verification")

    @pytest.mark.run(order=34)
    def test_GlobalSettings_Orphan_Drug_Management(self):
        result = self.gb.Orphan_Drug_Management()
        self.ts.markFinal("test_GlobalSettings", result, "Orphan Drug Management Data Verification")

    @pytest.mark.run(order=35)
    def test_GlobalSettings_Orphan_Drug_Designations(self):
        result = self.gb.Orphan_Drug_Designations()
        self.ts.markFinal("test_GlobalSettings", result, "Orphan Drug Designations Data Verification")

    @pytest.mark.run(order=36)
    def test_GlobalSettings_UOMperUOI_Managements(self):
        result = self.gb.UOM_per_UOI_Managements()
        self.ts.markFinal("test_GlobalSettings", result, "UOM per UOI Managements Data Verification")

    @pytest.mark.run(order=37)
    def test_GlobalSettings_UOMperUOI_Mismatched(self):
        result = self.gb.UOM_per_UOI_Mismatch()
        self.ts.markFinal("test_GlobalSettings", result, "UOM per UOI Managements Mismatched Data Verification")

    @pytest.mark.run(order=38)
    def test_GlobalSettings_UOMperUOI_Showall(self):
        result = self.gb.UOM_per_UOI_Showall()
        self.ts.markFinal("test_GlobalSettings", result, "UOM per UOI Managements ShowAll Data Verification ")

    @pytest.mark.run(order=39)
    def test_GlobalSettings_Payer_Code_Management(self):
       result = self.gb.Payer_Code_Management()
       self.ts.markFinal("test_GlobalSettings", result, "Payer Code Managements Data Verification")

    def test_logout(self):
        driver = self.driver
        logout = SmartLogoutPage(driver)
        logout.smart_logout()


