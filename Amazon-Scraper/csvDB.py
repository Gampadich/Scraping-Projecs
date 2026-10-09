import pandas


def convertToCSV(products):
    # Convert global dictionary into a Pandas DataFrame
    products = pandas.DataFrame(products)

    # Remove duplicate rows and fill missing values
    products.drop_duplicates().fillna(' ')

    # Export DataFrame to CSV file with UTF-8 BOM encoding for proper character rendering in Excel
    products.to_csv('products.csv', index=False, encoding='utf-8-sig')