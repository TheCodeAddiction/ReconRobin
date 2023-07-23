from itertools import chain

from . import visual_helper
import os

animation = visual_helper


def write_list_to_file(filename, array, message):
    file_path = os.path.join("Output", filename)
    with open(file_path, "w") as f:
        animation.print_information(message)
        for data in array:
            f.write(data + "\n")
        f.close()
def create_domain_super_list(filename, domains, message):
    print(message)
    file_path = os.path.join("Output", filename)
    with open(file_path,"w") as f:
        merged_no_duplicates = list(set(domains)) # removes duplicates
        for domain in merged_no_duplicates:
            f.write(domain+ "\n")
