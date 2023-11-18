#!/usr/bin/env python3
"""Module deals with authentication"""
import bcrypt

class DB:
    def _hash_password(password: str) -> bytes:
    """Returns bytes as a salted hash of the input password"""
    hashed_pwd = hashpw(password.encode("utf-8"), gensalt())
    return hashed_pwd
