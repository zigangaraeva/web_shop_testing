from page_objects.base_page import BasePage
from locators.xpaths import XpathLoginPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)

    def enter_login(self, email):
        self._input(XpathLoginPage.login, email)

    def enter_password(self, password_text):
        self._input(XpathLoginPage.password, password_text)

    def click_login_button(self):
        self._click(XpathLoginPage.login_btn)

    def welcome_page(self):
        self._find_element(XpathLoginPage.welcome_to_store)