from base.basepage import BasePage


class Navigation(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    #locators
    _three = '//button[contains(text(),"Open Menu")]'
    _all_items = 'inventory_sidebar_link'
    _about = 'about_sidebar_link'
    _logout = 'logout_sidebar_link'
    _reset_app_state = 'reset_sidebar_link'
    _cross = 'Close Menu'

    def click_three(self):
        self.elementClick(self._three, locatorType="xpath")

    def navigate_all_items(self):
        self.elementClick(self._all_items)

    def navigate_all_about(self):
        self.elementClick(self._about)

    def navigate_logout(self):
        self.elementClick(self._logout)

    def click_cross(self):
        self.elementClick(self._cross, locatorType="link")

