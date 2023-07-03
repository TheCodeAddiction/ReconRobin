from crt import crt
from VirusTotal import virustotal as vt
from helper import file_helper
from dns_recon import dns
def main():
    target_list = input("Give me a list of domains name:\n")
    target_domains = target_list.split(",")
    for domain in target_domains:
        crt_domains = crt.get_all_domains(crt.create_url(domain),domain)
        vt_domains = vt.get_all_subdomains(domain.strip())
        dns_domains = dns.find_all_domains_dns(domain.strip())
        all_domains = [crt_domains, vt_domains,dns_domains]
        all_domains_no_dns = [crt_domains, vt_domains]
        file_helper.create_domain_super_list(domain+"_all_domains_including_DNS",all_domains,"== creating super list ==")
        file_helper.create_domain_super_list(domain+"_all_domains_no_dns",all_domains_no_dns,"== creating super list no DNS ==")



if __name__ == '__main__':
    main()
