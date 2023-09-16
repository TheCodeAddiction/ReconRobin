from itertools import chain

from . import visual_helper
import os

animation = visual_helper


def write_list_to_file(filename, array, message, domain_name):
    os.makedirs("Output/" + domain_name, exist_ok=True)
    file_path = os.path.join("Output/"+domain_name, filename)
    with open(file_path, "w") as f:
        animation.print_information(message)
        for data in array:
            f.write(data + "\n")
        f.close()
def create_domain_super_list(filename, domains, message,domain_name):
    print(message)
    os.makedirs("Output/"+domain_name, exist_ok=True)
    file_path = os.path.join("Output/"+domain_name, filename)
    with open(file_path,"w") as f:
        for domain_list in domains:
            all_domains_no_duplicates = list(set(domain_list)) # removes duplicates
            for domain in all_domains_no_duplicates:
                f.write(domain+ "\n")


def write_report_data_to_file(data):
    # Open a file in write mode
    with open('Output/report_data.raw', 'w') as f:
        # Write the header
        f.write("Domains | IPs | Ports | Services | Is New | Is Removed | Is Old\n")

        # Write each record to the file
        for record in data:
            record = ['None' if not x.strip() else x for x in record] # if the data is empty, it replaces by None for easy parsing later
            line = ' | '.join(record)
            f.write(line + '\n')
