import requests
import data

def scrape_by_api(url):
    data = requests.get(url='https://catalog-api.rozetka.com.ua/v3/goods/getFront', headers=headers)

    formated_data = data.json()

    print(formated_data)
