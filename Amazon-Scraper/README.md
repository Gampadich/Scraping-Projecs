# Amazon PC Market Scraper

A high-performance, asynchronous Python tool designed for automated data extraction from Amazon. The project is optimized for monitoring the computer market, ensuring reliable data delivery directly to cloud storage.

---

## Key Functionalities

### State Persistence & Session Management

The scraper implements a robust state management system using SQLite. It tracks the scraping progress by storing the current page index in a local database (`pages.db`). This allows the script to:

- Resume from the exact page after an interruption.
- Ensure no data is lost during long-running sessions.
- Automatically reset progress once the full search result is processed.

### Cloud Integration (Google Sheets API)

Unlike standard scrapers that save files locally, this tool features real-time cloud synchronization:

- **Batch Data Transmission:** To stay within Google API quotas (300 requests/min), the tool collects an entire page of data and uploads it in a single batch.
- **Service Account Authentication:** Secure connection using Google Cloud service accounts for seamless background operation.

### Reliable Data Extraction

- **Dynamic Content Handling:** Powered by Playwright to handle Amazon's complex JavaScript-rendered search results.
- **Data Sanitization:** Automatically cleans and structures product titles, variation options (`options`), star ratings, and price strings.
- **Anti-Bot Mitigation:** Implements custom User-Agents and human-like delays (`wait_for_timeout`) to maintain a low profile.

---

## Technical Architecture

The project follows a modular functional approach, separating concerns into specialized modules:

| Module | Responsibility |
|---|---|
| `main.py` | Orchestrates the browser automation and scraping flow |
| `sqlDatabase.py` | Handles all low-level database operations for state persistence |
| `googleSheetsDatabase.py` | Manages the API connection and batch writing logic |

## Tech Stack

- **Python 3.12+**
- **Playwright (Chromium)** — Asynchronous browser automation.
- **gspread & google-auth** — Google Sheets API integration.
- **SQLite3** — Local state management.
- **Asyncio** — High-concurrency execution.

---

## Installation and Setup

**1. Install required packages:**

```bash
pip install playwright gspread google-auth
```

**2. Install browser binaries:**

```bash
playwright install chromium
```

**3. API Configuration:**

- Place your Google Service Account `credentials.json` in the root folder.
- Share your target Google Sheet with the service account's email.

**4. Run the script:**

```bash
python main.py
```

---

## Usage Notes

The scraper initializes by verifying the local SQLite state. If a previous session exists, it navigates directly to the last saved page. Data is committed to Google Sheets only after a full page is successfully parsed, ensuring data integrity. Once the final page is reached, the local session is cleared automatically.

---

*Developed for real-time e-commerce analytics and price monitoring.*