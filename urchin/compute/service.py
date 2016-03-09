from urchin import service
from urchin.service import ServiceBase

class Service(ServiceBase):

    def __init__(self):
        self.wsgi = service.WSGIService

    def start(self):
        pass




