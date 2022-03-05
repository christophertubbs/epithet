#!/bin/env python
"""
Put module documentation here
"""
import typing

_choice = typing.Tuple[str, str]


def choices(func: typing.Callable[[], typing.List[_choice]]) -> typing.Callable[[], typing.List[_choice]]:
    """
    Decorator for functions that return lists of values formatted like [database value, screen choice] that adds each value as a member

    :param func: A function that returns a list of tuples formatted as [database value, screen choice]
    :return: That same function except each choice is also a member of the function
    """
    for database_value, screen_choice in func():
        screen_choice = screen_choice.replace(" ", "_")
        setattr(func, screen_choice, database_value)

    return func
