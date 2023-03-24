import argparse
import subprocess

# Set up argument parser
parser = argparse.ArgumentParser(description="Run dig command on a list of domains and subdomains for various DNS record types.")
parser.add_argument("--ip", type=str, help="Specify the IP address of the DNS server to query.")
args = parser.parse_args()

# List of DNS record types to query
dns_record_types = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "SRV", "TXT"]

# Function to run dig command
def run_dig(domain, record_type, ip=None):
    command = ["dig",record_type,domain]
    if ip:
        command.append(f"@{ip}")
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# Read domains and subdomains from file
filename = "domains.txt"  # Replace with your file name
with open(filename, "r") as file:
    domains = file.readlines()

# Remove newline characters and whitespace from domains
domains = [domain.strip() for domain in domains]

# Open output files
with open("soa_records.txt", "w") as soa_file, \
     open("valid_records.txt", "w") as valid_file, \
     open("pretty_output.txt", "w") as pretty_file, \
     open("false_output.txt","w") as false_file:

    # Run dig command for each domain and DNS record type
    for domain in domains:
        for record_type in dns_record_types:
            dig_output = run_dig(domain, record_type, ip=args.ip)

            # Check if the ANSWER count is greater than zero
            answer_count = 0
            for line in dig_output.splitlines():
                if line.startswith(";; flags:"):
                    answer_count = int(line.split("ANSWER:")[1].split(",")[0].strip())
                    break

            if answer_count > 0:
                # Write SOA records to soa_records.txt
                if record_type == "SOA":
                    soa_file.write(dig_output)
                    soa_file.write("\n")
                else:
                    valid_file.write(dig_output)
                    valid_file.write("\n")
            else:
                false_file.write(dig_output)
                false_file.write("\n")

                # Get and write the ANSWER SECTION part to pretty_output.txt
                answer_section = False
                for line in dig_output.splitlines():
                    if line.startswith(";; ANSWER SECTION:"):
                        answer_section = True
                        continue
                    elif line.startswith(";; Query time:"):
                        answer_section = False
                        pretty_file.write("\n")
                        break

                    if answer_section:
                        pretty_file.write(line.strip())
                        pretty_file.write("\n")