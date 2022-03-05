#!/bin/env python
"""
Put module documentation here
"""
import typing

from utilities.decorators import choices


@choices
def content_types() -> typing.List[typing.Tuple[str, str]]:
    return [
        ("line", "Line"),
        ("map", "Map")
    ]


@choices
def value_types() -> typing.List[typing.Tuple[str, str]]:
    return [
        ("integer", "Integer"),
        ("float", "Float"),
        ("string", "String"),
        ("boolean", "Boolean")
    ]


@choices
def css_styles() -> typing.List[typing.Tuple[str, str]]:
    return [
        ("color", "Text Color"),
        ("padding", "Padding"),
        ("margin", "Margin"),
        ("background", "Background"),
        ("cursor", "Cursor"),
    ]
