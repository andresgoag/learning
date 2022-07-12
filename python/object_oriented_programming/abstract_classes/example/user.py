from saveable import Saveable


class User(Saveable):
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def login(self):
        return 'logged in'

    def __repr__(self) -> str:
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }