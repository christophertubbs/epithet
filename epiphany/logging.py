#!/bin/env python
"""
Put module documentation here
"""
import os
import logging
import typing
import sys

from logging import INFO
from logging import WARNING
from logging import ERROR
from logging import DEBUG

DEFAULT_LOGGER_NAME = os.environ.get("DEFAULT_LOGGER_NAME", "epiphany")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/epiphany.log',
            'maxBytes': 1024*1024*10, # 10MB
            'backupCount': 10,
            'formatter': 'default',
        }
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        },
    },
    DEFAULT_LOGGER_NAME: {
        'handlers': ['console'],
        'level': 'WARNING',

    },
}


def log(
        message: str,
        level: typing.Union[int, str] = None,
        logger_name: str = None,
        exception: typing.Union[typing.Tuple, BaseException] = None
):
    if logger_name is None:
        logger_name = DEFAULT_LOGGER_NAME

    if level is None:
        level = INFO
    elif isinstance(level, str):
        level = logging.getLevelName(level.upper())

    logger = logging.getLogger(logger_name)

    logger.log(level, message, exc_info=exception)


def info(message: str, logger_name: str = None, exception: typing.Union[typing.Tuple, BaseException] = None):
    log(message, INFO, logger_name, exception)


def warn(message: str, logger_name: str = None, exception: typing.Union[typing.Tuple, BaseException] = None):
    log(message, WARNING, logger_name, exception)


def error(message: str, logger_name: str = None, exception: typing.Union[typing.Tuple, BaseException] = None):
    if not exception or not isinstance(exception, tuple) and not isinstance(exception, BaseException):
        exception = sys.exc_info()

    log(message, ERROR, logger_name, exception)


def debug(message: str, logger_name: str = None, exception: typing.Union[typing.Tuple, BaseException] = None):
    log(message, DEBUG, logger_name, exception)
