import pandas

def export_to_csv(products):
    products = pandas.DataFrame(products)
    products.drop_duplicates().fillna(' ')
    products.to_csv('products.csv', index=False)
