import requests
from helper import data_helper, regex_helper
from helper.visual_helper import VisualHelper

animation = VisualHelper()


def create_url(domain):
    return "https://crt.sh/?q="+domain+"&output=json"


def get_all_domains(url):
    animation.start_loading()
    data = requests.get(url).json()
    unique_domains = data_helper.remove_duplicates_from_list(regex_helper.grab_common_name_from_crt(data))
    print(unique_domains)
    animation.stop_loading()
    return unique_domains


