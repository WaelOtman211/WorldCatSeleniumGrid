import concurrent.futures
import unittest
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.logic_api.user_logic import UserLogic


class TestUserLogic(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()
        self.user_logic = UserLogic(self.my_api)
        self.user_data = self.my_api.user_data_handler
        self.get_user_data = self.user_data.get_user_data()
        self.get_username = self.user_data.get_username()
        self.get_user_id = self.user_data.get_user_id()

    def test_create_user(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url_Pet_Swagger(driver)

        print(self.user_logic.create_user(self.user_data.get_user_data()))
        self.assertEqual(self.user_logic.create_user(self.user_data.get_user_data()).status_code, 200)

    def test_get_user_by_username(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url_Pet_Swagger(driver)

        print(self.user_logic.get_user_by_username(self.get_username))

        expected_user_id = self.get_user_id
        expected_user_email = self.user_data.get_email()
        expected_user_pass = self.user_data.get_password()
        self.assertEqual(self.user_logic.get_user_by_username(self.get_username)['id'],expected_user_id)
        self.assertEqual(self.user_logic.get_user_by_username(self.get_username)['email'], expected_user_email)
        self.assertEqual(self.user_logic.get_user_by_username(self.get_username)['password'], expected_user_pass)

    def test_update_user(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url_Pet_Swagger(driver)

        print(self.user_logic.get_user_by_username(self.get_username)['id'])
        self.assertEqual(self.user_logic.update_user(self.get_username,self.get_user_data).status_code, 200)


    def test_delete_user(self):
        self.assertEqual(self.user_logic.delete_user(self.get_username).status_code, 200)

    def test_run_grid_parallel(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_update_user, self.browser.browser_types)

        else:
            self.test_update_user(self.browser.default_browser)


if __name__ == '__main__':
    unittest.main()
