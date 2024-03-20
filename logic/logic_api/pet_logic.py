

class PetLogic:
    def __init__(self, api_object):
        self.api = api_object

    def get_pet_by_id(self, pet_id):
        return self.api.api_get_request(f'v2/pet/{pet_id}').json()

    def add_pet(self, pet_data):
        return self.api.api_post_request('v2/pet', data=pet_data)

    def update_pet_by_id(self, pet_data):
        return self.api.api_put_request(f'v2/pet/', data=pet_data)

    def delete_pet_by_id(self, pet_id):
        return self.api.api_delete_request(f'v2/pet/{pet_id}')
