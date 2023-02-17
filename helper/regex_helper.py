import re

def verify_url(url):
    url_regex = re.compile(
        r'^(?:http|https)://'  # http:// or https://
        r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'  # domain name
        r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)$',
        flags=re.IGNORECASE
    )
    if url_regex.search(url):
        return True
    else:
        return False


def grab_common_name_from_crt(data):
    domains = []
    for domain in data:
        regex = r"'common_name': '([^']*)'"
        match = re.search(regex, str(domain))
        if match:
            domains.append(match.group(1))

    return domains
