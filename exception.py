#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kerlomz <kerlomz@gmail.com>


class SystemException(RuntimeError):
    def __init__(self, message, code=-1):
        self.message = message
        self.code = code


def exception(text, code=-1):
    raise SystemException(text, code)


class ConfigException:
    SYS_CONFIG_PATH_NOT_EXIST = -4041
    MODEL_CONFIG_PATH_NOT_EXIST = -4042
    CHAR_SET_NOT_EXIST = -4043
    CHAR_SET_INCORRECT = -4043
    INSUFFICIENT_SAMPLE = -5

