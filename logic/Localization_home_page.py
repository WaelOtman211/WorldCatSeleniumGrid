from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from infra.base_page import Base_Page
import time


class LocalizationPage(Base_Page):
    COOKIES_BUTTON = '//button[@id="onetrust-accept-btn-handler"]'
    SEARCH_INPUT = '//input[@placeholder=" Type a city name or postal code"]'
    COMBOBOX_BUTTON = '//div[@aria-haspopup="listbox"]'
    LIST_COMBOBOX = '(//div[@aria-haspopup="listbox"])[2]'
    LIBRARY_BUTTON = '//li[@data-value="lib"]'
    LOCATION_BUTTON = '//li[@data-value="location"]'
    LIBRARY_HEADING = (By.XPATH, '//h1[@class="MuiTypography-root MuiTypography-h1 tss-8ep8vk-root mui-16lxm23"]')
    LOCALIZATION_BUTTON = '//span[@class="MuiBox-root mui-0"]'
    INPUT_LOCALIZATION = '//input[@placeholder=" Type a city name or postal code"]'
    UPDATE_LOCATION_BUTTON = '//button[@data-testid="location-dialog-update-button"]'
    ENSURE_LOCATION = '//input[@value="United States"]'
    NOT_FOUND_TITLE = '(//h2)[1]'
    LANGUAGE_SELECTOR = '//select[@id="language-selector"]'
    FRENCH_OPTION = '//option[@value="fr"]'
    HOME_PAGE_BUTTON = '//a[@data-testid="header-home-link"]'

    def __init__(self, driver):
        super().__init__(driver)

    def press_cookies_button(self):
        time.sleep(2)
        cookies_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COOKIES_BUTTON))
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

    def click_update_location_button(self):
        update_location = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.UPDATE_LOCATION_BUTTON))
        )
        update_location.click()

    def click_localization_button(self):

        local_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOCALIZATION_BUTTON))
        )
        local_button.click()

    def ensure_the_location_update(self):
        ensure_location = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ENSURE_LOCATION))
        )
        ensure_location.send_keys(Keys.RETURN)

    def insert_location_to_the_localization_input(self, location):
        local_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.INPUT_LOCALIZATION))
        )
        local_input.send_keys(location)
        local_input.send_keys(Keys.RETURN)
        local_input.click()
        time.sleep(2)
        self.ensure_the_location_update()

    def dose_found_any_librarys(self):
        time.sleep(3)
        try:
            not_found_title = self._driver.find_element(By.XPATH,self.NOT_FOUND_TITLE)
            if not_found_title.is_displayed():
                return not_found_title.text
        except TimeoutException:
            return False

    def until_the_cookies_window_goes(self):
        WebDriverWait(self._driver, 10).until_not(
            EC.visibility_of_element_located((By.XPATH, self.COOKIES_BUTTON))
        )

    def choose_french_language(self):
        french_option=self._driver.find_element(By.XPATH,self.FRENCH_OPTION)
        french_option.click()

    def scroll_into_specific_element(self,element):
        self._driver.execute_script("arguments[0].scrollIntoView(true);",
                                    self._driver.find_element(By.XPATH,element ))

    def click_language_selector(self):
        language_selector = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LANGUAGE_SELECTOR))
        )
        language_selector.click()

    def scroll_to_the_top_of_the_page(self):
        self._driver.execute_script("window.scrollTo(0, 0);")

    def check_home_page_button_language(self):
        home_page_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, self.HOME_PAGE_BUTTON))
        )
        current_language = home_page_button.text.strip()
        return current_language

    def change_language_flow(self):
        self.press_cookies_button()
        self.until_the_cookies_window_goes()
        self.scroll_into_specific_element(self.LANGUAGE_SELECTOR)
        self.click_language_selector()
        self.choose_french_language()
        self.scroll_to_the_top_of_the_page()

    def is_the_language_changed(self):
        self.change_language_flow()
        current_language=self.check_home_page_button_language()
        if "Accueil" in current_language:
            return True
        else:
            return False



    def search_for_library_due_to_location(self, localizationUpdate,location):
        self.press_cookies_button()
        self.click_localization_button()
        self.insert_location_to_the_localization_input(localizationUpdate)
        self.click_update_location_button()
        self.click_combobox_button()
        self.click_library_button()
        self.select_location_from_list()
        self.click_location_button()
        self.enter_location_and_submit(location)
        self.dose_found_any_librarys()




