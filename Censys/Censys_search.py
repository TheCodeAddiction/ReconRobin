import json
from censys.search import CensysHosts


def get_api_id():
    with open("secrets.json", "r") as f:
        data = json.load(f)
        return data["censys_api_id"]

def get_api_secret():
    with open("secrets.json", "r") as f:
        data = json.load(f)
        return data["censys_api_secret"]



h = CensysHosts(api_id=get_api_id(),api_secret=get_api_secret())
def search(domain):
    # Single page of search results
    # should do a search: dns.names=chat.csam.politiet.no
    query = h.search("dns.names=chat.csam.politiet.no", per_page=5)
    for result in query:
        print(result)
        print("\n\n")
    #print(query())



