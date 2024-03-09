

class StoreLogic:
    def __init__(self, api_object):
        self.api = api_object

    def get_inventory(self):
        return self.api.api_get_request('/store/inventory')

    def place_order(self, order_data):
        return self.api.api_post_request('v2/store/order', data=order_data)

    def get_order_by_id(self, order_id):
        return self.api.api_get_request(f'v2/store/order/{order_id}').json()

    def delete_order(self, order_id):
        return self.api.api_delete_request(f'v2/store/order/{order_id}')
