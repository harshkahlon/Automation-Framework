import unittest
from tests.ClaritySmoke_test import TestEntityWithPHIAccess
from tests.SmartSmoke_test import TestSmarthPHIAccess
import HtmlTestRunner


# class ClaritySmokeTest(unittest.TestCase):
#
#     def Clarity_Smoke_Test_Results(self):
#         Clarity_Smoke_Test_Results = unittest.TestSuite()
#         Clarity_Smoke_Test_Results.addTest(unittest.TestLoader().loadTestsFromTestCase(TestEntityWithPHIAccess))
#         Clarity_Smoke_Test_Results.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSmarthPHIAccess))
#         return Clarity_Smoke_Test_Results
#
#
# if __name__ == '__main__':
#     unittest.main(
#         testRunner=HtmlTestRunner.HTMLTestRunner(output='//nfs201/Dev/TeamCity/SileniumTesting/reports', verbosity=2,
#                                                  descriptions= 'Test',
#                                                  report_title='Clarity and Smart  Smoke Test Report'))


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestEntityWithPHIAccess)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestSmarthPHIAccess)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)