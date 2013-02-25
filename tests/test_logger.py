#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging

import ktb_logger.env as env
from ktb_logger.log_client import KTBLogger

if env.USE_COROUTINE:
    from ktb_logger.coroutine_logger import CoroutineLogger, join_consumers
    XLogger = CoroutineLogger
else:
    from ktb_logger.thread_logger import ThreadLogger, join_consumers


env.HOST = '127.0.0.1'
env.PORT = 1463
env.LOG_CATEGORIES = [ 'access', ]
env.LOG_LEVEL = logging.DEBUG


def test_log():
    ktb_logger = KTBLogger.instance()
    ktb_logger.init(categories=env.LOG_CATEGORIES, level=env.LOG_LEVEL)

    # Access logger
    env.as_log = ktb_logger.get_logger('access')
    env.as_log.error('test1')
    env.as_log.error('test2')
    join_consumers()
