"""
Creates a webdriver instance based on driver configuration

"""

from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser


    def getWebDriverInstance(self):
        baseURL = "https://www.saucedemo.com/index.html"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver