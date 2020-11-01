#!/usr/bin/env python3
"""
function filter_datum
"""
import re


def filter_datum(fields, redaction, message, separator):
    """ A function that returns the log message obfuscated """
    lst = message.split(separator)

    for f in fields:
        for i in range(len(lst)):
            if lst[i].startswith(f):
                subst = f + '=' + redaction + separator
                lst[i] = subst
    return separator.join(lst)
