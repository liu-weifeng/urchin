import eventlet
from eventlet import wsgi
from urchin.wsgi import Application

if __name__=="__main__":
    app = Application("")
    wsgi.server(eventlet.listen(('',8090)),app)

