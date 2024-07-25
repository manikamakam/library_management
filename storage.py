import json
import os

class Storage:
    """
    Class for handling file operations.
    """

    def __init__(self, filename):
        """
        Initializes the storage filename

        Args:
            filename (str): The name of the file for storing data.
        """
        self.filename = filename

    def load_data(self, cls):
        """
        Loads data from the file and returns instances of the specified class.

        Args:
            cls (type): The class type to instantiate objects from the data.

        Returns:
            dict: A dictionary of objects keyed by their unique identifier.
        """
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r") as file:
            data = json.load(file)
        return {key: cls.from_dict(value) for key, value in data.items()}

    def save_data(self, data):
        """
        Saves data to the file.

        Args:
            data (dict): A dictionary of objects to be saved, keyed by their unique identifier.
        """
        with open(self.filename, "w") as file:
            json.dump({key: value.to_dict() for key, value in data.items()}, file, indent=4)
