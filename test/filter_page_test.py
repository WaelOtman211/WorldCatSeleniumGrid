import concurrent.futures
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.filter_page import FilterPage  # Renamed to reflect new focus


class FilterTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.close_browser()

    def test_fill_filter_search_and_check_book_year(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url(driver)
        filter = FilterPage(driver)
        expected_result="1802"
        self.assertEqual(expected_result,filter.is_the_year_of_specific_book_is_correct_due_to_the_filter("war","peace","1800","2000"),"the year dose mach the filter filling")

    def test_fill_filter_search_and_reset(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url(driver)
        filter = FilterPage(driver)
        self.assertTrue(filter.is_the_filter_reset("war","peace","1800","2000"),"filter dose not reset")

    def test_run_grid_parallel(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_fill_filter_search_and_check_book_year, self.browser.browser_types)

        else:
            self.test_fill_filter_search_and_check_book_year(self.browser.default_browser)





