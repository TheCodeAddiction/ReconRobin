class ShodanData:
    def __init__(self):
        self.ips = set()
        self.ports = set()
        self.services = set()

    def add_ip(self, ip):
        self.ips.add(ip)

    def add_port(self, port):
        self.ports.add(port)

    def add_service(self, service):
        self.services.add(service)

    def __str__(self):
        return f"IPs: {self.ips}, Ports: {self.ports}, Services: {self.services}"
