from models.base_model import BaseModel


class Player(BaseModel):
    def __init__(self, username, role="user"):
        self.username = username
        self.role = role