from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class QOTD(Protocol):
    def connectionMade(self):
        self.transport.write(self.factory.quote + '\r\n')
        self.transport.loseConnection()

class QOTDFactory(Factory):
    
    protocol = QOTD

    def __init__(self, quote=None):
        self.quote = quote or 'An apple a day keeps the doctor away'

endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(QOTDFactory('configurable quote'))
reactor.run()
