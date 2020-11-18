#!/usr/bin/env python3
""" Database module
"""

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from typing import TypeVar

from user import Base
from user import User


class DB:
    """ Database for SQLAlchemy.
        Handles creation of session and engine, as well as construction of the
        ORM.
        Methods:
            add_user: Add user to the User table.
            find_user_by: find a user in the User table.
            update_user: update a user at a user ID.
    """

    def __init__(self):
        """ Initialize engine """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ Create session """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> TypeVar('User'):
        """ Add a user instance to the session DB """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user
