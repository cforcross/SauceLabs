from selenium import webdriver
import unittest
from pages.ProductPage.product_page import AllProducts
from utilities.teststatus import TestStatus
import pytest
import time
from test.products.navigation_page import Navigation
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ProductTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        # self.p = AllProducts(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = Navigation(self.driver)

    def set_up(self):
        self.nav.click_three()
        self.nav.navigate_all_about()

    def proucts(self):
        baseUrl = "https://www.saucedemo.com/inventory.html"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.get(baseUrl)

        p = AllProducts(driver)
        p.find_products()

        ts = TestStatus(driver)
        result1 = p.is_present()
        result2 = p.is_header()
        ts.mark(result2, "Header is present")
        ts.markFinal("element_present", result1, "element is present")


ff = ProductTest()
ff.proucts()
