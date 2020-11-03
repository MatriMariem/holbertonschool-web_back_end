#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> str:
    """ Encrypting passwords """
    p = password.encode()
    return bcrypt.hashpw(p, bcrypt.gensalt())
