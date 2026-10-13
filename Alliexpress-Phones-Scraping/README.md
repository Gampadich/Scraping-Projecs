# AliExpress Asynchronous Phone Scraper

An asynchronous web scraper built with **Python**, **Playwright**, and **Pandas** to collect smartphone listings from AliExpress search results. The project supports browser automation, pagination, structured data processing, and CSV export.

## 🚀 Features

- **Asynchronous Execution:** Uses Python's `asyncio` and Playwright's asynchronous API for efficient browser automation.
- **Stealth Integration:** Uses `playwright-stealth` and custom browser settings to help reduce automated browsing detection.
- **Automatic Pagination:** Navigates through multiple search result pages by adjusting URL parameters.
- **Data Processing:** Organizes scraped product information into a structured dataset using Pandas.
- **CSV Export:** Saves collected product data to a `products.csv` file.
- **Browser Automation:** Uses Playwright to interact with dynamically loaded search results.

## 🛠️ Tech Stack

- **Python 3.10+** — Programming language.
- **Playwright** — Browser automation and page interaction.
- **Playwright-Stealth** — Browser stealth functionality.
- **Pandas** — Data processing and CSV export.
- **Asyncio** — Asynchronous execution.

## 📂 Project Structure

```text
Aliexpress-Phones-Scraping/
│
├── scraping.py       # Main scraping script
├── data.py           # Product data storage and insertion functions
├── exportToCsv.py    # CSV export utility using Pandas
├── requirements.txt  # Project dependencies
└── products.csv      # Generated dataset
```

## ⚙️ Installation

### 1. Clone the repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/Aliexpress-Phones-Scraping.git
cd Aliexpress-Phones-Scraping
```

### 2. Install dependencies

Make sure Python 3.10 or newer is installed.

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers

```bash
playwright install
```

## ▶️ Usage

Run the main scraping script:

```bash
python scraping.py
```

The script launches a browser, collects smartphone listings from multiple search result pages, and processes the retrieved data.

Depending on the implementation, the browser may run in visible mode (`headless=False`). The collected product data is exported to `products.csv` using Pandas.

## 📊 Output

The scraper generates a CSV file named `products.csv`, which can be opened with:

- Microsoft Excel
- Google Sheets
- LibreOffice Calc
- Python and Pandas

The file can be used for further data analysis, filtering, and product comparisons.

## ⚠️ Notes

- The actual output depends on the available search results and the website's current page structure.
- AliExpress may change its HTML structure or introduce access restrictions, which can require updates to the scraper.
- Use reasonable request rates and respect the website's terms of service.

## 📄 License

No license has been specified for this project yet.
