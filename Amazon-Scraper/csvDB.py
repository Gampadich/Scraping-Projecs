import pandas

def convertToCSV(products):
    products = pandas.DataFrame(products)
    products.drop_duplicates().fillna(' ')
    products.to_csv('products.csv', index=False, encoding='utf-8-sig')
