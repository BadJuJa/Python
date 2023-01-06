import json
import os


class Settings:
    def __init__(self):
        self.paths = self.get_and_validate_settings()

    example_settings = {
            'art_path': '',
            'ero_path': '',
            'porn_path': '',
            'current_folder_path': os.getcwd()
        }

    def create_settings(self):
        with open('settings.json', 'w', encoding='utf-8') as f:
            json.dump(self.example_settings, f, ensure_ascii=False, indent=4)

    def get_settings(self):
        with open('settings.json', 'r') as f:
            sets = json.load(f)
        return sets

    def validate_settings(self, sets):
        key_set_1 = set(sets.keys())
        key_set_2 = set(self.example_settings.keys())
        if key_set_1 == key_set_2:
            return sets
        else:
            os.remove('settings.json')
            self.create_settings()
            return self.get_settings()

    def get_and_validate_settings(self):
        return self.validate_settings(self.get_settings())

    def rewrite_settings(self, arg=None):
        if arg is None:
            arg = self.paths
        with open('settings.json', 'w', encoding='utf-8') as f:
            json.dump(arg, f, ensure_ascii=False, indent=4)

    def update_paths(self):
        self.paths = self.get_settings()
