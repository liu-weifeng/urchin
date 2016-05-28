import eventlet
import webob
import webob.dec


class Request(webob.Request):

    def __init__(self, environ, *args, **kwargs):
        pass

    # def __init__(self, environ, *args, **kwargs):
    #     if CONF.secure_proxy_ssl_header:
    #         scheme = environ.get(CONF.secure_proxy_ssl_header)
    #         if scheme:
    #             environ['wsgi.url_scheme'] = scheme
    #     super(Request, self).__init__(environ, *args, **kwargs)


class Middleware(object):

    @classmethod
    def factory(cls, global_config, **local_config):

        def _factory(app):
            return cls(app, **local_config)
        return _factory

    def __init__(self, application):
        self.application = application

    def process_request(self, req):
        return None

    def process_response(self, response):
        return response

    @webob.dec.wsgify(RequestClass=Request)
    def __call__(self, req):
        response = self.process_request(req)
        if response:
            return response
        response = req.get_response(self.application)
        return self.process_response(response)
