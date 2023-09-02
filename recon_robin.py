from crt import crt
from VirusTotal import virustotal as vt
from helper import file_helper, network_helper
from dns_recon import dns
from Report import ReportGenerator
import argparse
from Censys import Censys_search
from Shodan import Shodan_helper


def main(target_domains):
    for domain in target_domains:
        crt_domains = crt.get_all_domains(crt.create_url(domain), domain)
        vt_domains = vt.get_all_subdomains(domain.strip())
        dns_domains = dns.find_all_domains_dns(domain.strip())
        all_domains = [crt_domains, vt_domains, dns_domains]  # all subdomains it could find.
        all_domains_no_dns = [crt_domains, vt_domains]
        file_helper.create_domain_super_list(domain + "_all_domains_including_DNS", all_domains,
                                             "== creating super list ==", domain)
        file_helper.create_domain_super_list(domain + "_all_domains_no_dns", all_domains_no_dns,
                                             "== creating super list no DNS ==", domain)

        # Report creation section
        reports = []
        is_new = "0"  # dummy data
        is_removed = "0"  # dummy data
        is_old = "1"  # dummy data

        flat_array_all_domains = set()  # a list of every domain in a set
        for array in all_domains:
            for item in array:
                flat_array_all_domains.add(item)

        amount_of_domains = len(flat_array_all_domains)
        for subdomain in flat_array_all_domains:  # creates a data column for each domain that we know of
            print("Amount of requests left: ", str(amount_of_domains) + "/" + str(len(flat_array_all_domains)))
            amount_of_domains = amount_of_domains - 1
            data = ReportGenerator.generate_data_column_of_domain(subdomain, is_new, is_removed, is_old)
            if not data:  # we cant find an ip for the target
                print("Skipping", subdomain, "no IP found - host is not online")
                pass
            else:
                reports.append(data)

        ReportGenerator.generate_markdown_report(domain, ["to be added"], ["to be added"], reports)


def dns_recon_only(domains, ip=None):
    for domain in domains:
        dns_domains = dns.find_all_domains_dns(domain, ip)
        file_helper.create_domain_super_list(domain + "_all_DNS_results", dns_domains,
                                             "== Writing DNS results to file ==", domain)


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
