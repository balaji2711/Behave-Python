import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class SeleniumActions:
    element = None

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locatorType, locatorValue):
        element = None
        if locatorType == 'ID':
            element = self.driver.find_element_by_id(locatorValue)
        elif locatorType == 'NAME':
            element = self.driver.find_element_by_name(locatorValue)
        elif locatorType == 'XPATH':
            element = self.driver.find_element_by_xpath(locatorValue)
        elif locatorType == 'CSS_SELECTOR':
            element = self.driver.find_element_by_css_selector(locatorValue)
        elif locatorType == 'CLASS_NAME':
            element = self.driver.find_element_by_class_name(locatorValue)
        elif locatorType == 'TAG_NAME':
            element = self.driver.find_element_by_tag_name(locatorValue)
        return element

    def click(self, locatorType, locatorValue):
        try:
            element = SeleniumActions.find_element(self, locatorType, locatorValue)
            element.click()
        except NoSuchElementException:
            print('Unable to click an element')

    def type(self, locatorType, locatorValue, value):
        try:
            element = SeleniumActions.find_element(self, locatorType, locatorValue)    
            WebDriverWait(self.driver, 10).until(lambda driver: element)
            element.clear()
            element.send_keys(value)
        except NoSuchElementException:
            print('Unable to enter a text') 

    def get(self, locatorType, locatorValue):
        try:
            element = SeleniumActions.find_element(self, locatorType, locatorValue)
            WebDriverWait(self.driver, 5).until(lambda driver: element)
            return element.text
        except Exception:
            print('Unable to fetch a text')
            return ''

    def get_attribute_value(self, locatorType, locatorValue):
        try:            
            element = SeleniumActions.find_element(self, locatorType, locatorValue)
            WebDriverWait(self.driver, 5).until(lambda driver: element)
            return element.get_attribute('value')
        except NoSuchElementException:
            print('Unable to fetch a text based on attribute value') 

    def get_attribute(self, locatorType, locatorValue, attribute_name):
        try:            
            element = SeleniumActions.find_element(self, locatorType, locatorValue)
            WebDriverWait(self.driver, 5).until(lambda driver: element)
            return element.get_attribute(attribute_name)
        except NoSuchElementException:
            print('Unable to fetch a text based on attribute name')  

    def get_selected_text_from_drop_down(self, locatorType, locatorValue):
        try:
            element = SeleniumActions.find_element(self, locatorType, locatorValue)
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(element))
            select = Select(element)
            return select.first_selected_option.text.strip()
        except NoSuchElementException:
            print('Unable to fetch a text from selected drop-down')

    def hover(self, locatorType, locatorValue):
        try:
            element = SeleniumActions.find_element(self, locatorType, locatorValue)
            WebDriverWait(self.driver, 5).until(lambda driver: element)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
        except NoSuchElementException:
            print("Can't hover an element")

    def switch_to_top_window(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
        self.driver.maximize_window()
        time.sleep(5)

    def switch_to_frame(self, frame_reference):
        self.driver.switch_to_frame(frame_reference)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def select(self, locatorType, locatorValue, element, visible_text):
        element = SeleniumActions.find_element(self, locatorType, locatorValue)
        WebDriverWait(self.driver, 5).until(lambda driver: element)
        select = Select(element)
        try:
            select.select_by_visible_text(visible_text)
        except NoSuchElementException:
            time.sleep(5)
        finally:
            select.select_by_visible_text(visible_text)

    def validate_page_title(self, expected_title):
        actual_title = str(self.driver.title)
        assert actual_title == expected_title, "Incorrect page title - "+actual_title

    def is_selected(self, locatorType, locatorValue):
        try:
            element = SeleniumActions.find_element(self, locatorType, locatorValue)
            WebDriverWait(self.driver, 5).until(lambda driver: element)
            flag = element.is_selected()
        except NoSuchElementException:
            print('Element not found')
            flag = False
        return flag

    def is_displayed(self, locatorType, locatorValue):
        try:
            element = SeleniumActions.find_element(self, locatorType, locatorValue)
            flag = element.is_displayed()
        except NoSuchElementException:
            print('Element not found')
            flag = False
        return flag

    def scroll_to_element(self, locatorType, locatorValue):
        try:
            element = SeleniumActions.find_element(self, locatorType, locatorValue)
            location = element.location
            cord_y = location['y']-200
            cord_x = location['x']
            self.driver.execute_script("window.scrollTo("+str(cord_x)+", "+str(cord_y)+")")
        except NoSuchElementException:
            print('Element not found')
    
    def drag_and_drop(self, source_locatorType, source_locatorValue,target_locatorType, target_locatorValue):
        try:
            action_chains = ActionChains(self.driver)
            source = SeleniumActions.find_element(self, source_locatorType, source_locatorValue)
            target = SeleniumActions.find_element(self, target_locatorType, target_locatorValue)
            action_chains.drag_and_drop_by_offset(source, 100, 100).perform()
            time.sleep(2)
            action_chains.drag_and_drop(source, target).perform()
            time.sleep(2)
        except NoSuchElementException:
            print("Can't drag and drop an element")