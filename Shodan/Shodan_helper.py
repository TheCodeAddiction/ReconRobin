import json
import shodan

def get_api_key():
    with open("secrets.json", "r") as f:
        data = json.load(f)
        return data["shodan_api_key"]


SHODAN_API_KEY = get_api_key()

api = shodan.Shodan(SHODAN_API_KEY)

def shodan_get_all_ports_from_ip(ip):
    try:
        return api.host(ip)['ports']
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
                if hostname.strip() == domain.strip() or hostname.strip() == "www."+domain.strip():
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
