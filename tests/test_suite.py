import unittest
from tests.test_registration import TestRegistration
from tests.test_browsing import TestBrowsing
from tests.test_cart_management import TestCartManagement
from tests.test_payment_processing import TestPaymentProcessing
from tests.test_order_tracking import TestOrderTracking

class TestSuite(unittest.TestSuite):
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestRegistration('test_user_registration'))
        suite.addTest(TestBrowsing('test_product_browsing'))
        suite.addTest(TestCartManagement('test_cart_management'))
        suite.addTest(TestPaymentProcessing('test_payment_processing'))
        suite.addTest(TestOrderTracking('test_order_tracking'))
        return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestSuite().suite())
