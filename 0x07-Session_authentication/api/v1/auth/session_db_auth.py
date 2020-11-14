#!/usr/bin/env python3
""" SessionDBAuth inherits from SessionExpAuth """
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta
from flask import request


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class """

    def create_session(self, user_id=None):
        """
        creates and stores new instance of UserSession
        and returns the Session ID
        """
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        session_data = {"user_id": user_id, "session_id": session_id}
        obj = UserSession(**session_data)
        obj.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        returns the User ID
        by requesting UserSession in the database based on session_id
        """
        if not session_id:
            return None
        try:
            objs = UserSession.search({"session_id": session_id})
            if not objs or len(objs) == 0:
                return None
            if session_id not in self.user_id_by_session_id:
                return None
            if "created_at" not in self.user_id_by_session_id[session_id]:
                return None
            limit_date = (timedelta(seconds=self.session_duration) +
                          self.user_id_by_session_id[session_id]["created_at"])
            if limit_date < datetime.now():
                self.destroy_session(request)
                return None
            return objs[0].user_id
        except Exception as e:
            return None

    def destroy_session(self, request=None):
        """ Destroy a current session """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        try:
            sessions = UserSession.search({session_id: session_id})
            if sessions is None:
                return False

            sessions[0].remove()

            return True

        except ValueError:
            return False
