from urchin.service import ProcessLauncher
from urchin.compute.service import Service
from urchin import service


def main():
    launcher = ProcessLauncher()
    launcher.launch_service(Service())
    server = service.WSGIService("compute")
    launcher.launch_service(server, workers=server.workers or 1)
    launcher.wait()

