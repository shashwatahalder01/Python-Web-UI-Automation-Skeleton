from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from time import sleep
# from selenium.common.exceptions import TimeoutException


# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):

    def __init__(self, driver, base_url="about:blank"):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 90

    # perform Js command
    def execute_javascript(self, command):
        self.driver.execute_script(command)

    # Open link in new Tab
    def open_link_new_tab(self, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

    # Open link in new window
    def open_link_new_window(self, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.SHIFT).click(element).key_down(Keys.SHIFT).perform()

    # Get text of multiple elements ✓✓
    def get_text_of_multiple_element(self, *locator):
        elements = self.driver.find_elements(*locator)
        val = []
        for element in elements:
            val.append(element.text)
        return val

    # Interacting with the page_________________________

    # Locate elements _________________________________

    # Find single element
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    # Find multiple elements
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    # Mouse hover on an element
    def hover(self, *locator):
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # button / link / image_____________________________________

    # Element properties

    # Element is displayed or not
    def element_is_displayed(self, *locator):
        element = self.driver.find_element(*locator)
        res = element.is_displayed()
        return res

    # Element is enabled or not
    def element_is_enabled(self, *locator):
        element = self.driver.find_element(*locator)
        res = element.is_enabled()
        return res

    # Element is selected or not   # checkbox/Radio
    def element_is_selected(self, *locator):
        element = self.driver.find_element(*locator)
        res = element.is_selected()
        return res

    # Get attribute
    def get_attribute_value(self, attribute, *locator):
        element = self.driver.find_element(*locator)
        val = element.get_attribute(attribute)
        # print(val)
        return val

    # Get CSS property
    def get_css_property(self, attribute, *locator):
        element = self.driver.find_element(*locator)
        val = element.value_of_css_property(attribute)
        # print(val)
        return val

    # Get text
    def get_text(self, *locator):
        element = self.driver.find_element(*locator)
        val = element.text
        # print(val)
        return val

    # Text field ___________________________________

    # Send data
    def send_data(self, data, *locator):
        self.driver.find_element(*locator).send_keys(data)

    # Clear input field
    def clear_field(self, *locator):
        self.driver.find_element(*locator).clear()

        # or force clear

    def clear_input_field(self, *locator):
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    # Clear input field and then send data to input field
    def clear_input_field_and_send_keys(self, data, *locator):
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(data)

        # or

    def clear_field_and_send_keys(self, data, *locator):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(data)

    # Filling in forms_________________________________

    # Get num of dropdown element
    def get_num__of_dropdown_element(self, *locator):
        select = Select(self.driver.find_element(*locator))
        options = select.options
        return len(options)

    # Get list of dropdown element
    def get_list_of_dropdown_element(self, *locator):
        select = Select(self.driver.find_element(*locator))
        options = select.options
        option_values = []
        for option in options:
            option_values.append(option.text)
        return option_values

    # Get active option in select
    def get_active_option_of_dropdown_element(self, *locator):
        select = Select(self.driver.find_element(*locator))
        selected_option_text = select.first_selected_option.text
        return selected_option_text

    # Select dropdown elements
    def select_dropdown_element(self, name, *locator):
        select = Select(self.driver.find_element(*locator))
        options = select.options
        option_values = []
        for option in options:
            option_values.append(option.text)
        # print(option_values)
        select.select_by_index(option_values.index(name))

    # Select 'Select' element by index value
    def select_by_index(self, index, *locator):
        select = Select(self.driver.find_element(*locator))
        return select.select_by_index(index)

    # Select 'Select' element by visible text
    def select_by_visible_text(self, text, *locator):
        select = Select(self.driver.find_element(*locator))
        return select.select_by_visible_text(text)

    # Select 'Select' element by value
    def select_by_value(self, value, *locator):
        select = Select(self.driver.find_element(*locator))
        return select.select_by_value(value)

    # De-select all 'Select' element
    def deselect_all(self, *locator):
        select = Select(self.driver.find_element(*locator))
        select.deselect_all()

    # Get list of all default selected options
    def get_selected_options(self, *locator):
        select = Select(self.driver.find_element(*locator))
        all_selected_options = select.all_selected_options
        return all_selected_options

    # Get list of all options
    def get_all_options(self, *locator):
        select = Select(self.driver.find_element(*locator))
        options = select.options
        return options

    # Submit form
    def submit_form(self, *locator):
        element = self.driver.find_element(*locator)
        element.submit()

    # Click
    def click(self, *locator):
        self.driver.find_element(*locator).click()

    # Double click
    def double_click(self, *locator):
        self.driver.find_element(*locator).double_click()

    # Click and hold
    def click_and_hold(self, *locator):
        self.driver.find_element(*locator).click_and_hold()

    # contest click/ right click
    def context_click(self, *locator):
        self.driver.find_element(*locator).context_click()

    # Move cursor to element then click
    def move_cursor_and_click(self, *locator):
        menu = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)  # initialize ActionChain object
        actions.move_to_element(*locator).click(*locator).perform()

    # click drop down item
    def click_drop_down_element(self, menu, submenu1):
        menu = self.driver.find_element(menu)
        submenu = self.driver.find_element(submenu1)
        actions = ActionChains(self.driver)  # initialize ActionChain object
        actions.move_to_element(menu).click(submenu).perform()

    #  move cursor by offset
    def move_cursor_by_offset(self, xoffset, yoffset):
        actions = ActionChains(self.driver)
        actions.move_by_offset(xoffset, yoffset)

    # move cursor to element
    def move_cursor_to_element(self, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    # move cursor to element with offset
    def move_cursor_to_element_offset(self, xoffset, yoffset, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, xoffset, yoffset)
        actions.perform()

    # Drag and drop an element
    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(source_locator)
        target = self.driver.find_element(target_locator)
        drag_and_drop = ActionChains(self.driver).drag_and_drop(source, target)
        drag_and_drop.perform()

    # Drag and drop by offset
    def drag_and_drop_offset(self, source_locator, xoffset, yoffset):
        source = self.driver.find_element(source_locator)
        drag_and_drop = ActionChains(self.driver).drag_and_drop_by_offset(source, xoffset, yoffset)
        drag_and_drop.perform()

    # modifier key + key:  CONTROL+C
    def command_perform(self, modifier_key, key):
        actions = ActionChains(self.driver)
        actions.key_down(f'Keys.{modifier_key}')  # hold key
        actions.send_keys(key)
        actions.key_down(f'Keys.{modifier_key}')  # release key
        actions.perform()

    # Sends keys to current focused element
    def send_keys_actionchains(self, key):
        actions = ActionChains(self.driver)
        actions.send_keys(key)

    # Sends keys to an element
    def send_keys_to_element_actionchains(self, key, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(element, key)

    #  Navigation _______________________________________

    # Open desired url
    def open_url(self, url):
        self.driver.get(url)

    # Open sub_url of main domain
    def open_sub_url(self, url):
        #  Base url is the main domain
        url = self.base_url + url
        self.driver.get(url)

    # Refresh page
    def refresh_page(self):
        return self.driver.refresh()

    # Go to forward page
    def go_forward(self):
        return self.driver.forward()

    # Go back to previous page
    def go_back(self):
        return self.driver.back()

    # assertions
    def assert_element_is_displayed(self, message="element is found", *locator):
        res = self.element_is_displayed(*locator)
        assert res is True
        print(message)

    def assert_element_is_not_displayed(self, message="element not found", *locator):
        res = self.element_is_displayed(*locator)
        assert res is True
        print(message)

    def assert_get_attribute_value(self, choice, attribute, expected_val, *locator):
        val = self.get_attribute_value(attribute, *locator)
        # print(val)
        if choice is True:
            assert val == expected_val
        else:
            assert val != expected_val

    def assert_get_text(self, choice, expected_val, *locator):
        val = self.get_text(*locator)
        # print(val)
        if choice is True:
            assert val == expected_val
        else:
            assert val != expected_val

    # can also be used as attribute has or not
    def assert_blank_checkbox_element(self, attribute, result, *locator):
        val = self.get_attribute_value(attribute, *locator)
        assert val == result

    def assert_checkbox_element(self, attribute, result, *locator):
        val = self.get_attribute_value(attribute, *locator)
        assert val == result


