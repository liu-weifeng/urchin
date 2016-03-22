import eventlet.greenpool
import webob
import webob.dec
import eventlet


class ProcessLauncher(object):

    def __init__(self):
        self.green_pool = eventlet.greenpool.GreenPool()

    def launch_service(self, service, workers=1):
        self.green_pool.spawn(service)

    def wait(self):

        self.green_pool.waitall()


# test wsgi
class Resource(object):
    
    @webob.dec.wsgify
    def __call__(self, request):
        import pdb;pdb.set_trace()
        print request.body



if __name__ == '__main__':
    def func():
        import syslog, time
        for i in range(10):
            time.sleep(1)
            syslog.syslog(syslog.LOG_ERR, 'test processlanceher %d' % i)

    def func2():
        import syslog, time
        for i in range(10):
            time.sleep(2)
            syslog.syslog(syslog.LOG_ERR, 'test processlanceher 2 %d' % i)
    launcher = ProcessLauncher()
    launcher.launcher_service(func)
    launcher.launcher_service(func2)
    launcher.wait()
