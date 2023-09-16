import os
import re

from Report.ReportDataClass import ReportDataClass
from helper.ReportHistoryHelper import compare_report_data
from helper.data_helper import comma_seperated_string_to_set, service_string_to_set


def is_scan_history_present():
    if os.path.exists("/Output/report_data.raw"):
        return True
    else:
        return False


def compare_new_and_old_scan(scan_result):
    old_data = fetch_all_data_from_previous_report()  # fetch data from old report
    new_data = map_scan_result_to_report_class(scan_result)  # fetch data from the new scan
    for new_results in new_data:
        for old_results in old_data:
            if new_results.domain.strip() == old_results.domain.strip(): # domain exists in both scans, check ports, ips and services for something different
                ip_reports = compare_report_data(comma_seperated_string_to_set(new_results.ips), comma_seperated_string_to_set(old_results.ips))
                port_reports = compare_report_data(comma_seperated_string_to_set(new_results.ports), comma_seperated_string_to_set(old_results.ports))
                service_reports = compare_report_data(service_string_to_set(new_results.services),service_string_to_set(old_results.services))

                new_ips = ip_reports[0]
                old_ips = ip_reports[1]
                same_ips = ip_reports[2]

                new_ports = port_reports[0]
                old_ports = port_reports[1]
                same_ports = port_reports[2]

                new_services = service_reports[0]
                old_services = service_reports[1]
                same_services = service_reports[2]

                print("New ips | New ports | New services:")
                print(*new_ips,*new_ports,*new_services)
# Fetches data from previous scans and maps the data to objects for easy comparison.
def fetch_all_data_from_previous_report():
    with open('Output/report_data.raw', 'r') as file:
        data = file.read()
        print("\n")
        print("data:",data)
        print("\n")

    lines = data.strip().split('\n')
    report_object_array = []
    # Skip the header line
    for line in lines[1:]:
        # Use regular expression to split only on |
        fields = [field.strip() for field in re.split(r'(?<!\\)\|', line)]

        if len(fields) != 7:
            print(f"Error in line: {line}")
            continue

        domain, ips, ports, services, is_new, is_removed, is_old = fields
        report_object = ReportDataClass(domain, ips, ports, services, is_new, is_removed, is_old)
        report_object_array.append(report_object)

    return report_object_array


# maps the data from the live censys/shodan scans into a list of ReportDataClass objects
def map_scan_result_to_report_class(reports):
    return [ReportDataClass(*data) for data in reports]
