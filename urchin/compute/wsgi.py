import webob.dec

from urchin import exception

_SUPPORTED_CONTENT_TYPES = (
    'application/json',
    'application/vnd.openstack.compute+json',
    'text', # just for test
)

def get_supported_content_types():
    return _SUPPORTED_CONTENT_TYPES

class Request(webob.Request):
    def get_content_type():
        if "Content-Type" not in self.headers:
            return None

        content_type = self.content_type

        # NOTE(markmc): text/plain is the default for eventlet and
        # other webservers which use mimetools.Message.gettype()
        # whereas twisted defaults to ''.
        if not content_type or content_type == 'text/plain':
            return None

        if content_type not in get_supported_content_types():
            raise exception.InvalidContentType(content_type=content_type)

        return content_type

class Resource(object):

    def get_body(self, request):
        try:
           content_type = request.get_content_type()
        except:
           return None, b''

        return content_type, request.body

    def dispatch(self):
        pass
    
    @webob.dec.wsgify
    def __call__(self, request):
        import pdb;pdb.set_trace()
        content_type, body = self.get_body(request) 
        print content_type
        print body

@webob.dec.wsgify
def fun(request):
    print request.body


