def create_url(domain_list):
    url_list = []
    for domain in domain_list:
        url_list.append("https://www.virustotal.com/gui/domain/"+domain+"/relations")
    print(url_list)

urls = ["shein.com"]
create_url(urls)