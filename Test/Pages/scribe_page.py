from data.data import Data
from pages.base_page import BasePage
from pages.login_page import LogInPage
from utils.locators import AdminDashboardLocator
from utils.locators import ScribePageLocator
from utils.locators import LogsPageLocator
from utils.read_email import *
from time import sleep
import allure
from random import randint


class ScribePage(BasePage):
    def __init__(self, driver):
        self.locator = ScribePageLocator
        self.locatorAdminDashboard = AdminDashboardLocator
        self.locatorLogsPage = LogsPageLocator
        self.data = Data
        super().__init__(driver)

    def login(self):
        page_login = LogInPage(self.driver)
        page_login.logIn(self.data.username, self.data.userPassword)

    def newEmailGenerate(self):
        # newemail = f"{self.data.scribeEmailInitialText}_{randint(0, 100)}"
        # newemail = f"{''.join(random.sample('0123456789', 5))}"
        if self.data.stagingPortal:
            newemail = f"{self.data.scribeEmailInitialText}_{randint (0,99999)}"
        else:
            newemail = f"{self.data.scribeEmailInitialText}_{randint(0, 99999)}{self.data.scribeEmailEndTextaug}"

        return newemail

    def createScribe(self):
        self.clear_field_and_send_keys(self.data.scribeFirstname, *self.locator.firstName)
        sleep(1)
        self.clear_field_and_send_keys(self.data.scribeLastname, *self.locator.lastName)
        sleep(1)
        if self.data.stagingPortal:
            self.clear_field_and_send_keys(self.newEmailGenerate(), *self.locator.emailprefix)
        else:
            self.clear_field_and_send_keys(self.newEmailGenerate(), *self.locator.email)
        sleep(1)
        self.clear_field_and_send_keys(self.data.testScribeId, *self.locator.scribeId)
        sleep(1)
        self.select_by_index(self.data.scribePasswordlimit, *self.locator.passwordLimit)
        sleep(1)
        self.send_data(self.data.scribePartner, *self.locator.partner)
        sleep(1)
        self.click(*self.locator.assignToProviderBtn)
        sleep(1)
        self.click(*self.locator.unassigned)
        sleep(1)
        self.click(*self.locator.createScribe)

    @allure.step("verify scribe creation form")
    def test_C9294_verify_scribe_creation_form(self):
        self.login()
        self.click(*self.locatorAdminDashboard.scribe)
        sleep(2)
        self.click(*self.locatorAdminDashboard.createScribe)
        sleep(15)

        elements = [self.locator.basicInformationSec, self.locator.providerSec,
                    self.locator.authenticationSec, self.locator.selectedProviderSec, self.locator.createScribe]
        messages = ["Basic information section found", "Provider section found", "Authentication section found",
                    "Selected provider section found", "Create scribe button found"]
        for i in range(0, len(elements)):
            self.assert_element_is_displayed(messages[i], *elements[i])

    @allure.step("verify scribe creation form components")
    def test_C9295_verify_scribe_creation_form_components(self):
        self.login()
        self.click(*self.locatorAdminDashboard.scribe)
        sleep(2)
        self.click(*self.locatorAdminDashboard.createScribe)
        sleep(15)

        elements = [self.locator.firstName, self.locator.lastName, self.locator.email, self.locator.phone,
                    self.locator.assignToProviderBtn, self.locator.selectedProvider, self.locator.passwordLimit,
                    self.locator.enforceMFA, self.locator.createScribe]
        messages = ["First name field found", "Last name field found", "Email field found", "phone field found",
                    "assign to provider field found", "selected provider field found", "password limit field found",
                    "enforce MFA field found", "create scribe button found"]
        for i in range(0, len(elements)):
            self.assert_element_is_displayed(messages[i], *elements[i])

    @allure.step("verify email address on scribe createion form")
    def test_C9297_verify_email_address_on_scribe_creation_form(self):
        # TODO: test will be deleted or need to redesign cause: element is divided into two separate element
        self.login()
        self.click(*self.locatorAdminDashboard.scribe)
        sleep(2)
        self.click(*self.locatorAdminDashboard.createScribe)
        sleep(10)
        self.clear_field_and_send_keys(self.data.scribeFirstname, *self.locator.firstName)
        sleep(1)
        self.clear_field_and_send_keys(self.data.scribeLastname, *self.locator.lastName)
        sleep(1)
        self.clear_field_and_send_keys(self.data.scribeInvalidEmail, *self.locator.email)
        sleep(1)
        self.click(*self.locator.createScribe)
        val = self.get_attribute_value(self.data.classAttribute, *self.locator.email)
        assert self.data.classError in val
        print("invalid email alert found ")
        sleep(1)

    @allure.step("verify upload image on scribe createion form")
    def test_C9298_verify_upload_image_on_scribe_creation_form(self):
        self.login()
        self.click(*self.locatorAdminDashboard.scribe)
        sleep(2)
        self.click(*self.locatorAdminDashboard.createScribe)
        sleep(15)
        self.send_data(self.data.providerImagePath, *self.locator.UploadImage)
        sleep(3)
        print('User Image updated')
        self.assert_get_attribute_value(False, self.data.srcAttribute, self.data.scribeDemoImageName, *self.locator.scribeImage)
        print('image source file name changed')
        sleep(2)
        self.click(*self.locator.deleteImage)
        print('image deleted')
        sleep(2)
        self.send_data(self.data.providerFourMBImagePath, *self.locator.UploadImage)
        sleep(1)
        self.assert_get_text(True, self.data.largerImageAlert, *self.locator.largerImageAlert)
        print(self.data.largerImageAlert + " alert message found")

    @allure.step("verify phone number on scribe createion form")
    def test_C9299_verify_phone_number_on_scribe_creation_form(self):
        self.login()
        self.click(*self.locatorAdminDashboard.scribe)
        sleep(2)
        self.click(*self.locatorAdminDashboard.createScribe)
        sleep(15)
        self.send_data(self.data.scribeInvalidPhoneNumber, *self.locator.phone)
        self.assert_get_attribute_value(True, self.data.valueAttribute, self.data.scribeEmptyPhone, *self.locator.phone)
        print('Cant input invalid characters in phone field')
        sleep(2)
        self.send_data(self.data.scribePhoneNumber, *self.locator.phone)
        sleep(1)
        self.assert_get_attribute_value(True, self.data.valueAttribute, self.data.scribePhoneNumber, *self.locator.phone)
        print('Can input valid characters in phone field')

    @allure.step("verify password limitation form")
    def test_C9300_verify_password_limitation_on_scribe_creation_form(self):
        self.login()
        self.click(*self.locatorAdminDashboard.scribe)
        sleep(2)
        self.click(*self.locatorAdminDashboard.createScribe)
        sleep(10)

        list1 = self.get_list_of_dropdown_element(*self.locator.passwordLimit)
        list_int = list1
        list_int = list(map(int, list_int))
        res = all(2 <= ele <= 10 for ele in list_int)
        assert res is True
        val = self.get_num__of_dropdown_element(*self.locator.passwordLimit)
        list2 = []
        for i in range(0, val):
            self.select_by_index(i, *self.locator.passwordLimit)
            val = self.get_active_option_of_dropdown_element(*self.locator.passwordLimit)
            list2.append(val)
            sleep(1)
        print('password  limit options: ', list1, sep='\n')
        print('Selected password limit options', list2, sep='\n')
        assert list1 == list2

    @allure.step("verify successfully create scribe")
    def test_C9301_verify_successfully_create_scribe(self):
        self.login()
        self.click(*self.locatorAdminDashboard.scribe)
        sleep(2)
        self.click(*self.locatorAdminDashboard.createScribe)
        sleep(10)
        elements = [self.locator.firstName, self.locator.lastName, self.locator.emailprefix,
                    self.locator.scribeId]

        elements_input = [self.data.scribeFirstname, self.data.scribeLastname, self.data.scribeEmailInitialText,
                          self.data.testScribeId]
        # TODO: more elements need to be asserted. cant replicate scenario manually due to bug(latest changes in site)
        for i in range(len(elements)):
            self.click(*self.locator.createScribe)
            sleep(1)
            val = self.get_attribute_value(self.data.classAttribute, *elements[i])
            print(val)
            assert self.data.classError in val
            self.send_data(elements_input[i], *elements[i])

        # # TODO: need to change it if select option increases
        # self.get_list_of_dropdown_element(*self.locator.domain)
        # self.get_text(*self.locator.domain)

        self.createScribe()
        sleep(1)
        val = self.get_text(*self.locator.scribeCreateSuccessMessage)
        print(val + ' message found')
        self.assert_get_text(True, self.data.createScribeSuccessMessage, *self.locator.scribeCreateSuccessMessage)

    @allure.step("verify email upon successfully create scribe")
    def test_C9302_verify_email_upon_successfully_create_scribe(self):
        self.login()
        self.click(*self.locatorAdminDashboard.scribe)
        sleep(2)
        self.click(*self.locatorAdminDashboard.createScribe)
        sleep(10)
        self.createScribe()
        sleep(1)
        val = self.get_text(*self.locator.scribeCreateSuccessMessage)
        print(val + ' message found')
        self.assert_get_text(True, self.data.createScribeSuccessMessage, *self.locator.scribeCreateSuccessMessage)
        sleep(10)

        # verify email
        try:
            service = connectgmailApi()
            email = getlastestmail(service)
            # email = {'id': '17a5ca5f5f4bd0aa', 'threadId': '17a5b1bb861b3bc2'}
            # print(email)
            emailbody = getemailbody(service, email)
            # print(emailbody)
            assert self.data.scribeEmailSubject == emailbody[0]
            assert self.data.adminName in emailbody[1]
            print(self.data.scribeEmailSubject + " found in message subject")
            print("admin name found in message body ")
        except:
            print('Error reading email body from gmail')

    @allure.step("verify scribe ID in_scribe_form")
    def test_C76131_verify_scribeID_in_scribe_form(self):
        self.login()
        # Get non-unique ScribeID
        self.click(*self.locatorAdminDashboard.log)
        sleep(1)
        self.click(*self.locatorAdminDashboard.scribeLogs)
        sleep(10)

        list1 = self.get_text_of_multiple_element(*self.locatorLogsPage.uniqueId)
        print(list1)
        list1 = list(set(list1))
        print(list1)
        try:
            list1.remove(self.data.testScribeId)
        except:
            pass
        print(list1)
        nonUniqueScribeId = ''
        for i in range(len(list1)):
            if list1[i] is not None:
                nonUniqueScribeId = list1[i]
                break
        print(nonUniqueScribeId)
        self.click(*self.locatorAdminDashboard.scribe)
        sleep(1)
        self.click(*self.locatorAdminDashboard.createScribe)
        sleep(10)

        # Fill out necessary fields
        self.clear_field_and_send_keys(self.data.scribeFirstname, *self.locator.firstName)
        sleep(1)
        self.clear_field_and_send_keys(self.data.scribeLastname, *self.locator.lastName)
        sleep(1)
        self.click(*self.locator.assignToProviderBtn)
        sleep(1)
        self.click(*self.locator.unassigned)
        sleep(1)
        if self.data.stagingPortal:
            self.clear_field_and_send_keys(self.newEmailGenerate(), *self.locator.emailprefix)
            sleep(1)
            self.send_data(self.data.scribePartner, *self.locator.partner)
        else:
            self.clear_field_and_send_keys(self.newEmailGenerate(), *self.locator.email)
        sleep(1)

        # Empty field
        self.click(*self.locator.createScribe)
        val = self.get_attribute_value(self.data.classAttribute, *self.locator.scribeId)
        assert self.data.classError in val
        print("Fill out alert found ")

        # Invalid ScribeID input
        self.clear_field_and_send_keys(self.data.invalidScribeId, *self.locator.scribeId)
        sleep(1)
        val = self.get_attribute_value(self.data.classAttribute, *self.locator.scribeId)
        assert self.data.classError in val
        print("Invalid format alert found ")

        # Non-unique ScribeID input
        self.clear_field_and_send_keys(nonUniqueScribeId, *self.locator.scribeId)
        sleep(1)
        self.click(*self.locator.createScribe)
        val = self.get_text(*self.locator.statusMessage)
        print(val + ' message found')
        self.assert_get_text(True, self.data.nonUniqueScribeIdAlert, *self.locator.statusMessage)

        # valid input
        self.clear_field_and_send_keys(self.data.testScribeId, *self.locator.scribeId)
        sleep(1)
        val = self.get_attribute_value(self.data.classAttribute, *self.locator.scribeId)
        assert self.data.classSuccess in val
        print("Filled out with valid ScribeId ")
        self.click(*self.locator.createScribe)
        val = self.get_text(*self.locator.scribeCreateSuccessMessage)
        print(val + ' message found')
        self.assert_get_text(True, self.data.createScribeSuccessMessage, *self.locator.scribeCreateSuccessMessage)

        # TODO: log assertion
        self.click(*self.locatorAdminDashboard.scribe)
        sleep(1)
        self.click(*self.locatorAdminDashboard.createScribe)
        sleep(10)
