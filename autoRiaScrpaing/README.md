# 💻 Rozetka Laptop Web Scraper

An asynchronous Python web scraper built with **Playwright** and **Pandas** for extracting laptop listings from **Rozetka**.

The scraper uses browser automation with stealth capabilities, automatically handles pagination, cleans raw price data, removes duplicate listings, and exports the results into a structured CSV file.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Playwright** — asynchronous browser automation
* **playwright-stealth** — helps reduce bot-detection issues
* **Pandas** — data cleaning, transformation, and CSV export

---

## 📂 Project Structure

```text
Rozetka-laptop-scraping/
│
├── main.py              # Main scraping script and Playwright logic
├── csvDatabase.py       # Data cleaning and CSV export
├── producsData.py       # In-memory product data storage
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Rozetka-laptop-scraping.git
cd Rozetka-laptop-scraping
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it depending on your operating system:

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

If `requirements.txt` is already configured:

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install playwright playwright-stealth pandas
```

### 4. Install Playwright browsers

```bash
playwright install chromium
```

---

## 💻 Usage

Run the scraper with:

```bash
python main.py
```

The script will launch Chromium and begin collecting laptop listings from Rozetka.

---

## ⚙️ How It Works

The scraper follows this workflow:

1. **Launches Chromium** using Playwright.
2. **Applies stealth techniques** to reduce bot-detection issues.
3. **Opens Rozetka laptop catalog pages** according to the configured filters.
4. **Extracts product information**, including:

   * Product URL
   * Product title
   * Product price
5. **Navigates through multiple pages** automatically.
6. **Cleans price values** by removing currency symbols, spaces, and other non-numeric characters.
7. **Removes duplicate products** from the collected dataset.
8. **Exports the final dataset** to a CSV file.

---

## 🔎 Supported Filters

The scraper can work with configured Rozetka catalog filters such as:

* **Brand**
* **SSD capacity**
* **Price range**

The exact filters depend on the URLs and selectors configured in `main.py`.

---

## 📊 Output

After the scraping process finishes, the collected data is saved to:

```text
rozetka-laptop-scraped.csv
```

Example:

| URL                                                        | Title                                 | Price |
| ---------------------------------------------------------- | ------------------------------------- | ----: |
| [Rozetka](https://rozetka.com.ua/ua/496860584/p496860584/) | Ноутбук HP Pavilion 15-p258nl / 15.6" | 16446 |
| [Rozetka](https://rozetka.com.ua/ua/609074099/p609074099/) | Lenovo ThinkPad X13 Yoga G1 i7-10510U | 17999 |

---

## 📄 CSV Structure

The generated CSV contains three main columns:

| Column  | Description                     |
| ------- | ------------------------------- |
| `URL`   | Direct link to the product page |
| `Title` | Product name                    |
| `Price` | Cleaned numeric product price   |

---

## ⚠️ Notes

* Make sure **Chromium** is installed through Playwright before running the scraper.
* Website structure and CSS selectors may change over time, which can require updates to the scraper.
* Scraping behavior should comply with **Rozetka's terms of use and applicable policies**.
* Running the scraper in non-headless mode allows you to visually monitor the browser while it is collecting data.

---

## 📜 License

This project is intended for educational and research purposes.
