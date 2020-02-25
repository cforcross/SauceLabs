from base.basepage import BasePage


class Checkout(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # locators

    _first_name = 'first-name'
    _last_name = 'last-name'
    _postal_code = 'postal-code'
    _continue = '//input[@class = "btn_primary cart_button"]'
    _cancel = '//a[contains(text(),"CANCEL")]'

    _valid_ = '//div[contains(text(),"Checkout")]'

    # invalid_locator
    _error_message = '//*[@id="contents_wrapper"]/div[2]]'

    _finish_ = '//a[@class="btn_action cart_button"]'

    def enter_first_name(self, name):
        self.sendKeys(name, self._first_name)

    def enter_last_name(self, last):
        self.sendKeys(last, self._last_name)

    def enter_postal(self, postal):
        self.sendKeys(postal, self._postal_code)

    def click_continue(self):
        self.elementClick(self._continue, locatorType="xpath")

    def hover_cancel(self):
        self.hover_me(self._cancel, locatorType="xpath")

    def click_finish(self):
        self.elementClick(self._finish_, locatorType='xpath')

    def checkout_cart(self, name=" ", last=" ", postal=" "):
        self.enter_first_name(name)
        self.enter_last_name(last)
        self.enter_postal(postal)
        self.hover_cancel()
        self.click_continue()
        self.click_finish()

    def valid_checkout(self):
        result = self.isElementPresent(self._valid_)
        return result

    def invalid_check(self):
        result = self.isElementPresent(self._error_message)
        return result
