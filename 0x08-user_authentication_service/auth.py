#!/usr/bin/env python3
""" Password Hashing """
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """
    The returned string is a salted hash of the input password,
    hashed with bcrypt.hashpw
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        "create instance of db"
        self._db = DB()

    def register_user(email: str, password: str) -> User:
        """ registers a new user """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hpassword = _hash_password(password)
            user = self._db.add_user(email=email, password=hpassword)
            return user
