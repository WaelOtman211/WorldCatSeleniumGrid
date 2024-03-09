

class UserLogic:
    def __init__(self, api_object):
        self.api = api_object

    def create_user(self, user_data):
        return self.api.api_post_request('v2/user', data=user_data)

    def get_user_by_username(self, username):
        return self.api.api_get_request(f'v2/user/{username}').json()

    def update_user(self, username, user_data):
        return self.api.api_put_request(f'v2/user/{username}', data=user_data)

    def delete_user(self, username):
        return self.api.api_delete_request(f'v2/user/{username}')
