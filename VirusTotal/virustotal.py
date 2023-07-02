import requests
import json
from helper import file_helper


def create_url(domain):
    return "https://www.virustotal.com/api/v3/domains/" + domain + "/subdomains?limit=1000"


def get_api_key():
    with open("secrets.json", "r") as f:
        data = json.load(f)
        return data["virus_total_api_key"]


def get_all_subdomains(domain):
    results = []
    url = create_url(domain)
    vt_api_key = get_api_key()
    headers = {
        "accept": "application/json",
        "x-apikey": vt_api_key
    }
    response = requests.get(url, headers=headers).json()
    data = response["data"]
    for item in data:
        results.append(item["id"])
    results_no_dup = list(dict.fromkeys(results))
    file_helper.write_list_to_file(domain+"_virustotal_subdomains.txt", results_no_dup, "writing virustotal subdomains to file")
    return results_no_dup

