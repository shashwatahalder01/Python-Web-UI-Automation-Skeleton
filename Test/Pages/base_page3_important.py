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

    #     if element is visible
    #  if element is not visible
    #  if visible then do some action

    # Mouse hover by pyautogui

    # download file using chrome option and js executor
    # elem = driver.switch_to.active_element
    # add slider function
    # add scroll
    # add scroll to element
    # add send image function
    # add has attribute or not

    # clear multiple input fields
    # # add try catch approach
    # def try_except(self, *locator):
    #     try:
    #         element = self.driver.find_element(*locator)
    #         element.click()
    #         print("clicked on 1st imagedelete")
    #     except:
    #         element = self.driver.find_element(*locator)
    #         self.driver.execute_script("arguments[0].click();", element)

    # add js executor for all function alternatives
    # 'document.getElementById("context-menu").style.display="block"'

    # perform Js command
    def execute_javascript(self, command):
        self.driver.execute_script(command)

    # Js element click
    def js_click(self, *locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    # Js scroll to element
    def js_scroll_to_element(self, *locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Js scroll by pixel value
    def js_scroll_by_pixel(self, x_axis_value, y_axis_value, *locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script(f"javascript:window.scrollBy({x_axis_value},{y_axis_value});", element)

    # Js accept alert
    def js_accept_alert(self):
        self.driver.execute_script("window.confirm = function(){return true;}")

    def js_remove_attribute(self):
        js = 'document.getElementById("upload-button").removeAttribute("onclick");'
        self.driver.execute_script(js)

    # common scenarios

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

    # Find single element  ✓✓
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    # Find multiple elements  ✓✓
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    # Mouse hover on an element  ✓✓
    def hover(self, *locator):
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # button / link / image_____________________________________

    # Element properties

    # Element is displayed or not  ✓✓
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

    # Get attribute ✓✓
    def get_attribute_value(self, attribute, *locator):
        element = self.driver.find_element(*locator)
        val = element.get_attribute(attribute)
        # print(val)
        return val

    # Get CSS property ✓✓
    def get_css_property(self, attribute, *locator):
        element = self.driver.find_element(*locator)
        val = element.value_of_css_property(attribute)
        # print(val)
        return val

    # Get text ✓✓
    def get_text(self, *locator):
        element = self.driver.find_element(*locator)
        val = element.text
        # print(val)
        return val

    # Text field ___________________________________

    # Send data ✓✓
    def send_data(self, data, *locator):
        self.driver.find_element(*locator).send_keys(data)

    # Clear input field ✓✓
    def clear_field(self, *locator):
        self.driver.find_element(*locator).clear()

        # or force clear
    def clear_input_field(self, *locator):
        element = self.driver.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    # Clear input field and then send data to input field ✓✓
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

    # Select dropdown elements ✓✓
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

    # screenshot________________________________________

    # save screenshot   # formate must be png
    def take_screenshot(self, imagepath):
        self.driver.save_screenshot(imagepath+'/sample_screenshot_1.png')

    def get_screenshot(self, imagepath):
        self.driver.get_screenshot_as_file(imagepath+'/sample_screenshot_2.png')

    # returns binary data
    def take_binary_screenshot(self):
        self.driver.get_screenshot_as_png('sample_screenshot_1.png')
        # import StringIO
        # from PIL import Image
        # screenshot = driver.get_screenshot_as_png()
        #
        # size = (0, 0, 680, 400)
        # image = Image.open(StringIO.StringIO(screen))
        # region = image.crop(size)
        # region.save('sample_screenshot_3.jpg', 'JPEG', optimize=True, quality=95)

    # take element screenshot
    def take_element_screentshot(self, imagepath, *locator):
        # from PIL import Image
        element = self.driver.find_element(*locator)
        # location = element.location
        # size = element.size
        # self.driver.save_screenshot("/data/image.png")
        # x = location['x']
        # y = location['y']
        # width = location['x'] + size['width']
        # height = location['y'] + size['height']
        #
        # im = Image.open('/data/WorkArea/image.png')
        # im = im.crop((int(x), int(y), int(width), int(height)))
        # im.save('/data/image.png')

    # Mouse actions_____________________________________

    # Click ✓✓
    def click(self, *locator):
        self.driver.find_element(*locator).click()

    # Double click ✓✓
    def double_click(self, *locator):
        self.driver.find_element(*locator).double_click()

    # Click and hold
    def click_and_hold(self, *locator):
        self.driver.find_element(*locator).click_and_hold()

    # contest click/ right click
    def context_click(self, *locator):
        self.driver.find_element(*locator).context_click()

    # or

    def right_click(self, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver).move_to_element(element)
        actions.context_click().perform()

    # Move cursor to element then click / click drop down item
    def move_cursor_and_click(self, menu, submenu1):
        menu = self.driver.find_element(menu)
        submenu = self.driver.find_element(submenu1)
        actions = ActionChains(self.driver)  # initialize ActionChain object
        actions.move_to_element(menu).click(submenu).perform()

    #  move cursor by offset
    def move_cursor_by_offset(self, xoffset, yoffset):
        actions = ActionChains(self.driver)
        actions.move_by_offset(xoffset, yoffset)

    # move cursor to element  # same  as hover function
    def move_cursor_to_element(self, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    # move cursor to element with offset
    def move_cursor_to_element_offset(self, xoffset, yoffset, *locator):
        element = element = self.driver.find_element(*locator)
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
        actions.key_down(f'Keys.{modifier_key}')    # hold key
        actions.send_keys(key)
        actions.key_down(f'Keys.{modifier_key}')    # release key
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

    # Moving between windows and frames____________________

    # Switch to window
    def switch_to_window(self, window):
        return self.driver.switch_to_window(window)

    # count iframe
    def iframe_count(self):
        iframe_list = self.driver.find_elements_by_tag_name("iframe")
        length = len(iframe_list)
        print(length)
        return length

    # Switch to frame or iframe  #  argument frame can be index, id ,name of frame or web element of frame (for web-element method might be different)
    def switch_to_frame(self, frame):
        return self.driver.switch_to_frame(frame)

    # Switch to sub_frame or iframe
    def switch_to_sub_frame(self, parent_frame, child_frame):
        return self.driver.switch_to_frame(parent_frame + '.' + child_frame)

    # Switch back to parent frame  # or can use switch to frame method
    def switch_to_parent_frame(self):
        return self.driver.switch_to.parent_frame()

    # Switch back to main frame
    def switch_to_main_frame(self):
        return self.driver.switch_to_default_content()

    # Popup dialogs______________________________________

    # Switch to alert
    def switch_to_alert(self):
        return self.driver.switch_to.alert

    # Accept alert
    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    # Dismiss alert
    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    # get alert text
    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        val = alert.text
        return val

    # send text to alert
    def send_text_to_alert(self, text):
        alert = self.driver.switch_to.alert
        val = alert.send_keys(text)

    # Read browser details______________________________

    # Get title
    def get_title(self):
        return self.driver.title

    # Get window handles
    def get_window_handles(self):
        return self.driver.window_handles

    # Get current window handles
    def get_current_window_handles(self):
        return self.driver.current_window_handles
    #  which one are correct???
    # def get_window_handle(self, num):
    #     return self.driver.window_handles[num]
    #
    # def switch_window(self, win):
    #     return self.driver.switch_to_window(win)

    # Get current url
    def get_current_url(self):
        return self.driver.current_url

    # Get page source
    def get_page_source(self):
        return self.driver.page_source

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

    #  Cookies ___________________________________________

    # Set cookie for the entire domain
    def set_cookies(self, url, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.get(url)
        self.driver.add_cookie(cookie)

    # Get all the available cookies for the current URL
    def get_cookies(self, url):
        self.driver.get(url)
        self.driver.get_cookies()

    # Get User-Agent value

    def get_user_agent_value(self):
        agent = self.driver.execute_script("return navigator.userAgent")
        print(agent)

    # User - Agent setup in Chrome:
    # With Chrome, you have to use Options instance to set the user - agent value.
    #
    # from selenium import webdriver
    # from selenium.webdriver.chrome.options import Options
    #
    # opts = Options()
    # opts.add_argument("user-agent=[user-agent string]")
    # # Below is tested line
    # # opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    #
    # driver = webdriver.Chrome(chrome_options=opts)
    # Alternative   way    to  pass driver path along with other details:
    #
    # driver = webdriver.Firefox(profile, executable_path="path to geckodriver")
    # driver = webdriver.Chrome(chrome_options=opts, executable_path="path to chromedriver")

    # Waits__________________________________________________

    # Explicit wait

    #  title is

    # title contains

    #  wait till presence of element is located
    def wait_till_presence_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.presence_of_element_located(*locator))
        return element

    #  wait till visibility_of_element_located
    def wait_till_visibility_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.visibility_of_element_located(*locator))
        return element

    # visibility of

    #  wait till presence_of_all_elements_located
    def wait_till_presence_of_all_elements_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.presence_of_all_elements_located(*locator))
        return element

    #  wait till text_to_be_present_in_element
    def wait_till_text_to_be_present_in_element(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.text_to_be_present_in_element(*locator))
        return element

    #  wait till text_to_be_present_in_element_value
    def wait_till_text_to_be_present_in_element_value(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.text_to_be_present_in_element_value(*locator))
        return element

    #  wait till frame_to_be_available_and_switch_to_it
    def wait_till_frame_to_be_available_and_switch_to_it(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.frame_to_be_available_and_switch_to_it(*locator))
        return element

    #  wait till invisibility_of_element_located
    def wait_till_invisibility_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.invisibility_of_element_located(*locator))
        return element

    #  wait till element_to_be_clickable
    def wait_till_element_to_be_clickable(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.element_to_be_clickable(*locator))
        return element

    # staleness of

    #  wait till element_to_be_selected
    def wait_till_element_to_be_selected(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.element_to_be_selected(*locator))
        return element

    #  wait till element_located_to_be_selected
    def wait_till_element_located_to_be_selected(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.element_located_to_be_selected(*locator))
        return element

    #  wait till element_selection_state_to_be
    def wait_till_element_selection_state_to_be(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.element_selection_state_to_be(*locator))
        return element

    #  wait till element_located_selection_state_to_be
    def wait_till_element_located_selection_state_to_be(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.element_located_selection_state_to_be(*locator))
        return element

    #  wait till alert_is_present
    def wait_till_alert_is_present(self, seconds):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.alert_is_present)
        return element

    # custom wait

    # implicit wait
    def implicit_waits(self, seconds):
        return self.driver.implicitly_wait(seconds)

    # def assert_true(self, result):
    #     assert result is True
    #
    # def assert_false(self, result):
    #     assert result is False
    #
    # def assert_in(self, result, data):
    #     assert result in data
    #
    # def assert_not_in(self, result, data):
    #     assert result not in data

    # self.assertEqual()
    # self.assertEquals()
    # self.assertTrue()
    # self.assertFalse()
    # self.assert_()
    # self.assertAlmostEqual()
    # self.assertAlmostEquals()
    # self.assertNotAlmostEqual()
    # self.assertNotAlmostEquals()
    # self.assertCountEqual()
    # self.assertDictEqual()
    # self.assertGreater()
    # self.assertGreaterEqual()
    # self.assertIn()
    # self.assertIs()
    # self.assertIsNot()
    # self.assertIsNone()
    # self.assertIsNotNone()
    # self.assertIsInstance()
    # self.assertNotIsInstance()
    # self.assertLess()
    # self.assertLessEqual()
    # self.assertListEqual()
    # self.assertLogs()
    # self.assertMultiLineEqual()

    # def wait_element(self, *locator):
    #     try:
    #         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
    #     except TimeoutException:
    #         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
    #         self.driver.quit()

    # def wait_element1(self, *locator):
    #     try:
    #         ignored_exceptions = (NoSuchElementException, StaleElementReferenceException )
    #         WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located(locator))
    #     except TimeoutException:
    #         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
    #         self.driver.quit()

    # dynamic locator
    #     def symptom(name):
    #         typename = f"//span[contains(text(), '{name}')]"
    #         return typename

    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"

    # use try catch instead of if else
    # clear input field first

    # Keys.RETURN  Keys.ARROW_DOWN2

    # setup selenium remote driver
