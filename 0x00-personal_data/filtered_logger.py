#!/usr/bin/env python3

"""
This module provides a function for obfuscating log messages.

Functions:
    filter_datum(fields, redaction, message, separator) -> str
"""

import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = None):
        """
        Initialize RedactingFormatter with a list of fields to redact.

        Args:
            fields (list): List of strings representing fields to redact.
        """    
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format log record and redact specified fields.

        Args:
            record (logging.LogRecord): Log record to format.

        Returns:
            str: Formatted and redacted log message.
        """
        msg = logging.Formatter(self.FORMAT).format(record)
        result = filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
        
        return result


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
