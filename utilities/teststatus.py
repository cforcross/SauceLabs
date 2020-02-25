from base.webdriver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from traceback import print_stack


class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(TestStatus, self)
        super().__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info(f"--------Verification Success {resultMessage}")
                else:
                    self.resultList.append("Fail")
                    self.log.info(f"--------Verification Success {resultMessage}")
                    self.screenShot(resultMessage)
            else:
                self.resultList.append('Fail')
                self.log.error(f"--------Verification Failed:: {resultMessage}")
                self.screenShot(resultMessage)
        except:
            self.resultList.append('Fail')
            self.log.error(f"--------Verification Failed:: {resultMessage}")
            self.screenShot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):

        self.setResult(result, resultMessage)
        print()

    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(f"----TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + "---TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
