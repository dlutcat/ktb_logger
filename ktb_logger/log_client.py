#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import logging
import ktb_logger.env as env


class LogHandler(logging.Handler):
    """
    i want to log the msg to backend logger
    but do not need the lock.so overwrite lock method

    """

    def __init__(self, logger, level=logging.NOTSET):
        self._logger = logger
        logging.Handler.__init__(self, level)

    def createLock(self):
        pass

    def acquire(self):
        pass

    def release(self):
        pass

    def emit(self, record):
        msg = self.format(record)
        self._logger.Log(msg)


def _gen_py_logger(logstream, name, level=logging.DEBUG):
    formatter = logging.Formatter('time:%(asctime)s level:%(levelname)s msg:%(message)s')
    py_handler = LogHandler(logstream)
    py_handler.setFormatter(formatter)
    py_logger = logging.getLogger(name)
    py_logger.addHandler(py_handler)
    py_logger.setLevel(level)
    return py_logger


class KTBLogger(object):
    def __init__(self):
        self.inited = False
        self.m = {}

    def init(self, categories, level):

        if env.USE_COROUTINE:
            from coroutine_logger import CoroutineLogger, join_consumers
            XLogger = CoroutineLogger
        else:
            from thread_logger import ThreadLogger, join_consumers
            XLogger = ThreadLogger

        if self.inited:
            return
        with KTBLogger._instance_lock:
            for cate in set(categories):
                self.m[cate] = _gen_py_logger(XLogger(env.HOST, env.PORT, cate), cate, level=level)
            self.inited = True

    _instance_lock = threading.Lock()

    @staticmethod
    def instance():
        if not hasattr(KTBLogger, "_instance"):
            with KTBLogger._instance_lock:
                if not hasattr(KTBLogger, "_instance"):
                    # New instance after double check
                    KTBLogger._instance = KTBLogger()
        return KTBLogger._instance

    def get_logger(self, key):
        return self.m[key]
