#!/bin/env python
"""
Put module documentation here
"""

import typing
import pathlib
import json

import requests
import aiohttp

import pandas

from providers.provider import Provider


class InstantaneousNWIS(Provider):
    __root_url = "https://waterservices.usgs.gov/nwis/iv/?format=json"
    def get_dataset(self, **kwargs) -> pandas.DataFrame:
        pass

    async def get_data_async(self, **kwargs) -> pandas.DataFrame:
        pass

    _name = "Instantaneous NWIS"


class DailyNWIS(Provider):
    __root_url = "https://waterservices.usgs.gov/nwis/dv/?format=json"

    def get_dataset(self, **kwargs) -> pandas.DataFrame:
        pass

    async def get_data_async(self, **kwargs) -> pandas.DataFrame:
        pass

    _name = "Daily NWIS"
