from base.basepage import BasePage


class HomeLog(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator
    _username = 'user-name'
    _password = 'password'
    _login = '//*[@id="login_button_container"]/div/form/input[3]'
    _verity = '//div[@class="product_label"]'
    _all_images = '//img[@class="inventory_item_img"]'
    _invalid_user = '//*[@id="login_button_container"]//button[contains(text(),"")]'

    def get_user(self, name):
        self.sendKeys(name, self._username, locatorType="id")

    def get_password(self, password):
        self.sendKeys(password, self._password, locatorType="id")

    def login(self):
        self.elementClick(self._login, locatorType='xpath')

    def log_in(self, name=" ", password=" "):
        self.get_user(name)
        self.get_password(password)
        self.login()

    #checks all pictures are present
    def verify(self):
        result = self.isElementPresent(self._verity)
        return result

    # def all_images(self):
    #     result = self.elementPresenceCheck(self._all_images)
    #     return result

    def verify_login_fail(self):
        result = self.isElementPresent(self._invalid_user)
        return result

    def verify_login_title(self):
        return self.verifyPageTitle('excess') #im delibarately failing this












