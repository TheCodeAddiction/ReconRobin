import json
import shodan

def get_api_key():
    with open("secrets.json", "r") as f:
        data = json.load(f)
        return data["shodan_api_key"]


SHODAN_API_KEY = get_api_key()

api = shodan.Shodan(SHODAN_API_KEY)

def testSearch():
    # Wrap the request in a try/ except block to catch errors
    try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
    except shodan.APIError as e:
        print('Error: {}'.format(e))