import json


class StoreDataHandler:
    def __init__(self, store_data_file_path):
        self.store_data = self.load_store_data(store_data_file_path)

    def load_store_data(self, store_data_file_path):
        with open(store_data_file_path, 'r') as f:
            return json.load(f)

    def get_store_data(self):
        return self.store_data

    def get_order_id(self):
        return self.store_data.get('id')

    def get_store_pet_id(self):
        return self.store_data.get('petId')

    def get_complete(self):
        return self.store_data.get('complete')

    def get_store_status(self):
        return self.store_data.get('status')

    def get_quantity(self):
        return self.store_data.get('quantity')

    def get_shipDate(self):
        return self.store_data.get('shipDate')




