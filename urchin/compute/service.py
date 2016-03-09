from urchin.compute.wsgi import WSGIServer
from urchin.service import ServiceBase

class Service(ServiceBase):

    def __init__(self):
        self.wsgi = WSGIServer()

    def start(self):
        pass




