import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from infra.base_page import Base_Page


class NavigationPage(Base_Page):
    COOKIES_BUTTON = '//button[@id="onetrust-accept-btn-handler"]'
    LIBRARIES_PAGE_BUTTON = '//a[@data-testid="header-libraries-link"]'
    PAGE_TITLE = '//h1[@class="MuiTypography-root MuiTypography-h1 tss-8ep8vk-root mui-16lxm23"]'
    TOPICS_PAGE_BUTTON = '//a[@data-testid="header-topics-link"]'
    LISTS_PAGE_BUTTON = '//a[@data-testid="header-lists-link"]'
    ABOUT_PAGE_BUTTON = '//a[@data-testid="header-about-link"]'
    FOR_LIBRARIES_PAGE_BUTTON = '//a[@data-testid="header-for-librarians-link"]'
    HOME_PAGE_BUTTON = '//a[@data-testid="header-home-link"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.libraries_page_button = self._driver.find_element(By.XPATH, self.LIBRARIES_PAGE_BUTTON)
        self.topics_page_button = self._driver.find_element(By.XPATH, self.TOPICS_PAGE_BUTTON)
        self.lists_page_button = self._driver.find_element(By.XPATH, self.LISTS_PAGE_BUTTON)
        self.about_page_button = self._driver.find_element(By.XPATH, self.ABOUT_PAGE_BUTTON)
        self.for_libraries_page_button = self._driver.find_element(By.XPATH, self.FOR_LIBRARIES_PAGE_BUTTON)
        self.home_page_button = self._driver.find_element(By.XPATH, self.HOME_PAGE_BUTTON)

    def press_cookies_button(self):
        time.sleep(2)
        cookies_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.COOKIES_BUTTON))
        )
        cookies_button.click()

    def find_page_title(self):
        page_title = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.PAGE_TITLE))
        )
        print(page_title.text)
        return page_title.text

    def click_libraries_page_button(self):
        self.press_cookies_button()
        self.libraries_page_button.click()

    def click_topic_page_button(self):
        self.topics_page_button.click()

    def click_list_page_button(self):
        self.lists_page_button.click()

    def click_about_page_button(self):
        self.about_page_button.click()

    def click_for_libraries_page_button(self):
        self.for_libraries_page_button.click()

    def click_home_page(self):
        self.home_page_button.click()

    def navigation_flow(self):
        try:
            self.click_libraries_page_button()
            self.click_topic_page_button()
            self.click_list_page_button()
            self.click_about_page_button()
            self.click_for_libraries_page_button()
            return True
        except TimeoutException:

            return False
