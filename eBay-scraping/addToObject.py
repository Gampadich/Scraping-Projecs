from data import products

def add_to_object(url, title, productCondition, cost, canBuy, deliveryCost, location, sold, positiveReply, refurbish, extra):
    """
    Appends extracted product attributes to their respective lists
    inside the centralized products dictionary container.
    """
    products['URL'].append(url)
    products['Title'].append(title)
    products['Product Condition'].append(productCondition)
    products['Cost'].append(cost)
    products['Available'].append(canBuy)
    products['Delivery cost'].append(deliveryCost)
    products['Location'].append(location)
    products['Sold now'].append(sold)
    products['Positive reply`s'].append(positiveReply)
    products['Refurbish'].append(refurbish)
    products['Extras'].append(extra)