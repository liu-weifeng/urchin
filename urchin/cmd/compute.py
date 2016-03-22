from urchin.utils import launcher
from urchin.compute import service


def main():
    # launcher = ProcessLauncher()
    # launcher.launch_service(Service())
    # server = service.WSGIService("compute")
    # launcher.launch_service(server, workers=server.workers or 1)
    # launcher.wait()
    _launcher = launcher.ProcessLauncher()
    _service = service.Service()
    _launcher.launch_service(_service)
    _launcher.wait()


# test

if __name__ == "__main__":
    
    main()
