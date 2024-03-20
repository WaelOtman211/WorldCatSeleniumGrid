import unittest
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.logic_api.pet_logic import PetLogic


class TestPetLogic(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.browser = BrowserWrapper()
        self.pet_logic = PetLogic(self.my_api)
        self.pet_data = self.my_api.pet_data_handler
        self.get_pet_id = self.pet_data.get_pet_id()
        self.get_pet_status = self.pet_data.get_pet_status()
        self.get_pet_name = self.pet_data.get_pet_name()

    def test_add_pet_to_the_store_and_check_correct_adding(self):
        self.assertEqual(self.pet_logic.add_pet(self.pet_data.get_pet_data()).status_code, 200)

    def test_update_pet_by_id(self):

        self.assertEqual(self.pet_logic.update_pet_by_id(self.pet_data.get_pet_data()).status_code, 200)

    def test_find_pet_by_id(self):

        expected_id = self.get_pet_id
        expected_name = self.get_pet_name
        expected_status = self.get_pet_status

        self.assertEqual(self.pet_logic.get_pet_by_id(self.get_pet_id)['id'], expected_id)
        self.assertEqual(self.pet_logic.get_pet_by_id(self.get_pet_id)['name'], expected_name)
        self.assertEqual(self.pet_logic.get_pet_by_id(self.get_pet_id)['status'], expected_status)

    def test_delete_pet_by_id(self):
        self.assertEqual(self.pet_logic.delete_pet_by_id(self.pet_data.get_pet_id()).status_code, 200)



if __name__ == '__main__':
    unittest.main()
