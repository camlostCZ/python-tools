"""
timetools.py

Useful time-processing functions.
"""

from typing import Any, Callable

import functools
import time


def timer(func: Callable, repeat: int = 1) -> Any:
    """
    Measure time function takes to complete.

    Arguments:
        func - function measured
        repeat number of time function should be executed

    Returns:
        time it takes to execute 'funct' as many as 'repeat'-times.
    """

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        t_start = time.perf_counter()
        for _ in range(repeat):
            func(*args, **kwargs)
        t_end = time.perf_counter()
        t_delta = t_end - t_start
        return t_delta

    return wrapper_timer
