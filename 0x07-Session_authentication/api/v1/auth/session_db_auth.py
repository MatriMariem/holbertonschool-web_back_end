#!/usr/bin/env python3
""" SessionDBAuth inherits from SessionExpAuth """
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


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
        objs = UserSession.search({"session_id": session_id})
        if not objs or len(objs) == 0:
            return None
        return objs[0].user_id

    def destroy_session(self, request=None):
        """
        destroys the UserSession
        based on the Session ID from the request cookie
        """
        if not request:
            return None
        session_id = self.session_cookie(request)
        objs = UserSession.search({"session_id": session_id})
        if objs and len(objs) > 0:
            objs[0].remove()
