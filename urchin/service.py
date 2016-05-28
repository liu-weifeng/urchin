from urchin import wsgi
import eventlet
import eventlet.wsgi

def main():
    app = wsgi.Application()
    eventlet.wsgi.server(eventlet.listen(('', 8090)), app)


# test wsgi
if __name__ == "__main__":
    main()

