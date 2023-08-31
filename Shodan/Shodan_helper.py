import json
import shodan

from Shodan.ShodanDataClass import ShodanData


def get_api_key():
    with open("secrets.json", "r") as f:
        data = json.load(f)
        return data["shodan_api_key"]


SHODAN_API_KEY = get_api_key()

api = shodan.Shodan(SHODAN_API_KEY)

def get_all_shodan_data_from_domain(domain):
    all_ips = set()
    all_ports = set()
    all_services = set()
    try:
        results = api.search('hostname:{}'.format(domain))
        for result in results['matches']:
            hostnames = result['hostnames']
            ip = result['ip_str']
            ports = shodan_get_all_ports_from_ip(ip) # we need to see if we can find a way to not make this call as it heavly slows down the program.
            for hostname in hostnames:
                if hostname.strip() == domain.strip():
                    all_ips.add(ip)
                    product = result.get('product', '')
                    version = result.get('version', '')
                    all_services.add(f"{product} {version}")
                    for port in ports:
                        all_ports.add(port)

        shodan_data = ShodanData()
        shodan_data.ips = all_ips
        shodan_data.ports = all_ports
        shodan_data.services = all_services
        return shodan_data
    except shodan.APIError as e:
        print('Error: {}'.format(e))

def shodan_get_all_ports_from_ip(ip):
    try:
        host_info = api.host(ip)
        with open("API.HOST.json", "w") as f:
            json.dump(host_info, f, indent=4)
        return host_info['ports']
    except shodan.APIError as e:
        print('Error: {}'.format(e))


def get_ips_for_specific_domain(domain):
    all_ips = set()
    try:
        results = api.search('hostname:{}'.format(domain))
        for result in results['matches']:
            hostnames = result['hostnames']
            ip = result['ip_str']
            for hostname in hostnames:
                if hostname.strip() == domain.strip():
                    all_ips.add(ip)
        return all_ips
    except shodan.APIError as e:
        print('Error: {}'.format(e))

def get_ports_for_specific_domain(domain):
    all_ports = set()
    try:
        results = api.search('hostname:{}'.format(domain))
        for result in results['matches']:
            hostnames = result['hostnames']
            ip = result['ip_str']
            ports = shodan_get_all_ports_from_ip(ip)
            for hostname in hostnames:
                if hostname.strip() == domain.strip():
                    for port in ports:
                        all_ports.add(port)
        return all_ports
    except shodan.APIError as e:
        print('Error: {}'.format(e))


def get_services_for_specific_domain(domain):
    all_services = set()
    try:
        results = api.search('hostname:{}'.format(domain))
        for result in results['matches']:
            hostnames = result.get('hostnames', [])
            if domain in hostnames or "www."+domain in hostnames:
                product = result.get('product', 'Unknown')
                version = result.get('version', 'Unknown')
                all_services.add(f"{product} {version}")
        print(all_services)
        return all_services

    except shodan.APIError as e:
        print('Error: {}'.format(e))
