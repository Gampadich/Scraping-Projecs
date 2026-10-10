# eBay Web Scraper

A Python-based web scraper built with **Playwright, Requests, and Pandas** to collect laptop product listings, specifications, pricing, and seller information from eBay search results.

## Features

- **Proxy Integration** — Uses the `scrape.do` API proxy service to retrieve target pages and handle website access restrictions.
- **Environment Configuration** — Securely stores API tokens in a local `.env` file using `python-dotenv`.
- **Comprehensive Data Extraction** — Collects product titles, conditions, prices, availability, shipping costs, seller locations, sales volume, ratings, refurbished status, and product tags.
- **Data Processing** — Uses Pandas to process collected information and remove duplicate records.
- **CSV Export** — Saves structured product data to a local `products.csv` file.

## Tech Stack

- **Python 3.10+**
- **Playwright** — Browser automation and page interaction.
- **Requests** — HTTP requests and communication with the proxy API.
- **Pandas** — Data processing, cleaning, and CSV export.
- **python-dotenv** — Environment variable management.
- **scrape.do** — Proxy and page-rendering service.

## Requirements

- Python 3.10 or newer
- A `scrape.do` API token
- An internet connection

## Installation & Setup

### 1. Clone the Repository

Clone the repository and navigate to the project directory.

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install playwright requests pandas python-dotenv
```

### 3. Install Playwright Browser

Install Chromium for Playwright:

```bash
playwright install chromium
```

## Environment Variables

Create a `.env` file in the root directory of the project and add your `scrape.do` API token:

```env
PROXY_API=your_scrape_do_token_here
```

Replace `your_scrape_do_token_here` with your actual API token.

**Important:** Never commit your `.env` file or expose your API token in a public repository. Add `.env` to your `.gitignore` file.

## Project Structure

```text
eBay-Web-Scraper/
├── main.py
├── api.py
├── addToObject.py
├── data.py
├── csvDB.py
├── .env
├── .gitignore
└── products.csv
```

### File Descriptions

| File | Description |
|---|---|
| `main.py` | Main controller responsible for browser initialization, page navigation, product parsing, and pagination. |
| `api.py` | Retrieves page HTML through the `scrape.do` proxy service. |
| `addToObject.py` | Helper module that adds extracted product attributes to the data storage structure. |
| `data.py` | Contains the data structure used to store collected product information. |
| `csvDB.py` | Processes collected data using Pandas and exports the results to a CSV file. |
| `.env` | Stores environment variables, including the proxy API token. |
| `products.csv` | Output file containing the scraped product listings. |

## Usage

Run the main scraper script from the project directory:

```bash
python main.py
```

The scraper will retrieve product listings, extract the configured attributes, process the collected data, and save the results to `products.csv`.

## Output Data

Depending on the available information on eBay, the exported dataset may contain:

- Product title
- Product condition
- Price
- Availability
- Shipping cost
- Seller location
- Sales volume
- Seller or product ratings
- Refurbished status
- Product tags

The exact fields depend on the extraction logic implemented in the project.

## Notes

- Website layouts and page structures may change, requiring updates to the scraping logic.
- API usage may be subject to `scrape.do` plan limits and pricing.
- Respect eBay's applicable terms, robots.txt directives, and rate limits.
- Keep API credentials private and use environment variables for sensitive configuration.

## License

See the `LICENSE` file for licensing information.
