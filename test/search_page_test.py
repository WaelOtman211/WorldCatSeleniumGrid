import concurrent.futures
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.search_page import SearchPage  # Renamed to reflect new focus


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.close_browser()

    def test_search_library_due_to_location(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url(driver)
        search_page = SearchPage(driver)
        search_page.search_for_library_due_to_location("Yokneam Ilit")
        expected_result="Libraries"
        self.assertEqual(expected_result, search_page.is_lib_page_loaded())

    def test_search_item_by_Brett_Cooke(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url(driver)
        search_page = SearchPage(driver)
        search_page.search_for_item_by_Brett_Cooke("war and peace")
        Author_expected = "Brett Cooke"
        self.assertTrue(search_page.is_the_book_title_correct("war and peace"), "the book dose not displayed on the books list")
        self.assertEqual(Author_expected,search_page.is_the_author_name_correct(),"Not the same author")

    def test_run_grid_parallel(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_search_library_due_to_location, self.browser.browser_types)

        else:
            self.test_search_library_due_to_location(self.browser.default_browser)





