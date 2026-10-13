import pandas as pd


def exportToCsv(products):
    """
    Converts the collected product dictionary into a pandas DataFrame,
    cleans up duplicates and empty values, and exports it to a CSV file.
    """
    df = pd.DataFrame(products)

    # Drop duplicates and fill missing values with spaces
    df = df.drop_duplicates().fillna(' ')

    # Save DataFrame to CSV without row indices
    df.to_csv('products.csv', index=False)