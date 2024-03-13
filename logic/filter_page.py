import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from infra.base_page import Base_Page


class FilterPage(Base_Page):
    COOKIES_BUTTON = '//button[@id="onetrust-accept-btn-handler"]'
    FILTER_BUTTON = '//button[@aria-label="Advanced Search"]'
    KEYWORD_INPUT = '(//input[@placeholder="Enter your search term"])[1]'
    TITLE_INPUT = '(//input[@placeholder="Enter your search term"])[2]'
    YEAR_FROM_INPUT = '//input[@aria-label="Show items published after year"]'
    YEAR_TO_INPUT = '//input[@aria-label="Show items published before year"]'
    SEARCH_BUTTON = '//button[@data-testid="advanced-search-search"]'
    SORTED_BY_BUTTON = '//div[@aria-labelledby="sortBy"]'
    LAST_RECENT_BUTTON = '//li[@data-value="publicationDateAsc"]'
    YEAR_DATE_OF_BOOK = '//span[@id="date-27243240"]'
    RESET_BUTTON = '//button[@data-testid="advanced-search-reset"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.filter_button = self._driver.find_element(By.XPATH, self.FILTER_BUTTON)

    def press_cookies_button(self):

        cookies_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.COOKIES_BUTTON))
        )
        cookies_button.click()

    def click_filter_button(self):
        self.filter_button.click()

    def fill_the_keyword_input(self, text):
        keyword_input = self._driver.find_element(By.XPATH, self.KEYWORD_INPUT)
        keyword_input.send_keys(text)

    def fill_the_title_input(self, text):
        title_input = self._driver.find_element(By.XPATH, self.TITLE_INPUT)
        title_input.send_keys(text)

    def fill_year_from_input(self, year_from):
        year_from_input = self._driver.find_element(By.XPATH, self.YEAR_FROM_INPUT)
        year_from_input.send_keys(year_from)

    def fill_year_to_input(self, year_to):
        year_to_input = self._driver.find_element(By.XPATH, self.YEAR_TO_INPUT)
        year_to_input.send_keys(year_to)

    def click_search_filter(self):
        search_filter = self._driver.find_element(By.XPATH, self.SEARCH_BUTTON)
        search_filter.click()

    def click_sorted_by_button(self):
        sorted_by_button = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.SORTED_BY_BUTTON))
        )
        sorted_by_button.click()

    def click_last_recent_button(self):
        last_recent_button = self._driver.find_element(By.XPATH, self.LAST_RECENT_BUTTON)
        last_recent_button.click()

    def filter_flow(self,keyword,title,year_from,year_to):
        self.press_cookies_button()
        self.click_filter_button()
        self.fill_the_keyword_input(keyword)
        self.fill_the_title_input(title)
        self.fill_year_from_input(year_from)
        self.fill_year_to_input(year_to)

    def continue_after_the_search_flow_to_sorted_by(self):
        self.click_search_filter()
        self.click_sorted_by_button()
        self.click_last_recent_button()

    def is_the_year_of_specific_book_is_correct_due_to_the_filter(self,keyword,title,year_from,year_to):
        self.filter_flow(keyword,title,year_from,year_to)
        self.continue_after_the_search_flow_to_sorted_by()
        book_year = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.YEAR_DATE_OF_BOOK))
        )
        return book_year.text

    def is_the_filter_reset(self,keyword,title,year_from,year_to):
        try:
            self.filter_flow(keyword,title,year_from,year_to)
            self.click_reset_button()
            return True
        except TimeoutException:
            return False

    def click_reset_button(self):
        reset_button = self._driver.find_element(By.XPATH, self.RESET_BUTTON)
        reset_button.click()