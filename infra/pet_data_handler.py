import json


class PetDataHandler:
    def __init__(self, pet_data_file_path):
        self.pet_data = self.load_pet_data(pet_data_file_path)

    def load_pet_data(self, pet_data_file_path):
        with open(pet_data_file_path, 'r') as f:
            return json.load(f)

    def get_pet_data(self):
        return self.pet_data

    def get_pet_id(self):
        return self.pet_data.get('id')

    def get_pet_name(self):
        return self.pet_data.get('name')

    def get_pet_status(self):
        return self.pet_data.get('status')





