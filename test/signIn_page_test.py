import concurrent.futures
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.signIn_page import SignInPage  # Renamed to reflect new focus


class SignInTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.close_browser()

    def test_try_to_signIn_with_correct_email_and_password(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url(driver)
        sign_in_page = SignInPage(driver)
        expected_result = "Wael"
        self.assertEqual(expected_result, sign_in_page.is_sign_in_success("wael.otman.97@gmail.com", "Wael@1234"),
                         "SignIn Success")

    def test_try_to_signIn_with_correct_email_and_wrong_password(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url(driver)
        sign_in_page = SignInPage(driver)
        expected_result = "The email or password is invalid. Authentication failed."
        self.assertEqual(expected_result, sign_in_page.is_sign_in_success("wael.otman.97@gmail.com", "Soso@1234"),
                         "SignIn Success")

    def test_run_grid_parallel(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_try_to_signIn_with_correct_email_and_password, self.browser.browser_types)

        else:
            self.test_try_to_signIn_with_correct_email_and_password(self.browser.default_browser)





