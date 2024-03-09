import unittest
from infra.api_wrapper import APIWrapper
from logic.user_logic import UserLogic


class TestUserLogic(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.user_logic = UserLogic(self.my_api)
        self.user_data = self.my_api.user_data_handler
        self.get_user_data = self.user_data.get_user_data()
        self.get_username = self.user_data.get_username()
        self.get_user_id = self.user_data.get_user_id()

    def test_create_user(self):
        print(self.user_data.get_user_data())
        self.assertEqual(self.user_logic.create_user(self.user_data.get_user_data()).status_code, 200)

    def test_get_user_by_username(self):
        expected_user_id = self.get_user_id
        expected_user_email = self.user_data.get_email()
        expected_user_pass = self.user_data.get_password()
        self.assertEqual(self.user_logic.get_user_by_username(self.get_username)['id'],expected_user_id)
        self.assertEqual(self.user_logic.get_user_by_username(self.get_username)['email'], expected_user_email)
        self.assertEqual(self.user_logic.get_user_by_username(self.get_username)['password'], expected_user_pass)

    def test_update_user(self):
        self.assertEqual(self.user_logic.update_user(self.get_username,self.get_user_data).status_code, 200)


    def test_delete_user(self):
        self.assertEqual(self.user_logic.delete_user(self.get_username).status_code, 200)



if __name__ == '__main__':
    unittest.main()
