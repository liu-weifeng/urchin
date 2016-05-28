import eventlet
import webob


class Request(webob.Request):

    def __init__(self, environ, *args, **kwargs):
        pass

    # def __init__(self, environ, *args, **kwargs):
    #     if CONF.secure_proxy_ssl_header:
    #         scheme = environ.get(CONF.secure_proxy_ssl_header)
    #         if scheme:
    #             environ['wsgi.url_scheme'] = scheme
    #     super(Request, self).__init__(environ, *args, **kwargs)


class Application(object):
    """Base WSGI application wrapper. Subclasses need to implement __call__."""

    def __init__(self, app):
        self.application = app

    def process_request(self, request):
        pass

    def process_response(self, response):
        pass

    @webob.dec.wsgify(RequestClass=Request)
    def __call__(self, req):
        response = self.process_request(req)
        if response:
            return response
        response = req.get_response(self.application)
        return self.process_response(response)
