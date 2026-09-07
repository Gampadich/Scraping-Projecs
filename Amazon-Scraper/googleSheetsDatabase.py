import gspread
from google.oauth2.service_account import Credentials

async def addRowIntoGoogleSheets(productsData):
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
    client = gspread.authorize(creds)
    spreadsheetID = '1wGDFqf2_ifAWvZLNwREHD86uj1XkuwRZRLJKxhjZvqs'
    sheet = client.open_by_key(spreadsheetID).sheet1

    sheet.append_rows(productsData)
    print('Successfully added products to Google Sheets')
