import gevent
from gevent.queue import Queue
from gevent.queue import Full
from logger_base import SLogger

__all__ = ['CoroutineLogger', 'join_consumers']

all_consumers = []
def join_consumers():
    gevent.joinall(all_consumers)


class CoroutineLogger(SLogger):
    def __init__(self, host, port, category, qsize=100000):
        SLogger.__init__(self, host, port, category, qsize)
        self._q = Queue(qsize)
        self._create_consumer()

    def _create_consumer(self):
        self._consumer = gevent.spawn(self._consumer_func)
        all_consumers.append(self._consumer)

    def _consumer_func(self):
        while True:
            msg = self._q.get()
            self._log_to_server(msg)
