import concurrent.futures
import unittest
from infra.browser_wrapper import BrowserWrapper
from logic.navigation_between_pages import NavigationPage  # Renamed to reflect new focus


class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()

    def tearDown(self):
        self.browser.close_browser()

    def test_navigation_between_pages(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url(driver)
        navigation = NavigationPage(driver)
        navigation.click_libraries_page_button()



    def test_run_grid_parallel(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_navigation_between_pages, self.browser.browser_types)

        else:
            self.test_navigation_between_pages(self.browser.default_browser)





