from abc import ABC, abstractmethod
import secrets
import hashlib, uuid

class User(ABC):
    __roles = "r"
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
        pwd = hashlib.sha512(pwd.encode("utf-8")).hexdigest()
        return pwd

    def isadmin(self):
        return False 


class Admin(User):
    __roles = "rwx"
    def __init__(self, username, password):
        super().__init__(username, password)

    def set_pwd(self, actuall_pwd, new_pwd):
        if self.is_pwd_correct(actuall_pwd):
            self._pwd = self.__hash_pwd__(new_pwd)

    def isadmin(self):
        return True

class Wallet(User):
    pass

