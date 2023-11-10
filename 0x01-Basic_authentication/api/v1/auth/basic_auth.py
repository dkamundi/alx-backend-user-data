#!/usr/bin/env python3
"""
Basic auth
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class for basic authentication """
    
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extract the Base64 part of the Authorization header for Basic Authentication.

        Return None if authorization_header is None.
        Return None if authorization_header is not a string.
        Return None if authorization_header doesn’t start by Basic (with a space at the end).
        Otherwise, return the value after Basic (after the space).
        You can assume authorization_header contains only one Basic.
        """
        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        base64_value = authorization_header.replace('Basic ', '', 1)

        return base64_value
