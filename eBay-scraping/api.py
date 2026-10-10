import urllib.parse
import requests

def get_page_html(proxy_api, url):
    """
    Encodes the target URL, builds the Scrape.do proxy request URL with rendering enabled,
    and returns the raw HTML response text.
    """
    changed_url = urllib.parse.quote(url)
    proxied_url = f'https://api.scrape.do?token={proxy_api}&url={changed_url}&render=true'
    response = requests.get(proxied_url)
    return response.text