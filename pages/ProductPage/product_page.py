from base.webdriver import SeleniumDriver
from base.basepage import BasePage
import time


class AllProducts(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _add_to_cart = '//*[@id="inventory_container"]/div/div[1]/div[3]/button'
    _selection_ = '//select[@class="product_sort_container"]'
    _product_link = 'item_4_title_link'  # id
    _image_present = '//*[@id="header_container"]//div[contains(text(),"Swag Labs")]'
    _remove_button = '//*[@id="inventory_item_container"]/div/div/div/button'
    _back = '//*[@id="inventory_item_container"]//button[contains(text(),"<- Back")]'
    _cart = '//*[@id="shopping_cart_container"]/a/span'
    _cart_occupied = '//span[@class="fa-layers-counter shopping_cart_badge"]'

    _cart_header = '//div[@class="subheader"]'
    _cart_remove = '//button[@class="btn_secondary cart_button"]'
    _continue_shopping = '//*[@id="cart_contents_container"]/div/div[2]/a[1]'
    _continue_checking = '//*[@id="cart_contents_container"]/div/div[2]/a[2]'

    def find_seletion_(self):
        self.selections(locatorType='xpath', locator=self._selection_, index=1)

    def click_on_cart(self):
        self.elementClick(self._add_to_cart, locatorType="xpath")

    def click_product_link(self):
        self.elementClick(self._product_link)

    def hover_remove_button(self):
        self.hover_me(self._remove_button, locatorType='xpath')

    def return_back(self):
        self.elementClick(self._back, locatorType="xpath")

    def click_filled_cart(self):
        self.elementClick(self._cart_occupied, locatorType="xpath")

    def hover_on_remove_cart(self):
        self.hover_me(self._cart_remove, locatorType="xpath")

    def hover_on_continue(self):
        self.hover_me(self._continue_shopping, locatorType="xpath")

    def click_checkout(self):
        self.elementClick(self._continue_checking, locatorType='xpath')

    def find_products(self):
        self.find_seletion_()
        self.click_on_cart()
        self.click_product_link()
        self.hover_remove_button()
        self.return_back()
        self.click_filled_cart()
        self.hover_on_remove_cart()
        self.hover_on_continue()
        self.click_checkout()

    def is_present(self):
        result = self.isElementPresent(self._selection_)
        return result

    def is_header(self):
        result = self.isElementPresent(self._cart_header)
        return result

    # verifies if image is found after clicking on link on product page
    # def is_image_present(self):
    #     result = self.isElementPresent(self._image_present)
    #     return result
5