import eventlet
import eventlet.wsgi
from urchin.compute import wsgi


eventlet.wsgi.server(eventlet.listen(('', 8090)), wsgi.Resource())


class Service(object):

    def __init__(self, app):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def wait(self):
        pass
