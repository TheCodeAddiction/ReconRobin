import requests
from helper import data_helper, regex_helper, file_helper, network_helper
from helper.visual_helper import VisualHelper

animation = VisualHelper()


def create_url(domain):
    return "https://crt.sh/?q=" + domain + "&output=json"


def get_all_domains(url):
    request = requests.get(url)
    network_helper.check_for_rate_limit(request.status_code,"crt.sh")
    data = request.json()
    unique_domains = data_helper.remove_duplicates_from_list(regex_helper.grab_common_name_from_crt(data))
    file_helper.write_list_to_file("crt_domains.txt", unique_domains, "writing crt.sh domains to file")
    return unique_domains
