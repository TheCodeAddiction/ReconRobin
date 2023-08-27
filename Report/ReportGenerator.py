from Shodan import Shodan_helper
from Shodan.Shodan_helper import get_all_shodan_data_from_domain
from helper import network_helper


def write_to_markdown(filename, content):  # just example
    with open(filename, 'w') as file:
        file.write(content)


def read_subdomains(domain_list):  # just example
    with open(domain_list, 'r') as file:
        contents = file.read()
        print(contents)


def generate_markdown_report(main_domain, new_domains, removed_domains, subdomain_data):
    report = []

    # Add title
    report.append(f"# Report for {main_domain}\n")
    report.append("---\n")
    report.append("## Changes since last report:\n")

    # Add new domains header
    if new_domains:
        report.append('### <span style="color:green">New domains</span>')
        for idx, domain in enumerate(new_domains, 1):
            report.append(f"{idx}. {domain}")
        report.append('\n')

    # Add removed domains header
    if removed_domains:
        report.append('### <span style="color:red">Removed Domains</span>')
        for idx, domain in enumerate(removed_domains, 1):
            report.append(f"{idx}. {domain}")
        report.append('\n')

    # Add subdomain table header
    report.append("## All Subdomains:")
    headers = ["domain name", "ip", "ports", "Services", "Is new", "Is removed", "Old domain"]
    header_line = '| ' + ' | '.join(headers) + ' |'
    separator_line = '| ' + ' | '.join(['-' * len(header) for header in headers]) + ' |'
    report.append(header_line)
    report.append(separator_line)

    # Add subdomain table data
    for row in subdomain_data:  # to add data, just add another field to the subdomain data
        data_line = '| ' + ' | '.join(row) + ' |'
        report.append(data_line)

    write_to_markdown("Output/" + main_domain + "/" + main_domain + "_report.md", '\n'.join(report))
    return '\n'.join(report)


def generate_data_column_of_domain(domain, is_new, is_removed, is_old):
    shodan_data = get_all_shodan_data_from_domain(domain)
    shodan_ports = shodan_data.ports
    shodan_ips = shodan_data.ips
    shodan_services = shodan_data.services
    ips = " ".join(map(str, shodan_ips))
    ports = " ".join(map(str, shodan_ports))
    services = " ".join(map(str, shodan_services))
    # domain_ip = network_helper.get_ip_of_domain(subdomain) # for simplcity we ignore this for now
    # shodan_ips.add(domain_ip)
    if not ips:
        return False
    if not ports:
        ports = "No Ports Found"
    return [domain, ips, ports, services, is_new, is_removed, is_old]
