import json


class ConfigHandler:
    def __init__(self, config_file_path):
        self.config = self.load_config(config_file_path)

    def load_config(self, config_file_path):
        with open(config_file_path, 'r') as f:
            return json.load(f)

    def get_base_url(self):
        return self.config.get('base_url')




