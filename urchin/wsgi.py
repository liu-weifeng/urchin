import eventlet
import webob
import webob.dec


class Request(webob.Request):
    pass


class Application(object):

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
        import pdb;pdb.set_trace()
        response = self.process_request(req)
        if response:
            return response
        response = req.get_response(self.application)
        return self.process_response(response)
