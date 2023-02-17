from crt import crt
from helper import file_helper


def main():
    target_domain = input("Give me a domain name:\n")
    crt.get_all_domains(crt.create_url(target_domain))

if __name__ == '__main__':
    main()
