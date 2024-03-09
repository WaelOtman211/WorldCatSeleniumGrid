import json


class UserDataHandler:
    def __init__(self, user_data_file_path):
        self.user_data = self.load_user_data(user_data_file_path)

    def load_user_data(self, user_data_file_path):
        with open(user_data_file_path, 'r') as f:
            return json.load(f)

    def get_user_data(self):
        return self.user_data

    def get_user_id(self):
        return self.user_data.get('id')

    def get_user_first_name(self):
        return self.user_data.get('firstName')

    def get_username(self):
        return self.user_data.get('username')

    def get_email(self):
        return self.user_data.get('email')

    def get_password(self):
        return self.user_data.get('password')



