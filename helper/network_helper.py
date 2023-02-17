def check_for_rate_limit(status_code, service_name):
    if status_code == 429:
        print("Error 429: You have been rate limited by:", service_name)
        print("Quiting")
        quit(1)
