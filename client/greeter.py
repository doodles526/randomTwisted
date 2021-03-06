from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint

class Greeter(Protocol):
    def sendMessage(self, msg):
        self.transport.write("MESSAGE %s \n" % msg) 

class GreeterFactory(Factory):
    def buildProtocol(self, addr):
        return Greeter()

def gotProtocol(p):
    p.sendMessage("Hello")
    reactor.callLater(1, p.sengMessage, "This is sent in a second")
    reactor.callLater(2, p.transport.loseConnection)

point = TCP4ClientEndpoint(reactor, 'localhost', 1234)
d = point.connect(GreeterFactory())
d.addCallback(gotProtocol)
reactor.run()
