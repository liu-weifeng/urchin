import socket

import eventlet
import eventlet.wsgi
import greenlet
import webob.dec
import webob.exc


class Request(webob.Request):
    def __init__(self, environ, *args, **kwargs):
        super(Request, self).__init__(environ, *args, **kwargs)


class Middleware(object):

    def process_request(self, req):
        """Called on each request.

        If this returns None, the next application down the stack will be
        executed. If it returns a response then that response will be returned
        and execution will stop here.

        """
        return None

    def process_response(self, response):
        """Do whatever you'd like to the response."""
        return response

    @webob.dec.wsgify(RequestClass=Request)
    def __call__(self, req):

        response = self.process_request(req)
        if response:
            return response
        response = req.get_response(self.application)
        return self.process_response(response)


class Application(Middleware):

    @webob.dec.wsgify(RequestClass=Request)
    def __call__(self, request):
        pass


"""
class Loader(object):


    def __init__(self, config_path=None):

        self.config_path = None

        config_path = config_path or CONF.api_paste_config
        if not os.path.isabs(config_path):
            self.config_path = CONF.find_file(config_path)
        elif os.path.exists(config_path):
            self.config_path = config_path

        if not self.config_path:
            raise exception.ConfigNotFound(path=config_path)

    def load_app(self, name):

        try:
            LOG.debug("Loading app %(name)s from %(path)s",
                      {'name': name, 'path': self.config_path})
            return deploy.loadapp("config:%s" % self.config_path, name=name)
        except LookupError:
            LOG.exception(_LE("Couldn't lookup app: %s"), name)
            raise exception.PasteAppNotFound(name=name, path=self.config_path)
"""