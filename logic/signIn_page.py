import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from infra.base_page import Base_Page


class SignInPage(Base_Page):
    COOKIES_BUTTON = '//button[@id="onetrust-accept-btn-handler"]'
    SIGN_IN_BUTTON = '//a[@data-testid="header-sign-in-link"]'
    EMAIL_INPUT_IN_WORLD_CAT_PAGE = '//input[@name="emailField"]'
    SUBMIT_BUTTON = '//button[@type="submit"]'
    EMAIL_INPUT_IN_SIGN_IN_PAGE = '//input[@placeholder="Email"]'
    PASSWORD_INPUT_IN_SIGN_IN_PAGE = '//input[@placeholder="Password"]'
    SUBMIT_SIGN_IN_BUTTON = '//button[@id="submitSignin"]'
    WELCOME_LABEL = '(//div[@role="combobox"])[1]'
    MY_PROFILE_BUTTON = '//li[@data-value="my-profile"]'
    USER_NAME = '(//p[@class="MuiTypography-root MuiTypography-body1 tss-1elsz4e-flexColumn mui-1qm8jy7"])[1]'
    INCORRECT_LABEL_DISPLAYED = '//div[@class="object-error"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)

    def press_cookies_button(self):
        time.sleep(2)
        cookies_button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.COOKIES_BUTTON))
        )
        cookies_button.click()

    def fill_email_input_in_sign_in_world_cat(self, email):
        email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT_IN_WORLD_CAT_PAGE)
        email_input.send_keys(email)

    def click_sing_in_button(self):
        self.press_cookies_button()
        self.sign_in_button.click()
        time.sleep(2)

    def click_submit_button(self):
        submit_button = self._driver.find_element(By.XPATH, self.SUBMIT_BUTTON)
        submit_button.click()
        time.sleep(10)

    def fill_email_in_sign_in_page(self, email):
        email_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT_IN_SIGN_IN_PAGE))
        )
        email_input.send_keys(email)

    def fill_password_in_sign_in_page(self, password):
        password_input = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PASSWORD_INPUT_IN_SIGN_IN_PAGE))
        )
        password_input.send_keys(password)

    def click_submit_sign_in_button(self):
        submit_sign_in_button = self._driver.find_element(By.XPATH, self.SUBMIT_SIGN_IN_BUTTON)
        submit_sign_in_button.click()
        try:
            incorrect_label = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.INCORRECT_LABEL_DISPLAYED))
            )
            if incorrect_label.is_displayed():
                return incorrect_label.text
        except TimeoutException:

            return "pass"

    def click_on_welcome_label(self):
        welcome_label = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.WELCOME_LABEL))
        )
        welcome_label.click()

    def click_on_my_profile_button(self):
        my_profile_button = WebDriverWait(self._driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.MY_PROFILE_BUTTON))
        )
        my_profile_button.click()

    def is_sign_in_success(self, email, password):
        result=self.sign_in_flow(email, password)
        if result == "pass":
            user_name = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.USER_NAME))
            )
            return user_name.text
        else:
            return result

    def sign_in_flow(self, email, password):
        self.click_sing_in_button()
        self.fill_email_input_in_sign_in_world_cat(email)
        self.click_submit_button()
        self.fill_email_in_sign_in_page(email)
        self.fill_password_in_sign_in_page(password)
        result = self.click_submit_sign_in_button()
        if result == "pass":
            self.click_on_welcome_label()
            self.click_on_my_profile_button()
            return "pass"
        else:
            return result
