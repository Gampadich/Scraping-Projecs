# A robust web scraping tool built with Python and Playwright to extract vehicle listing data from AutoRia. Designed for high performance and reliability, it can process thousands of records and export them directly to structured Excel spreadsheets.

## Key Features

- **Automated Pagination**: Automatically detects and navigates through hundreds of search result pages.
- **Fast Extraction**: High-speed data gathering (capable of processing 3500+ listings in ~10 minutes).
- **Data Cleaning**: Automatically handles non-breaking spaces (`\xa0`) and strips whitespace for clean data entry.
- **Robust Storage**: Uses `openpyxl` for direct Excel writing with support for existing file appending.
- **Error Handling**: Implements safe execution blocks to ensure data is saved even if a timeout occurs.

## Tech Stack

- **Python 3.10+**: Core logic.
- **Playwright**: Modern browser automation (Chromium).
- **Openpyxl**: Professional Excel file management.

## Installation

1. **Clone the repository:**
   git clone [https://github.com/your-username/auto-ria-scraping.git](https://github.com/your-username/auto-ria-scraping.git)
   cd auto-ria-scraping
Install dependencies:

pip install playwright openpyxl
playwright install chromium
Usage
Update the search URL in main.py and run the script:

python main.py
The scraper will launch a headless browser, iterate through the listings, and generate an autoRia.xlsx file containing:

URL

Model & Generation

Cost ($)

Mileage

Fuel Type & Gearbox

Location & Time

Developed as a professional automation tool for market analysis.
