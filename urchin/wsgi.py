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