from scribe import scribe
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol

class SLogger(object):
    def __init__(self, host, port, category, qsize=100000):
        self._host = host
        self._port = port
        self._category = category
        self._client = None
        self._transport = None
        self._conn()
        self._consumer = None
        self._create_consumer()

    def _conn(self):
        socket = TSocket.TSocket(host=self._host, port=self._port)
        self._transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(trans=self._transport,
                            strictRead=False, strictWrite=False)
        self._client = scribe.Client(iprot=protocol, oprot=protocol)
        self._transport.open()

    def _close(self):
        self._transport.close()

    def _create_consumer(self):
        raise NotImplementedError('_create_consumer not implemented')

    def _consumer_func(self):
        raise NotImplementedError('_create_consumer not implemented')

    def _log_to_server(self, msg):
        log_entry = scribe.LogEntry(category=self._category, message=msg)
        result = self._client.Log(messages=[log_entry])
        if result != scribe.ResultCode.OK:
            print result

    def Log(self, msg):
        try:
            self._q.put_nowait(msg)
        except Full:
            print 'queue is full,drop msg'
