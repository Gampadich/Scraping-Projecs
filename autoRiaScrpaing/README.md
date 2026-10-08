# 🚗 Auto.ria Vehicle Web Scraper

An object-oriented Python web scraper built with **Playwright** and **Pandas** for extracting used vehicle listings from the **Auto.ria** marketplace.

The scraper navigates through search results, handles dynamic pagination using the **"Show More"** button, extracts key vehicle specifications, cleans the collected data, removes duplicates, and exports the final dataset to an Excel (`.xlsx`) file.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **Playwright** — synchronous browser automation and dynamic page interaction
* **Pandas** — data processing, cleaning, duplicate removal, and dataset management
* **OpenPyXL** — Excel (`.xlsx`) file generation

---

## ✨ Features

* **Object-Oriented Architecture**
  The scraper is encapsulated in a reusable `Scraper` class, making it easy to customize and extend.

* **Dynamic Pagination**
  Automatically detects and clicks the **"Show More"** button to load additional vehicle listings.

* **Robust Data Extraction**
  Safely handles listings with missing or incomplete information without causing `IndexError` exceptions.

* **Data Sanitization**
  Cleans whitespace, non-breaking spaces (`\xa0`), and other formatting inconsistencies.

* **Duplicate Removal**
  Automatically removes duplicate vehicle listings from the resulting dataset.

* **Missing Data Handling**
  Handles unavailable attributes and fills missing values where necessary.

* **Excel Export**
  Saves the collected vehicle data directly into a structured `.xlsx` spreadsheet.

---

## 📊 Extracted Data

The scraper collects the following information from each vehicle listing:

| Attribute           | Description                          |
| ------------------- | ------------------------------------ |
| `URL`               | Direct link to the vehicle listing   |
| `Model`             | Vehicle brand and model              |
| `Generation`        | Model generation or year information |
| `Cost`              | Vehicle price                        |
| `Mileage`           | Recorded vehicle mileage             |
| `Gearbox`           | Transmission type                    |
| `Fuel Type`         | Engine/fuel type                     |
| `Location`          | Seller's city or region              |
| `Short Description` | Short seller description             |
| `Time`              | Listing creation or update timestamp |

---

## 📂 Project Structure

```text
AutoRia-Vehicle-Scraper/
│
├── main.py              # Main scraper and Scraper class
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AutoRia-Vehicle-Scraper.git
cd AutoRia-Vehicle-Scraper
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Alternatively, install the dependencies manually:

```bash
pip install playwright pandas openpyxl
```

### 4. Install Playwright Chromium

```bash
playwright install chromium
```

---

## 💻 Usage

Run the main scraper:

```bash
python main.py
```

The scraper will open Chromium, navigate to the configured Auto.ria search page, collect vehicle listings, and save the results to an Excel file.

---

## ⚙️ Customizing the Scraper

The `Scraper` class accepts a target search URL and an output filename.

You can use it to scrape different vehicle categories, regions, brands, or price ranges available on Auto.ria.

### Example

```python
from main import Scraper

scraper = Scraper(
    url="YOUR_TARGET_AUTO_RIA_SEARCH_URL",
    filename="my_custom_cars.xlsx"
)

scraper.scrape()
```

### Parameters

| Parameter  | Description                   |
| ---------- | ----------------------------- |
| `url`      | Auto.ria search results URL   |
| `filename` | Name of the output Excel file |

---

## 🔄 Scraping Workflow

The scraper follows the following process:

```text
Start
  │
  ▼
Open Auto.ria
  │
  ▼
Load search results
  │
  ▼
Extract vehicle listings
  │
  ▼
Parse vehicle attributes
  │
  ▼
Click "Show More"
  │
  ▼
More listings available?
  │
  ├── Yes ──► Continue scraping
  │
  └── No
        │
        ▼
Clean collected data
        │
        ▼
Remove duplicates
        │
        ▼
Export to XLSX
        │
        ▼
       Done
```

---

## 📄 Output

After the scraping process is completed, the collected data is exported to an Excel file.

For example:

```text
my_custom_cars.xlsx
```

The resulting spreadsheet contains structured records such as:

| Model         | Generation         |     Cost |    Mileage | Gearbox   | Fuel Type | Location |
| ------------- | ------------------ | -------: | ---------: | --------- | --------- | -------- |
| Example Car   | Example Generation | 15,000 $ | 120,000 km | Automatic | Diesel    | Kyiv     |
| Example Car 2 | Example Generation | 18,500 $ |  95,000 km | Manual    | Petrol    | Lviv     |

---

## ⚠️ Notes

* Make sure **Chromium** is installed through Playwright before running the scraper.
* Auto.ria may change its HTML structure or CSS selectors, which can require updates to the scraper.
* Some listings may contain incomplete information. The scraper is designed to handle missing fields safely.
* Scraping should comply with **Auto.ria's terms of use** and applicable website policies.
* Large scraping tasks may take some time because listings are loaded dynamically.

---

## 📜 License

This project is intended for **educational and research purposes**.
