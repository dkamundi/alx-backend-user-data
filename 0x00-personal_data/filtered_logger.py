#!/usr/bin/env python3

"""
This module provides a function for obfuscating log messages.

Functions:
    filter_datum(fields, redaction, message, separator) -> str
"""

import re
from typing import List

def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message.

    Args:
        fields (list): A list of strings representing fields to obfuscate.
        redaction (str): A string representing the redaction to use.
        message (str): A string representing the log line.
        separator (str): A string representing the character separating fields.

    Returns:
        str: The obfuscated log message.
    """
    for field in fields:
        expression = "(?<={}=)(.*?)(?={})".format(re.escape(field), re.escape(separator))
        message = re.sub(expression, redaction, message)

    return message


if __name__ == "__main__":
    main()
