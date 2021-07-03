from pages.base_page import BasePage
from utils.locators import SignInPageLocator


class SignInPage(BasePage):
    def __init__(self, driver):
        self.locator = SignInPageLocator
        super().__init__(driver)

    def signIn(self, email, password):

        self.find_element(*self.locator.email).send_keys(email)
        self.find_element(*self.locator.password).send_keys(password)
        self.find_element(*self.locator.signIn).click()

    def test_signin(self):

        self.signIn(email,password)
