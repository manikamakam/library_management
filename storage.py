import json
import os

class Storage:
    _instances = {}

    def __new__(cls, filename):
        if filename not in cls._instances:
            cls._instances[filename] = super(Storage, cls).__new__(cls)
        return cls._instances[filename]

    def __init__(self, filename):
        self.filename = filename

    def load_data(self, cls):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r") as file:
            data = json.load(file)
        return {key: cls.from_dict(value) for key, value in data.items()}

    def save_data(self, data):
        with open(self.filename, "w") as file:
            json.dump({key: value.to_dict() for key, value in data.items()}, file, indent=4)
