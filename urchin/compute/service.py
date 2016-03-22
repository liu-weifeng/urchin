import eventlet
import eventlet.wsgi
from urchin import service
from urchin.compute import wsgi

class Service(service.ServiceBase):
    def __init__(self):

        self.app = wsgi.Resource()
        self.port = 8080

    def start(self):
        eventlet.wsgi.server(eventlet.listen(('', self.port)),self.app)

    def __call__(self):
        self.start()


