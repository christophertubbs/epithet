#!/bin/env python
"""
Put module documentation here
"""
import os
from pathlib import Path
import typing


class __ValueManager(object):
    __TRUE_VALUES = [
        't',
        'T',
        'Y',
        'y',
        1,
        'true',
        'True',
        'Yes',
        'yes',
        True
    ]

    @classmethod
    def __is_true(cls, value: typing.Union[None, int, str, bool]):
        if isinstance(value, str):
            value = value.lower()

        return value in cls.__TRUE_VALUES

    @property
    def base_directory(self) -> Path:
        return Path(__file__).resolve().parent.parent

    @property
    def secret_key(self) -> str:
        return os.environ.get("SECRET_KEY", '@#twt%-m4cw^rzgssb=$qr)hjdi%*58e)efcwq5mqm1^%%80m')

    @property
    def database_backend(self) -> str:
        return os.environ.get("DATABASE_ENGINE", 'django.db.backends.sqlite3')

    @property
    def database_name(self) -> str:
        return os.environ.get("DATABASE_NAME", self.base_directory / 'db.sqlite3')

    @property
    def database_user(self) -> str:
        user = os.environ.get("DATABASE_USER", None)

        if user is not None:
            return user

        backend = self.database_backend.lower()

        if 'post' in backend:
            user = 'postgres'
        elif 'mysql' in backend or 'maria' in backend:
            user = 'root'

        return user

    @property
    def database_password(self) -> str:
        password = os.environ.get("DATABASE_PASSWORD", None)

        if password:
            return password

        backend = self.database_backend.lower()

        if 'post' in backend:
            password = 'postgres'
        elif 'mysql' in backend or 'maria' in backend:
            password = ''

        return password

    @property
    def database_host(self) -> str:
        return os.environ.get("DATABASE_HOST")

    @property
    def database_port(self) -> str:
        port = os.environ.get("DATABASE_PORT", None)

        if port:
            return port

        backend = self.database_backend.lower()

        if 'post' in backend:
            port = '5432'
        elif 'mysql' in backend or 'maria' in backend:
            port = '3306'

        return port

    @property
    def in_debug_mode(self) -> bool:
        in_debug = os.environ.get("DEBUG", True)
        return self.__is_true(in_debug)

    @property
    def time_zone(self) -> str:
        return os.environ.get("TIME_ZONE", "UTC")

    @property
    def use_timezone(self) -> bool:
        use_tz = os.environ.get("UZE_TZ")

        if not use_tz:
            use_tz = True
        else:
            use_tz.lower()

        return self.__is_true(use_tz)


APPLICATION_VALUES = __ValueManager()
