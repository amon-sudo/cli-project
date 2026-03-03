import json
import os

DATA_FOLDER = "data"


class FileStorage:
    def __init__(self, filename):
        os.makedirs(DATA_FOLDER, exist_ok=True)
        self.filename = os.path.join(DATA_FOLDER, filename)

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def load(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)