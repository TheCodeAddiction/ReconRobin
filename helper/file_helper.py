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
        merged = list(chain(*domains)) # merges all array togheter
        merged_no_duplicates = list(dict.fromkeys(merged)) # removes duplicates
        print("I recived all of these domains: ", domains , "of type: ",type(domainss))
        for domain in merged_no_duplicates:
            print("writing,",domain)
            f.write(domain+ "\n")
    return
