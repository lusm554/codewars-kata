import secrets
import hashlib, uuid

class User:
    _salt = uuid.uuid4().hex # remove salt if need to verify pwd not only in scope of class object
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
        return self._pwd

    def is_pwd_correct(self, pwd_to_verify):
        return self.__hash_pwd__(pwd_to_verify) == self._pwd

    def __hash_pwd__(self, pwd):
        pwd = hashlib.sha512(pwd.encode("utf-8") + self._salt.encode("utf-8")).hexdigest()
        return pwd


class Admin(User):
    pass

class Wallet:
    pass

u = User("lusm", "123")

print(
    u.is_pwd_correct("123")
)


