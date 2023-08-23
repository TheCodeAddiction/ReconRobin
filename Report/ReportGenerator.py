def write_to_markdown(filename, content): # just example
    with open(filename, 'w') as file:
        file.write(content)
def read_subdomains(domain_list): # just example
    with open(domain_list, 'r') as file:
        contents = file.read()
        print(contents)
def generate_markdown_report(main_domain, new_domains, removed_domains, subdomain_data):
    report = []

    # Add title
    report.append(f"# Report for {main_domain}\n")
    report.append("---\n")
    report.append("## Changes since last report:\n")

    # Add new domains header
    if new_domains:
        report.append('### <span style="color:green">New domains</span>')
        for idx, domain in enumerate(new_domains, 1):
            report.append(f"{idx}. {domain}")
        report.append('\n')

    # Add removed domains header
    if removed_domains:
        report.append('### <span style="color:red">Removed Domains</span>')
        for idx, domain in enumerate(removed_domains, 1):
            report.append(f"{idx}. {domain}")
        report.append('\n')

    # Add subdomain table header
    report.append("## All Subdomains:")
    headers = ["domain name", "ip", "ports", "Is new", "Is removed", "Old domain"]
    header_line = '| ' + ' | '.join(headers) + ' |'
    separator_line = '| ' + ' | '.join(['-'*len(header) for header in headers]) + ' |'
    report.append(header_line)
    report.append(separator_line)

    # Add subdomain table data
    for row in subdomain_data:
        data_line = '| ' + ' | '.join(row) + ' |'
        report.append(data_line)

    write_to_markdown("report.md", '\n'.join(report))
    return '\n'.join(report)


# Example usage
main_domain = "pst.no"
new_domains = ["vpn.pst.no"]
removed_domains = ["api.pst.no"]
subdomain_data = [
    ["vpn.pst.no", "68.12.1.2", "22, 3389, 21", "1", "0", "0"],
    ["api.pst.no", "192.168.1.1", "80, 443", "0", "1", "0"],
    ["pst.no", "10.0.0.1", "25, 80, 443, 8080", "0", "0", "1"]
]



