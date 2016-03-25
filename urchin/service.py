import eventlet
import eventlet.wsgi
class ServiceBase(object):
    def __init__(self):
        pass

    def __call__(self):
        self.start()


class Service(ServiceBase):
    def __init__(self):

        self.app = wsgi.Resource()
        self.port = 8080

    def start(self):
        eventlet.wsgi.server(eventlet.listen(('', self.port)),self.app)

    def __call__(self):
        self.start()
