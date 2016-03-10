from urchin.wsgi import Middleware
import webob.dec
import eventlet
import six
import abc
import socket
from urchin import utils
from urchin import wsgi


class Request(webob.Request):
    def __init__(self, environ, *args, **kwargs):
        super(Request, self).__init__(environ, *args, **kwargs)


class InstanceService(wsgi.Application):
    @webob.dec.wsgify(RequestClass=Request)
    def __call__(self, request):
        args = request['wsgiorg.routing_args'][1].copy()
        print args

