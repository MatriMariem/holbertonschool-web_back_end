#!/usr/bin/env python3
"""
Database class
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User
from typing import Dict
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """ Database class for SQLAlchemy """

    def __init__(self):
        """ creates engine """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ creates a session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ This method saves a new user to the database """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: Dict) -> User:
        """
        This method takes in arbitrary keyword arguments
        and returns the first row found in the users table
        as filtered by the method’s input arguments.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
        except InvalidRequestError:
            raise InvalidRequestError
        if user is None:
            raise NoResultFound
        else:
            return user
        return user

    def update_user(self, user_id: int, **kwargs: Dict) -> None:
        """
        The method will use find_user_by to locate the user to update,
        then will update the user’s attributes
        as passed in the method’s arguments
        then commit changes to the database.
        """
        user = self.find_user_by(id=user_id)
        try:
            for k, v in kwargs:
                user.k = v
        except Exception as e:
            raise ValueError
        self._session.commit()
