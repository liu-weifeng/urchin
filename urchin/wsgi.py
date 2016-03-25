import eventlet
import webob
import webob.dec
from urchin import exception
from urchin import compute

class Request(webob.Request):

    def __init__(self, *args, **kargs):

        super(Request, self).__init__(*args, **kargs)

    def get_content_type(self):

        if "Content-Type" not in self.headers:
            return None

        content_type = self.content_type

        # NOTE(markmc): text/plain is the default for eventlet and
        # other webservers which use mimetools.Message.gettype()
        # whereas twisted defaults to ''.
        if not content_type or content_type == 'text/plain':
            return None        


class Resource(object):

    def __init__(self):
        pass

    def get_body(self, request):
        try:
            content_type = request.get_content_type()
        except exception.InvalidContentType:
            LOG.debug("Unrecognized Content-Type provided in request")
            return None, ''

        return content_type, request.body

    def get_controler(self, request):
        path = request.path
        return path

    def get_meth(self, body):
        return body['action']
    
    def dispatch(self, controler, body, request):
        meth = self.get_meth(body)
        func = getattr(controler, meth)
        return func(body, request)

    @webob.dec.wsgify(RequestClass=Request)
    def __call__(self, request):
        content_type, body = self.get_body(request)
        controler = self.get_controler(request)
        return dispatch(controler, body, request)

