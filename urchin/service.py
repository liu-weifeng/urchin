import socket

import eventlet
import eventlet.wsgi
import greenlet
import webob.dec
import webob.exc
from urchin import wsgi
import urchin.compute.wsgi

class ServiceBase(object):

    def start(self):
        """start service"""

    def stop(self):
        """stop service"""


class ProcessLauncher(object):

    def launch_service(self, service, workers=1):
        service.start()


class WSGIService(object):
    """wsgi server"""

    def __init__(self, name, loader=None, use_ssl=False, max_url_len=None):
        """Initialize, but do not start the WSGI server.

        :param name: The name of the WSGI server given to the loader.
        :param loader: Loads the WSGI application using the given name.
        :returns: None

        """
        self.name = name
        # NOTE(danms): Name can be metadata, os_compute, or ec2, per
        # nova.service's enabled_apis
        self.binary = 'nova-%s' % name
        self.topic = None
        # self.manager = self._get_manager()
        # self.loader = loader or wsgi.Loader()
        # self.app = self.loader.load_app(name)
        self.app = urchin.compute.wsgi.InstanceService
        # inherit all compute_api worker counts from osapi_compute

        self.host = "0.0.0.0"
        self.port = 8080
        self.workers = 1
        self.use_ssl = use_ssl
        self.server = wsgi.Server(name,
                                  self.app,
                                  host=self.host,
                                  port=self.port,
                                  use_ssl=self.use_ssl,
                                  max_url_len=max_url_len)
        # Pull back actual port used
        self.port = self.server.port
        self.backdoor_port = None

    def start(self):

        # if self.manager:
        #     self.manager.init_host()
        #     self.manager.pre_start_hook()
        #     if self.backdoor_port is not None:
        #         self.manager.backdoor_port = self.backdoor_port
        self.server.start()
        # if self.manager:
        #     self.manager.post_start_hook()

    def reset(self):
        """Reset server greenpool size to default.

        :returns: None

        """
        self.server.reset()
    def stop(self):
        """Stop serving this API.

        :returns: None

        """
        self.server.stop()

    def wait(self):
        """Wait for the service to stop serving this API.

        :returns: None

        """
        self.server.wait()