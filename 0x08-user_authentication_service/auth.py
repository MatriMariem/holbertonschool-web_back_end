#!/usr/bin/env python3
""" Password Hashing """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """
    The returned string is a salted hash of the input password,
    hashed with bcrypt.hashpw
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())7


def _generate_uuid() -> str:
    """
    return a string representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        "create instance of db"
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ registers a new user """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hpassword = _hash_password(password)
            user = self._db.add_user(email, hpassword)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ checks if the password is correct for the user """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False
