#!/bin/env python
"""
Put module documentation here
"""
import os
import typing
import importlib
import pathlib
import pkgutil
import inspect

import epiphany.logging as logging

from providers.provider import Provider


def get_all_providers() -> typing.Iterable[type]:
    submodules = [
        importlib.import_module("providers." + filename[:-3])
        for filename in os.listdir(pathlib.Path().resolve())
        if filename.endswith(".py")
           and filename != "__init__.py"
    ]
    provider_classes: typing.List[typing.Type] = list()

    for submodule in submodules:
        provider_classes.extend(
            [
                obj
                for name, obj in inspect.getmembers(submodule)
                if inspect.isclass(obj) and Provider in obj.__bases__
            ]
        )

    return provider_classes


def get_providers() -> typing.List[typing.Tuple[str, str]]:
    provider_classes = get_all_providers()

    # TODO: Get the actual path, not just the name
    module_names = [
        (cls.__name__, cls.name())
        for cls in provider_classes
    ]
    return module_names


def get_provider(provider_name: str) -> Provider.__class__:
    provider_classes = get_all_providers()

    provider_classes = [
        cls
        for cls in provider_classes if cls.name() == provider_name
    ]

    if not provider_classes:
        raise ValueError(f"There are no available providers named '{provider_name}'")
    elif len(provider_classes) > 1:
        logging.warn(f"Multiple providers were found with the name of '{provider_name}'; the first will be used.")

    return provider_classes[0]


def test():
    for provider_class_class_name, provider_name in get_providers():
        print(f"[{provider_name}] => {provider_class_class_name}")
    print("Modules retrieved")


if __name__ == "__main__":
    test()
