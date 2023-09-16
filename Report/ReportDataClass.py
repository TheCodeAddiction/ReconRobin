class ReportDataClass:
    def __init__(self, domain, ips, ports, services, is_new, is_removed, is_old):
        self.domain = domain
        self.ips = ips
        self.ports = ports
        self.services = services
        self.is_new = is_new
        self.is_removed = is_removed
        self.is_old = is_old

    def __repr__(self):
        return f"ReportDataClass(domain={self.domain}, ips={self.ips}, ports={self.ports}, services={self.services}, is_new={self.is_new}, is_removed={self.is_removed}, is_old={self.is_old})"
