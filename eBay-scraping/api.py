import urllib.parse
import requests

def get_page_html(proxy_api, url):
    changed_url = urllib.parse.quote(url)
    proxied_url = f'https://api.scrape.do?token={proxy_api}&url={changed_url}&render=true'
    response = requests.get(proxied_url)
    return response.text
