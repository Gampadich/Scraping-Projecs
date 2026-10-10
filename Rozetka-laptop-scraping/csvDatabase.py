import pandas


async def clean_data_and_export_to_csv(productsData):
    """Converts scraped data dictionary into a Pandas DataFrame,

    strips non-numeric characters from the price column, removes duplicates,
    and exports the result to a clean CSV file.
    """
    df = pandas.DataFrame(productsData)

    if not df.empty:
        # Target the Price column and keep only numeric digits
        price_col = df.columns[-1]
        df[price_col] = df[price_col].astype(str).str.replace(
            r'\D', '', regex=True
        )

    # Remove identical records and fill missing values with empty space
    clean_data = df.drop_duplicates().fillna('')

    # Export dataset to CSV format
    clean_data.to_csv('./rozetka-laptop-scraped.csv', index=False)
    print('Data successfully exported to rozetka-laptop-scraped.csv')