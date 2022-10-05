import secrets

class User:
    def __init__(self, username, password):
        self._usrname = username
        self._pwd = self.__hash_pwd__(password)
        self._id = secrets.token_hex(15)

    @property
    def username(self):
        return self._usrname

    @property
    def id(self):
        return self._id 

    @property
    def password(self):
        return "not found"

    def __hash_pwd__(self, pwd):
        return pwd


class Admin(User):
    pass

class wallet:
    pass

u = User("lusm", "123")



