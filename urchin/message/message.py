import threading

class Message(object):
    def __init__(self):
        pass


class EventMessage(Message):

    def __init__(self, uuid, obj):
        super(EventMessage, self).__init__()
        self.uuid = uuid
        self.object = obj

    

class MessageQueue(object):
    
    def __init__(self):

        self._list = []
        self.lock = threading.Lock()

    def get():
        pass
