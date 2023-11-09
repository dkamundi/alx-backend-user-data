#!/usr/bin/env python3
"""
API authentication module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class for managing API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required for the given path 
        Returns True if path is None.
        Returns True if excluded_paths is None or empty.
        Returns False if path is in excluded_paths.
        Slash tolerant: path=/api/v1/status and path=/api/v1/status/
        must return False if excluded_paths contains /api/v1/status/
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if path.endswith('/') and excluded_path == path[:-1]:
                return False
            elif not path.endswith('/') and excluded_path + '/':
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from the request """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user from the request """
        return None
