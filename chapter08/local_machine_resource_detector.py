import socket
from opentelemetry.sdk.resources import Resource, ResourceDetector

class LocalMachineResourceDetector(ResourceDetector):
    def detect(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return Resource.create(
            {
                "net.host.name": hostname,
                "net.host.ip": ip_address,
            }
        )
