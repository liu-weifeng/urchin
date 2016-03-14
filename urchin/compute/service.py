import eventlet
import eventlet.wsgi
import wsgi


eventlet.wsgi.server(eventlet.listen(('', 8090)), wsgi.Resource())
