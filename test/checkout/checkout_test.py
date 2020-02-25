from selenium import webdriver
import unittest
from pages.checkout_page.checkoutpage import Checkout
import pytest
from utilities.teststatus import TestStatus



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CheckoutTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        # self.p = AllProducts(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def valid_checkout(self):
        baseUrl = "https://www.saucedemo.com/checkout-step-one.html"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        cc = Checkout(driver)
        cc.checkout_cart("chowa", "cross", "99450")
        result = cc.valid_checkout()
        self.ts.markFinal("element_present", result, "element is present")

    @pytest.mark.run(order=1)
    def invalid_checkout(self):
        baseUrl = "https://www.saucedemo.com/checkout-step-one.html"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        cc = Checkout(driver)
        cc.checkout_cart()
        cc.invalid_check()



ff = CheckoutTest()
ff.invalid_checkout()
