from user import User


class Admin(User):
    def __init__(self, username, password, access) -> None:
        self.access = access
        super().__init__(username, password)

    def __repr__(self):
        return f'<Admin {self.username}, access {self.access}>'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access
        }