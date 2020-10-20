#!/usr/bin/env python3
""" asynchronous coroutine """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    asynchronous coroutine wait_random that
    takes in an integer argument
    (max_delay, with a default value of 10)
    and waits for a random delay between 0 and max_delay
    (included and float value) seconds
    and eventually returns it
    """
    l = [
        wait_random(max_delay) for i in range(n)
    ]
    rs = []
    for x in asyncio.as_completed(l):
        r = await x
        rs.append(r)
    return rs
