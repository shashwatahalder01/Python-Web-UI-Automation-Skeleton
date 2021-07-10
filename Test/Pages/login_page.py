from data.data import Data
from pages.base_page import BasePage
from utils.locators import LogInPageLocator
from utils.locators import AdminDashboardLocator
from time import sleep
import allure


class LogInPage(BasePage):
    def __init__(self, driver):
        self.locator = LogInPageLocator
        self.locatorAdminDashboardPage = AdminDashboardLocator
        self.data = Data
        super().__init__(driver)

    def logIn(self, email, password):
        self.clear_field_and_send_keys(email, *self.locator.email)
        sleep(1)
        self.clear_field_and_send_keys(password, *self.locator.password)
        sleep(1)
        self.click(*self.locator.loginIn)
        sleep(5)
        print('successfully logged-In')

    def invalid_logIn(self, email, password):
        self.clear_field_and_send_keys(email, *self.locator.email)
        sleep(1)
        self.clear_field_and_send_keys(password, *self.locator.password)
        sleep(1)
        self.click(*self.locator.loginIn)

    def logout(self):
        self.click(*self.locatorAdminDashboardPage.username)
        sleep(2)
        self.click(*self.locatorAdminDashboardPage.logOut)
        print('successfully logged-out')

    @allure.step("verify super admin and can login with correct credential")
    def test_C9192_verify_super_admin_login_with_correct_credential(self):

        self.logIn(self.data.username, self.data.userPassword)
        sleep(1)
        res = self.element_is_displayed(*self.locatorAdminDashboardPage.dashboard)
        assert res is True
        print('Dashboard found in admin Dashboard page')
        res = self.element_is_displayed(*self.locatorAdminDashboardPage.username)
        assert res is True
        print('User menu found in admin Dashboard page')

    @allure.step("verify super admin cannot login with invalid credential")
    def test_C9193_verify_super_admin_cannot_login_with_invalid_credential(self):

        email = [self.data.incorrectUsername, self.data.username,  self.data.incorrectUsername]
        password = [self.data.incorrectUserPassword, self.data.incorrectUserPassword, self.data.userPassword]

        for i in range(3):
            self.invalid_logIn(email[i], password[i])
            res = self.element_is_displayed(*self.locator.loginAlert)
            assert res is True
            print('Error message shown')
            sleep(3)

    @allure.step("verify super admin don't get blocked for max invalid login attempts")
    def test_C9194_verify_super_admin_dont_get_blocked_for_max_invalid_login_attempts(self):

        for _ in range(10):
            self.invalid_logIn(self.data.incorrectUsername, self.data.incorrectUserPassword)
            sleep(1)

        self.logIn(self.data.username, self.data.userPassword)
        res = self.element_is_displayed(*self.locatorAdminDashboardPage.dashboard)
        assert res is True
        print('Dashboard found in admin Dashboard page')
        res = self.element_is_displayed(*self.locatorAdminDashboardPage.username)
        assert res is True
        print('User menu found in admin Dashboard page')
