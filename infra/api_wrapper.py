import requests
from infra.config_handler_Pet_swagger import ConfigHandler
from infra.pet_data_handler import PetDataHandler
from infra.store_handler import StoreDataHandler
from infra.user_data_handler import UserDataHandler


class APIWrapper:

    def __init__(self):
        self.response = None
        pet_data_file_path = r'C:\Users\saher\OneDrive\קבצים מצורפים\שולחן העבודה\repos\WorldCatSeleniumGrid\pet_data.json'
        config_pet_swagger_file_path = r'C:\Users\saher\OneDrive\קבצים מצורפים\שולחן העבודה\repos\WorldCatSeleniumGrid\config_Pet_swagger.json'
        store_file_path = r'C:\Users\saher\OneDrive\קבצים מצורפים\שולחן העבודה\repos\WorldCatSeleniumGrid\store.json'
        user_file_path = r'C:\Users\saher\OneDrive\קבצים מצורפים\שולחן העבודה\repos\WorldCatSeleniumGrid\user_data.json'
        self.store_data_handler = StoreDataHandler(store_file_path)
        self.user_data_handler = UserDataHandler(user_file_path)
        self.pet_data_handler = PetDataHandler(pet_data_file_path)
        self.config_handler = ConfigHandler(config_pet_swagger_file_path)
        self.base_url = self.config_handler.get_base_url()
        self.url=None

    def api_get_request(self, endpoint):
        url = self.base_url + endpoint

        self.response = requests.get(url)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_post_request(self, endpoint, data=None):
        self.url = self.base_url + endpoint
        self.response = requests.post(self.url, json=data)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_put_request(self, endpoint, data=None):
        self.url = self.base_url + endpoint
        self.response = requests.put(self.url, json=data)  # Assuming JSON data for PUT request
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_delete_request(self, endpoint):
        url = self.base_url + endpoint
        self.response = requests.delete(url)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code
