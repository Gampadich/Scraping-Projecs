import pandas

async def clean_data_and_export_to_csv(productsData):
    """Converts scraped data to DataFrame, cleans duplicates/nulls, and exports to CSV."""
    df = pandas.DataFrame(productsData)
    clean_data = df.drop_duplicates().fillna(' ')
    clean_data.to_csv('./rozetka-laptop-scraped.csv', index=False)