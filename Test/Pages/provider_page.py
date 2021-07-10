from data.data import Data
from pages.base_page import BasePage
from pages.login_page import LogInPage
from utils.locators import AdminDashboardLocator
from utils.locators import LogInPageLocator
from utils.locators import ProviderPageLocator
from time import sleep
import allure


class ProviderPage(BasePage):
    def __init__(self, driver):
        self.locator = ProviderPageLocator
        self.locatorAdminDashboard = AdminDashboardLocator
        self.locatorLogInPage = LogInPageLocator
        self.data = Data
        super().__init__(driver)

    def login(self):
        page_login = LogInPage(self.driver)
        page_login.logIn(self.data.username, self.data.userPassword)

    # Create Provider
    @allure.step("verify provider creation form")
    def test_C9269_verify_provider_creation_form(self):

        self.login()

        # For staging portal
        if self.data.stagingPortal:
            self.click(*self.locatorAdminDashboard.provider)
        sleep(2)

        self.click(*self.locatorAdminDashboard.createProvider)
        sleep(3)

        print('Basic details section found')
        print('contact information section found')
        print('security section found')
        print('app settings section found')
        print('create provider button found')
        elements = [self.locator.basicDetails,  self.locator.contactInformation, self.locator.security,
                    self.locator.appSettings, self.locator.createProvidersubmit]
        messages = ["Basic details section found", "contact information section found", "security section found",
                    "app settings section found", "create provider button found"]

        for i in range(0, len(elements)):
            self.assert_element_is_displayed(messages[i], *elements[i])

        val = self.get_text(*self.locator.firstName)
        assert val == ''
        val = self.get_text(*self.locator.lastName)
        assert val == ''
        val = self.get_text(*self.locator.email)
        assert val == ''
        print('Provider creation forms found with blank fields')

    @allure.step("verify provider creation form components")
    def test_C9270_verify_provider_creation_form_components(self):

        self.login()

        # For staging portal
        if self.data.stagingPortal:
            self.click(*self.locatorAdminDashboard.provider)
        sleep(2)

        self.click(*self.locatorAdminDashboard.createProvider)
        sleep(3)
        elements = [self.locator.basicDetails, self.locator.contactInformation, self.locator.security, self.locator.network,
                    self.locator.appSettings, self.locator.createProvidersubmit, self.locator.imageElement, self.locator.firstName,
                    self.locator.lastName, self.locator.email, self.locator.site, self.locator.timezone, self.locator.uniqueId,
                    self.locator.sendRegistrationEmail, self.locator.disableP2PConnection, self.locator.securitySettings, self.locator.onboarding,
                    self.locator.phone, self.locator.disableIdAuthViaEmail, self.locator.idVerificationTooltip, self.locator.passwordHistoryLimit,
                    self.locator.augmedixNoteWriter, self.locator.automaticContinuity, self.locator.twoWayCommunication, self.locator.ehrIntegration,
                    self.locator.customerScheduler]

        messages = ["Basic details section found", "contact information section found", "security section found", 'network section found',
                    "app settings section found", "create provider button found", 'image upload component found', 'first name component found',
                    'lastName component found', 'email component found', 'site component found', 'timezone component found', 'uniqueId component found',
                    'send registration Email component found', 'Peer-to-peer(P2P) connection component found', 'security Settings component found', 'onboarding component found',
                    'phone component found', 'Identity authentication via email component found', 'tooltip component found', 'password History Limit component found',
                    'augmedix NoteWriter component found', 'automatic Continuity  feature component found', 'two way communication feature component found',
                    'ehr Integration feature component found', 'Field test enrollment checkbox found']

        for i in range(0, len(elements)):
            print(i)
            self.assert_element_is_displayed(messages[i], *elements[i])

    @allure.step("verify access features on provider creation form")
    def test_C9271_verify_access_features_on_provider_creation_form(self):

        self.login()

        # For staging portal
        if self.data.stagingPortal:
            self.click(*self.locatorAdminDashboard.provider)
        sleep(2)

        self.click(*self.locatorAdminDashboard.createProvider)
        sleep(3)

        # for viewing elements
        self.move_cursor_to_element(*self.locator.ehrIntegration)
        sleep(1)

        # element displayed verification
        elements = [self.locator.augmedixNoteWriter, self.locator.automaticContinuity, self.locator.audioRecording, self.locator.cardPersistence,
                    self.locator.convertToText, self.locator.ehrScreenshot, self.locator.imageCapture, self.locator.manualContinuity,
                    self.locator.uploadImage, self.locator.speechToTextTranscriber, self.locator.enableStorageForIM, self.locator.automoaticallyRequestDailyFeedback,
                    self.locator.careAssist, self.locator.enableKinesis, self.locator.persistNotesForever, self.locator.enableDocAppLevelQualityOfStream]

        messages = ['augmedix NoteWriter component found', 'automatic Continuity  feature component found', 'audio Recording  feature component found', 'card Persistence feature component found',
                    'convert To Text  feature component found', 'ehr Screenshot  feature component found', 'image Capture  feature component found', 'manual Continuity feature component found',
                    'upload Image  feature component found', 'speech To Text Transcriber  feature component found', 'enable Storage For IM  feature component found', 'autmoatically Request Daily Feedback feature component found',
                    'care Assist  feature component found', 'enable Kinesis  feature component found', 'persist Notes Forever  feature component found', 'enable Doc App Level Quality Of Stream feature component found']

        for i in range(0, len(elements)):
            print(i)
            self.assert_element_is_displayed(messages[i], *elements[i])

        # Default off assert
        val = self.get_attribute_value(self.data.classAttribute, *self.locator.manualContinuity)
        assert self.data.labelTextDisabled in val
        print('Manual Continuity is disabled found')
        val = self.get_attribute_value(self.data.classAttribute, *self.locator.enableKinesis)
        assert self.data.labelTextDisabled in val
        print('Enable Kinesis is disabled found')
        val = self.get_attribute_value(self.data.classAttribute, *self.locator.persistNotesForever)
        assert self.data.labelTextDisabled in val
        print('Persist Notes Forever is disabled found')
        print('Default settings are off found')

        # all off by default and user can select-deselect
        elements = [self.locator.augmedixNoteWriter, self.locator.automaticContinuity, self.locator.audioRecording, self.locator.cardPersistence,
                    self.locator.convertToText, self.locator.ehrScreenshot, self.locator.imageCapture, self.locator.manualContinuity,
                    self.locator.uploadImage, self.locator.speechToTextTranscriber, self.locator.enableStorageForIM, self.locator.careAssist,
                    self.locator.automoaticallyRequestDailyFeedback, self.locator.enableDocAppLevelQualityOfStream]

        elements_input = [self.locator.augmedixNoteWriterInput, self.locator.automaticContinuityInput, self.locator.audioRecordingInput, self.locator.cardPersistenceInput,
                          self.locator.convertToTextInput, self.locator.ehrScreenshotInput, self.locator.imageCaptureInput, self.locator.manualContinuityInput,
                          self.locator.uploadImageInput, self.locator.speechToTextTranscriberInput, self.locator.enableStorageForIMInput, self.locator.careAssistInput,
                          self.locator.autmoaticallyRequestDailyFeedbackInput, self.locator.enableDocAppLevelQualityOfStreamInput]

        for i in range(0, len(elements)):
            self.assert_blank_checkbox_element(self.data.classAttribute, self.data.emptyFeatureValue, *elements_input[i])
            sleep(1)
            self.click(*elements[i])
            sleep(1)
            self.assert_checkbox_element(self.data.classAttribute, self.data.featureValue, *elements_input[i])

        # for running next part of test
        self.click(*self.locator.automaticContinuity)

        # Manual continuity disable_enable assert
        self.move_cursor_to_element(*self.locator.manualContinuity)
        sleep(2)
        val = self.get_attribute_value(self.data.classAttribute, *self.locator.manualContinuity)
        assert self.data.labelTextDisabled in val
        print('manual Continuity is disabled  found')
        self.click(*self.locator.automaticContinuity)
        sleep(3)
        val = self.get_attribute_value(self.data.classAttribute, *self.locator.manualContinuity)
        assert self.data.labelTextDisabled not in val
        print('manual Continuity is enabled found')

    @allure.step("verify image upload on provider creation form")
    def test_C9273_verify_image_upload_on_provider_creation_form(self):
        self.login()

        # For staging portal
        if self.data.stagingPortal:
            self.click(*self.locatorAdminDashboard.provider)
        sleep(2)

        self.click(*self.locatorAdminDashboard.createProvider)
        sleep(3)
        self.send_data(self.data.providerImagePath, *self.locator.uploadProfilePicture)
        sleep(3)
        print('User Image updated')

        res = self.element_is_displayed(*self.locator.deleteProfilePicture)
        assert res is True
        print('Delete Image button found')
        sleep(2)
        self.click(*self.locator.deleteProfilePicture)
        sleep(2)
        self.send_data(self.data.providerFourMBImagePath, *self.locator.uploadProfilePicture)
        sleep(1)
        val = self.get_text(*self.locator.largerImageAlert)
        print(val)
        assert val == self.data.largerImageAlert
        sleep(2)

    @allure.step("verify security settings on provider creation form")
    def test_C9274_verify_security_settings_on_provider_creation_form(self):
        self.login()

        # For staging portal
        if self.data.stagingPortal:
            self.click(*self.locatorAdminDashboard.provider)
        sleep(2)

        self.click(*self.locatorAdminDashboard.createProvider)
        sleep(3)
        list1 = self.get_list_of_dropdown_element(*self.locator.securitySettings)
        val = self.get_num__of_dropdown_element(*self.locator.securitySettings)
        list2 = []
        for i in range(0, val):
            self.select_by_index(i, *self.locator.securitySettings)
            val = self.get_active_option_of_dropdown_element(*self.locator.securitySettings)
            list2.append(val)
            sleep(1)
        print('Security setting options: ', list1, sep='\n')
        print('Selected security setting options', list2, sep='\n')
        assert list1 == list2

    @allure.step("verify phone number on provider creation form")
    def test_C9275_verify_phone_number_on_provider_creation_form(self):
        self.login()

        # For staging portal
        if self.data.stagingPortal:
            self.click(*self.locatorAdminDashboard.provider)
        sleep(2)

        self.click(*self.locatorAdminDashboard.createProvider)
        sleep(3)
        self.move_cursor_to_element(*self.locator.phone)
        sleep(2)
        self.send_data(self.data.providerInvalidPhoneNumber, *self.locator.phone)
        val = self.get_attribute_value(self.data.valueAttribute, *self.locator.phone)
        assert val == self.data.providerEmptyPhone
        print('Cant input invalid characters in phone field')
        sleep(2)
        self.send_data(self.data.providerPhoneNumber, *self.locator.phone)
        sleep(1)
        val = self.get_attribute_value(self.data.valueAttribute, *self.locator.phone)
        assert val == self.data.providerPhoneNumber
        print('Can input valid characters in phone field')

    @allure.step("verify email address on provider creation form")
    def test_C9276_verify_email_address_on_provider_creation_form(self):
        self.login()

        # For staging portal
        if self.data.stagingPortal:
            self.click(*self.locatorAdminDashboard.provider)
        sleep(2)

        self.click(*self.locatorAdminDashboard.createProvider)
        sleep(3)
        self.send_data(self.data.providerInvalidEmail, *self.locator.firstName)
        sleep(1)
        self.send_data(self.data.providerInvalidEmail, *self.locator.lastName)
        sleep(1)
        self.send_data(self.data.providerInvalidEmail, *self.locator.email)
        sleep(1)
        self.click(*self.locator.createProvidersubmit)
        sleep(1)
        val = self.get_attribute_value(self.data.classAttribute, *self.locator.email)
        assert self.data.classError in val
        print('invalid email format alert found')

    @allure.step("verify password limitation and onboarding option on provider creation form")
    def test_C9277_verify_password_limitation_and_onboarding_option_on_provider_creation_form(self):
        self.login()

        # For staging portal
        if self.data.stagingPortal:
            self.click(*self.locatorAdminDashboard.provider)
        sleep(2)

        self.click(*self.locatorAdminDashboard.createProvider)
        sleep(3)

        # verify password option
        list1 = self.get_list_of_dropdown_element(*self.locator.passwordHistoryLimit)
        list_int = list1
        list_int = list(map(int, list_int))
        res = all(2 <= ele <= 10 for ele in list_int)
        assert res is True
        val = self.get_num__of_dropdown_element(*self.locator.passwordHistoryLimit)
        list2 = []
        for i in range(0, val):
            self.select_by_index(i, *self.locator.passwordHistoryLimit)
            val = self.get_active_option_of_dropdown_element(*self.locator.passwordHistoryLimit)
            list2.append(val)
            sleep(1)
        print('password history limit options: ', list1, sep='\n')
        print('Selected password history limit options', list2, sep='\n')
        assert list1 == list2

        # verify onoarding option
        list1 = self.get_list_of_dropdown_element(*self.locator.onboarding)
        val = self.get_num__of_dropdown_element(*self.locator.onboarding)
        list2 = []
        for i in range(0, val):
            self.select_by_index(i, *self.locator.onboarding)
            val = self.get_active_option_of_dropdown_element(*self.locator.onboarding)
            list2.append(val)
            sleep(1)
        print('Onboarding options: ', list1, sep='\n')
        print('Selected onboarding options', list2, sep='\n')
        assert list1 == list2
