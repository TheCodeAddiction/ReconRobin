import socket
def check_for_rate_limit(status_code, service_name):
    if status_code == 429:
        print("Error 429: You have been rate limited by:", service_name)
        print("Quiting")
        quit(1)

def get_ip_of_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror as e:
        if e.errno == -2:
            # This specific error means the domain could not be resolved.
            # You can print an error message or just pass to ignore it.
            return ""
        else:
            # Handle other socket.gaierror possibilities here.
            return ""