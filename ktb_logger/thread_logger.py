from Queue import Queue
from Queue import Full
import threading
from logger_base import SLogger

__all__ = ['ThreadLogger', 'join_consumers']

all_consumers = []
def join_consumers():
    for consumer in all_consumers:
        consumer.join()

class ThreadLogger(SLogger):
    """
    A thread safe logger
    """
    def __init__(self, host, port, category, qsize=100000):
        SLogger.__init__(self, host, port, category, qsize)
        self._q = Queue(qsize)
        self._consumer.start()

    def _create_consumer(self):
        self._consumer = threading.Thread(target=self._consumer_func)
        self._consumer.setDaemon(True)
        all_consumers.append(self._consumer)

    def _consumer_func(self):
        while True:
            msg = self._q.get()
            self._log_to_server(msg)
            self._q.task_done()
