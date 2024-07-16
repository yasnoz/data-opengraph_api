# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""
import requests
import pprint

def fetch_metadata(url):
    """
    Returns the "data" dictionary of OpenGraph metadata found in HTML of given url
    """
    base_url = f"https://opengraph.lewagon.com/?url={url}"
    response = requests.get(base_url)
    data = response.json()
    if response.status_code == 200:
        return data['data']
    return {}

# To manually test, please uncomment the following lines and run `python opengraph.py`:
#import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(fetch_metadata("https://www.github.com"))
