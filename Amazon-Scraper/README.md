# Amazon Web Scraper

An asynchronous Python web scraper built with **Playwright** and **Pandas**, designed to extract product search results from Amazon.

## 🚀 Features

* **Anti-Bot Handling** — Uses `playwright-stealth` and customized browser contexts (User-Agent, viewport, and locale) to reduce bot detection and handle Amazon CAPTCHA pages ("Dogs of Amazon").
* **Asynchronous Execution** — Leverages `asyncio` and `playwright.async_api` for efficient browser automation.
* **Dynamic Data Extraction** — Collects product URLs, titles, specifications, options, and ratings across multiple search result pages.
* **Automatic Pagination** — Navigates through multiple pages of Amazon search results.
* **Data Export** — Processes the collected data using Pandas and exports it to a structured CSV file with UTF-8-SIG encoding.

## 🛠️ Tech Stack

* **Python 3.10+**
* **Playwright** — Browser automation and web scraping
* **playwright-stealth** — Stealth techniques for browser automation
* **Pandas** — Data processing and CSV export
* **asyncio** — Asynchronous execution

## 📦 Requirements

Make sure you have the following installed:

* Python 3.10 or newer
* pip

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Amazon-Scraper.git
cd Amazon-Scraper
```

### 2. Install dependencies

```bash
pip install playwright playwright-stealth pandas
```

### 3. Install Playwright browser binaries

```bash
playwright install chromium
```

## 📁 Project Structure

```text
Amazon-Scraper/
├── main.py          # Main scraping engine
├── dataObject.py    # Dictionary container for product data
├── csvDB.py         # CSV export utility using Pandas
└── products.csv     # Generated dataset (created after execution)
```

### File Description

* **`main.py`** — The main scraping engine. Handles browser contexts, page interactions, element selection, product extraction, and pagination.
* **`dataObject.py`** — Contains the dictionary structure used to store scraped product information.
* **`csvDB.py`** — Processes the collected product data and exports it to a CSV file using Pandas.
* **`products.csv`** — The output file containing the extracted product dataset.

## ▶️ Usage

Run the main scraper script:

```bash
python main.py
```

The scraper will:

1. Launch a Chromium browser.
2. Navigate to Amazon PC search results.
3. Extract product information, including URLs, titles, specifications, options, and ratings.
4. Navigate through subsequent pages of search results.
5. Process the collected data using Pandas.
6. Export the results to `products.csv`.

## 📊 Output

The scraper generates a `products.csv` file containing the extracted product data.

The CSV file uses **UTF-8-SIG encoding**, helping ensure compatibility with spreadsheet applications such as Microsoft Excel.

## ⚠️ Disclaimer

This project is intended for educational and personal use.

* Respect Amazon's [Conditions of Use](https://www.amazon.com/gp/help/customer/display.html?nodeId=GLSBYFE9MGKKQXXM).
* Review the website's applicable policies before scraping.
* Avoid excessive requests that could affect the website's performance.
* CAPTCHA handling and stealth techniques do not guarantee successful access.

## 📄 License

No license has been specified for this project. Add a license file if you intend to distribute or publish the source code.
