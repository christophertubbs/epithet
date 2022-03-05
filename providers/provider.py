#!/bin/env python
"""
Put module documentation here
"""
import abc

import pandas


class Provider(abc.ABC):
    _name = "Base Provider"

    @classmethod
    def name(cls) -> str:
        if cls._name == Provider._name:
            raise ValueError(f"A custom name needs to be set for the Provider named {cls.__name__}")

        return cls._name

    @abc.abstractmethod
    def get_dataset(self, **kwargs) -> pandas.DataFrame:
        pass

    @abc.abstractmethod
    async def get_data_async(self, **kwargs) -> pandas.DataFrame:
        pass
