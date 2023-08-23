from crt import crt
from VirusTotal import virustotal as vt
from helper import file_helper, network_helper
from dns_recon import dns
from Report import ReportGenerator
import argparse
from Shodan import Shodan_helper

def main(target_domains):
    for domain in target_domains:
        crt_domains = crt.get_all_domains(crt.create_url(domain),domain)
        vt_domains = vt.get_all_subdomains(domain.strip())
        dns_domains = dns.find_all_domains_dns(domain.strip())
        all_domains = [crt_domains, vt_domains,dns_domains]
        all_domains_no_dns = [crt_domains, vt_domains]
        file_helper.create_domain_super_list(domain+"_all_domains_including_DNS",all_domains,"== creating super list ==",domain)
        file_helper.create_domain_super_list(domain+"_all_domains_no_dns",all_domains_no_dns,"== creating super list no DNS ==",domain)

        # Report creation section
        reports = []
        ports = "22,21,443,80" # dummy data
        is_new = "0" # dummy data
        is_removed = "0" # dummy data
        is_old = "1" # dummy data

        flat_array_all_domains = [] # a list of every domain in one array instead of many small arrays.
        for array in all_domains:
            for item in array:
                flat_array_all_domains.append(item)

        unique_flat_array_all_domains = list(set(flat_array_all_domains))
        for subdomain in unique_flat_array_all_domains:
            domain_ip = network_helper.get_ip_of_domain(subdomain)
            report_overview_data = [subdomain, domain_ip, ports, is_new, is_removed, is_old]
            reports.append(report_overview_data)

        ReportGenerator.generate_markdown_report(domain,["to be added"],["to be added"],reports)



def dns_recon_only(target_domains, ip=None):
    for domain in target_domains:
        dns_domains = dns.find_all_domains_dns(domain,ip)
        file_helper.create_domain_super_list(domain + "_all_DNS_results", dns_domains, "== Writing DNS results to file ==",domain)


if __name__ == '__main__':
    target_list = input("Give me a list of domains name:\n")
    target_domains = target_list.split(",")

    parser = argparse.ArgumentParser()

    parser.add_argument('--ip', type=str, help='IP address of a spesific DNS server')
    parser.add_argument('--dns-only', action='store_true', help='Will only do DNS recon.')
    args = parser.parse_args()
    dns_server_ip = args.ip

    if args.dns_only:
        dns_recon_only(target_domains, dns_server_ip)

    else:
        main(target_domains)