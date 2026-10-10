import pandas

def export_to_csv(products):
    """
    Converts the products dictionary into a Pandas DataFrame,
    cleans duplicate entries, and exports the dataset to a CSV file.
    """
    products = pandas.DataFrame(products)
    products.drop_duplicates().fillna(' ')
    products.to_csv('products.csv', index=False)