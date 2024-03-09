import concurrent.futures
import unittest
from unittest.mock import MagicMock

from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.store_logic import StoreLogic


class TestStoreLogic(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()
        self.store_logic = StoreLogic(self.my_api)
        self.store_data = self.my_api.store_data_handler
        self.pet_data = self.my_api.pet_data_handler
        self.order_id = self.store_data.get_order_id()

    def test_place_order(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url_Pet_Swagger(driver)

        self.assertEqual(self.store_logic.place_order(self.store_data.get_store_data()).status_code, 200)

    def test_get_order_by_id(self,browser):
        driver = self.browser.get_driver(browser)
        self.browser.get_url_Pet_Swagger(driver)


        print(self.store_logic.get_order_by_id(self.order_id))
        expected_pet_id = self.pet_data.get_pet_id()
        expected_order_id = self.store_data.get_order_id()
        expected_order_quantity = self.store_data.get_quantity()
        self.assertEqual(expected_pet_id, self.store_logic.get_order_by_id(self.order_id)['petId'])
        self.assertEqual(expected_order_id, self.store_logic.get_order_by_id(self.order_id)['id'])
        self.assertEqual(expected_order_quantity, self.store_logic.get_order_by_id(self.order_id)['quantity'])

    def test_delete_order(self):
        self.assertEqual(self.store_logic.delete_order(self.order_id).status_code, 200)

    def test_run_grid_parallel(self):
        if self.browser.grid_enabled and not self.browser.serial_enabled:
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.browser.browser_types)) as executor:
                executor.map(self.test_get_order_by_id, self.browser.browser_types)

        else:
            self.test_get_order_by_id(self.browser.default_browser)

if __name__ == '__main__':
    unittest.main()
