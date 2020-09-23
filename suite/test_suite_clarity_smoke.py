import unittest
from tests.login_test import TestLoginPage
from tests.ClaritySmoke_test import TestEntityWithPHIAccess


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLoginPage)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestEntityWithPHIAccess)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
