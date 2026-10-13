# Dictionary structure to hold scraped product fields
products = {
    'URL': [],
    'Title': [],
    'Price': [],
    'Rate': [],
    'Sold': [],
    'Delivery': []
}

def addToData(url, title, price, rate, sold, delivery):
    """
    Appends a new product record into the global products dictionary.
    """
    products['URL'].append(url)
    products['Title'].append(title)
    products['Price'].append(price)
    products['Rate'].append(rate)
    products['Sold'].append(sold)
    products['Delivery'].append(delivery)