import concurrent.futures
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.logic_ui.Localization_home_page import LocalizationPage


class LocalizationTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.close_browser()

    def test_check_language_changing_to_french(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url(driver)
        localization_page = LocalizationPage(driver)

        self.assertTrue(localization_page.is_the_language_changed(),"The language is not French.")


    def test_find_library_in_incorrect_location(self, browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url(driver)
        localization_page = LocalizationPage(driver)

        localization_page.search_for_library_due_to_location("United States", "Yokneam Ilit")
        expected_result="We didn't find any results."
        self.assertEqual(expected_result,localization_page.dose_found_any_librarys())

    def test_run_grid_parallel(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_find_library_in_incorrect_location, self.browser.browser_types)

        else:
            self.test_find_library_in_incorrect_location(self.browser.default_browser)
