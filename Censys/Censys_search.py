import json
from censys.search import CensysHosts

from Censys.CensysDataClass import CensysData


def get_api_id():
    with open("secrets.json", "r") as f:
        data = json.load(f)
        return data["censys_api_id"]


def get_api_secret():
    with open("secrets.json", "r") as f:
        data = json.load(f)
        return data["censys_api_secret"]


censysClient = CensysHosts(api_id=get_api_id(), api_secret=get_api_secret())


def get_all_censys_data_from_domain(domain):
    try:
        all_ips = set()
        all_ports = set()
        all_services = set()
        censys_data = CensysData()
        domain_ips = get_ip_by_domain(domain) # grabs every IP
        for ip in domain_ips:
            all_ips.add(ip)
            results = censysClient.view(ip)
            services = results.get("services","")
            for service in services:
                all_ports.add(service.get("port",""))
                service_name = service.get("service_name","")
                software_list = service.get("software", "")
                for software in software_list[1:]:
                    service = str(service_name)+" "+str(software.get("vendor",""))+" "+str(software.get("product",""))+" "+str(software.get("version",""))
                    all_services.add(service)
            censys_data.ips = all_ips
            censys_data.ports = all_ports
            censys_data.services = all_services
        return censys_data
    except Exception as e:
        print(f"An exception occurred: {e}")

def get_ports_by_domain(domain):
    try:
        ports = set()
        query = censysClient.search("dns.names=" + domain)
        for res in query:
            for data in res:
                services = data["services"]
                for service in services:
                    ports.add(service["port"])
        return ports
    except Exception as e:
        print(f"An exception occurred: {e}")
def get_ip_by_domain(domain):
    try:
        ips = set()
        query = censysClient.search("dns.names=" + domain)
        for res in query:
            for data in res:
                ips.add(data["ip"])
        return ips
    except Exception as e:
        print(f"An exception occurred: {e}")