#!/usr/bin/env python3
"""
Basic auth
"""

import base64
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

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decode the Base64 authorization header.

        Return None if base64_authorization_header is None.
        Return None if base64_authorization_header is not a string.
        Return None if base64_authorization_header is not a valid Base64 - you can use try/except.
        Otherwise, return the decoded value as UTF8 string - you can use decode('utf-8').
        """
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None

        try:
            # Decode Base64 and convert to UTF-8
            decoded_value = base64.b64decode(base64_authorization_header).decode('utf-8')
            return decoded_value
        except base64.binascii.Error:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extract the user email and password from the Base64 decoded value.

        Return None, None if decoded_base64_authorization_header is None.
        Return None, None if decoded_base64_authorization_header is not a string.
        Return None, None if decoded_base64_authorization_header doesn’t contain :.
        Otherwise, return the user email and the user password - these 2 values must be separated by :.
        You can assume decoded_base64_authorization_header will contain only one :.
        """
        if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_email, user_password = decoded_base64_authorization_header.split(':', 1)

        return user_email, user_password
