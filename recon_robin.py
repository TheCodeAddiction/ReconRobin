from crt import crt
from VirusTotal import virustotal as vt
from helper import file_helper
def main():
    target_list = input("Give me a list of domains name:\n")
    target_domains = target_list.split(",")
    for domain in target_domains:
        crt_domains = crt.get_all_domains(crt.create_url(domain),domain)
        vt_domains = vt.get_all_subdomains(domain.strip())
        all_domains = [crt_domains, vt_domains]
        file_helper.create_domain_super_list(domain+"super_list",all_domains,"creating super list")



if __name__ == '__main__':
    main()
