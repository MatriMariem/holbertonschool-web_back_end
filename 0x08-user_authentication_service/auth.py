#!/user/bin/env python3
""" Password Hashing """
import bcrypt


def _hash_password(password: str) -> str:
    """
    The returned string is a salted hash of the input password,
    hashed with bcrypt.hashpw
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
