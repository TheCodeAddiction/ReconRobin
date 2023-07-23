import subprocess
import re
dns_record_types = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT"]
def run_dig(domain, record_type, ip=None):
    command = ["dig",record_type,domain]
    if ip:
        command.append(f"@{ip}")
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def find_all_domains_dns(domain, ip=None):
    all_records = []
    for record in dns_record_types:
        all_records.append(run_dig(domain,record, ip))
    domains = [re.findall(r'[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text) for text in all_records]
    result_no_dups = [list(set(sublist)) for sublist in domains] # returns an array on uniq arrays with domains in each, ik, kinda stupid but ¯\_(ツ)_/¯
    one_array_no_dups = [] # an array containing every unique result in the same
    for array in result_no_dups:
        for data in array:
            one_array_no_dups.append(data)
    print(one_array_no_dups)
    return one_array_no_dups



