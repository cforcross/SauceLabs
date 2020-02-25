from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
import utilities.custom_logger as cl
from selenium.webdriver import ActionChains
import logging
import time
import os


class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +
                           " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("Cannot click on the element with locator: " + locator +
                           " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("Cannot send data on the element with locator: " + locator +
                           " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.error("Element not found")
                return False
        except:
            self.log.error("Element not found")
            return False

    def elementPresenceCheck(self, locator, locatorType="xpath"):
        try:
            elementList = self.getElement(locator, locatorType)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.error("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    # using dropdown to select options
    def selections(self, locator, locatorType, index=" ", value="", text=" "):
        try:
            element = self.getElement(locator, locatorType)
            sel = Select(element)
            if sel.select_by_index(index):
                self.log.info(f"found selectiion with index {index} locator: {locator} and locatortype: {locatorType}")
            elif sel.select_by_value(value):
                self.log.info(f"found selectiion with value {value}  locator: {locator} and locatortype: {locatorType}")
            elif sel.select_by_visible_text(text):
                self.log.info(f"found selectiion with text {text} locator: {locator} and locatortype: {locatorType}")
            else:
                self.log.error("selector not found")
        except NoSuchElementException:
            print("exception error raised")
            print_stack()

    # hovers over element
    def hover_me(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            time.sleep(1)
            self.log.info(f"Hovered on element with locator {locator} and locatorType {locatorType}")
        except ElementNotInteractableException:
            self.log.error(f"Could not hover on element with locator {locator} and locatorType {locatorType}")

    # finds all() anchor tags on page
    def anchor_tags(self):
        element = self.driver.find_elements_by_tag_name('a')
        for i in element:
            print(i.get_attribute('href'))

    # gets the title
    def gettitle(self):
        return self.driver.title

    # Takes screenshot when they is an error
    def screenShot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotdirectory = "../screenshots/"
        relativeFileName = screenshotdirectory + fileName
        currentdirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentdirectory, relativeFileName)
        destinationDirectory = os.path.join(currentdirectory, screenshotdirectory)
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("screenshot saved  to director" + destinationFile)
        except:
            self.log.error("####Exception Occured")
            print_stack()
