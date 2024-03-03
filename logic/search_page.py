from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from infra.base_page import Base_Page
import time


class SearchPage(Base_Page):
    COOKIES_BUTTON = '//button[@id="onetrust-accept-btn-handler"]'
    SEARCH_INPUT = '//input[@placeholder=" Type a city name or postal code"]'
    COMBOBOX_BUTTON = '//div[@aria-haspopup="listbox"]'
    LIST_COMBOBOX = '(//div[@aria-haspopup="listbox"])[2]'
    LIBRARY_BUTTON = '//li[@data-value="lib"]'
    LOCATION_BUTTON = '//li[@data-value="location"]'
    LIBRARY_HEADING = (By.XPATH, '//h1[@class="MuiTypography-root MuiTypography-h1 tss-8ep8vk-root mui-16lxm23"]')
    ITEM_INPUT = '//input[@id="home-page-search-box"]'
    BOOK_TITLE='//a[@data-testid="title-880620165"]'
    AUTHOR_NAME='//a[@data-testid="author-880620165-0"]'

    def __init__(self, driver):
        super().__init__(driver)


    def press_cookies_button(self):
        time.sleep(2)
        cookies_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.COOKIES_BUTTON))
        )
        cookies_button.click()

    def click_library_button(self):
        library_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LIBRARY_BUTTON))
        )
        library_button.click()

    def is_lib_page_loaded(self):
        try:
            h1_element = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located(self.LIBRARY_HEADING)
            )

            return h1_element.text
        except TimeoutException:
            return False

    def select_location_from_list(self):
        list_combobox = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LIST_COMBOBOX))
        )
        list_combobox.click()

    def click_location_button(self):
        location_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOCATION_BUTTON))
        )
        location_button.click()

    def enter_location_and_submit(self, location):
        search_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_INPUT))
        )
        search_input.send_keys(location)
        search_input.send_keys(Keys.RETURN)

    def click_combobox_button(self):
        time.sleep(5)
        comboBox_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.COMBOBOX_BUTTON))
        )
        comboBox_button.click()

    def search_for_library_due_to_location(self, location):
        self.press_cookies_button()
        self.click_combobox_button()
        self.click_library_button()
        self.select_location_from_list()
        self.click_location_button()
        self.enter_location_and_submit(location)

    def insert_item_name_and_submit(self,book):
        item_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ITEM_INPUT))
        )
        item_input.send_keys(book)
        item_input.send_keys(Keys.RETURN)

    def is_the_book_title_correct(self,book):
        try:
            book_title = self._driver.find_element(By.XPATH, self.BOOK_TITLE)
            if book_title.text.lower() == book:
                return True
        except TimeoutException:
            return False

    def is_the_author_name_correct(self):
        try:
            author_name = self._driver.find_element(By.XPATH, self.AUTHOR_NAME)
            if author_name.is_displayed():
                return author_name.text
        except TimeoutException:
            return False

    def search_for_item_by_Brett_Cooke(self,book):
        self.press_cookies_button()
        self.insert_item_name_and_submit(book)
        time.sleep(5)
        self.is_the_author_name_correct()



