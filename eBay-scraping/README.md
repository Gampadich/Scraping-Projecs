# eBay Laptop Scraper

An asynchronous Python scraper for collecting laptop listings from eBay using Playwright, Scrape.do proxy rendering, SQLite page tracking, and Google Sheets integration.

The scraper automatically navigates through eBay pagination, extracts laptop product information, stores the current scraping progress in SQLite, and uploads all collected data directly into Google Sheets.

---

# Features

- Async scraping with Playwright
- Dynamic page rendering using Scrape.do
- Automatic pagination support
- SQLite database for saving current page progress
- Google Sheets integration
- Resume scraping from the last saved page
- Extracts detailed product information:
  - Product URL
  - Title
  - Condition
  - Price
  - Buy option
  - Delivery cost
  - Seller location
  - Sold count
  - Seller feedback
  - Refurbished status
  - Additional listing information

---

# Project Structure

```bash
.
├── main.py
├── sqlDatabase.py
├── googleSheetsDatabase.py
├── pages.db
├── credentials.json
├── .env
└── README.md
```

---

# Requirements

Install all required dependencies:

```bash
pip install playwright python-dotenv requests gspread google-auth
```

Install Playwright browser binaries:

```bash
playwright install
```

---

# Environment Variables

Create a `.env` file in the root directory:

```env
PROXY_API=your_scrape_do_token
```

---

# Google Sheets Setup

## 1. Create Google Cloud Service Account

1. Open Google Cloud Console
2. Create a new project
3. Enable:
   - Google Sheets API
   - Google Drive API
4. Create a Service Account
5. Download the service account credentials JSON file

Rename the downloaded file to:

```bash
credentials.json
```

Place it in the project root directory.

---

## 2. Share Your Spreadsheet

Share your Google Spreadsheet with the service account email found inside `credentials.json`.

Example:

```text
my-service-account@project.iam.gserviceaccount.com
```

---

## 3. Update Spreadsheet ID

Inside `googleSheetsDatabase.py` replace:

```python
spreadsheetID = 'YOUR_SPREADSHEET_ID'
```

with your actual Google Spreadsheet ID.

---

# Database

The project uses SQLite (`pages.db`) to store the current pagination state.

This allows the scraper to:

- Resume scraping after interruption
- Continue from the last processed page
- Avoid restarting from page 1

---

# How It Works

## main.py

Main scraper logic.

### Workflow

1. Initialize SQLite database
2. Load environment variables
3. Launch Playwright browser
4. Fetch rendered HTML through Scrape.do
5. Parse eBay product cards
6. Extract product information
7. Upload data to Google Sheets
8. Save current page number in SQLite
9. Continue until no next page exists

---

## sqlDatabase.py

Handles SQLite operations:

- Create database and table
- Save current page number
- Retrieve saved page number
- Delete page data after completion

---

## googleSheetsDatabase.py

Handles Google Sheets integration using the Google Sheets API.

Uploads all scraped products directly into the spreadsheet.

---

# Extracted Product Data

Each product contains:

| Field | Description |
|---|---|
| Product URL | Direct eBay listing URL |
| Title | Product title |
| Condition | Product condition |
| Cost | Product price |
| Buy Option | Auction / Buy It Now |
| Delivery Cost | Shipping price |
| Location | Seller location |
| Sold | Number of sold items |
| Positive Reply | Seller feedback |
| Refurbished | Refurbished status |
| Extra | Additional information |

---

# Running the Scraper

```bash
python main.py
```

---

# Example Output

```python
[
    'https://www.ebay.com/item/123456',
    'Dell Latitude 5520',
    'Used',
    '$299.99',
    'Buy It Now',
    'Free shipping',
    'United States',
    '15 sold',
    '98.7% positive feedback',
    False,
    None
]
```

---

# Technologies Used

- Python
- AsyncIO
- Playwright
- SQLite
- Google Sheets API
- gspread
- Scrape.do

---

# Notes

The scraper uses:

```python
render=true
```

inside Scrape.do requests to properly render dynamic eBay pages.

The browser currently runs in non-headless mode:

```python
browser = await p.chromium.launch(headless=False)
```

To run the scraper in background mode:

```python
browser = await p.chromium.launch(headless=True)
```

---

# Possible Improvements

- Add rotating proxies
- Add retry/error handling
- Save data as CSV or JSON
- Docker support
- Multi-category scraping
- Logging system
- Duplicate filtering
- Async batch Google Sheets uploads

---

# Disclaimer

This project is intended for educational purposes only.

Make sure your scraping activity complies with:

- eBay Terms of Service
- robots.txt policies
- Local laws and regulations

---

# License

MIT License

---

# Author

Built with Python, Playwright, SQLite, and Google Sheets automation.