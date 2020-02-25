import unittest
from selenium import webdriver
from pages.home_page.home_login import HomeLog
import time
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hP = HomeLog(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def valid_login(self):
        self.hP.log_in('standard_user', 'secret_sauce')

        result1 = self.hP.verify_login_title()
        self.ts.mark(result1, "Title is correct")

        result2 = self.hP.verify()
        self.ts.markFinal(result2, 'test validlogin', "very succesufl")

    @pytest.mark.run(order=1)
    def invalid_login(self):
        self.hP.log_in()
        result1 = self.hP.verify_login_fail()
        self.ts.mark(result1, "Title is wrong")


ff = PageTest()
ff.invalid_login()
