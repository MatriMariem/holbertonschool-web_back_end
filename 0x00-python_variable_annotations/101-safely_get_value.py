#!/usr/bin/env python3
""" a type-annotated function safely_get_value """
from typing import Any, Mapping, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[~T, None] = None):
    """ function safely_get_value """
    if key in dct:
        return dct[key]
    else:
        return default
