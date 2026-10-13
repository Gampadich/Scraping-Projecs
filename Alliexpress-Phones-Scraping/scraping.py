from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from data import products, addToData
from exportToCsv import exportToCsv
import asyncio


async def phones_scraping(url):
    """
    Asynchronous function to scrape smartphone listings from AliExpress.
    Handles browser context, stealth mode, pagination via URL parameters,
    data extraction, and CSV export.
    """
    async with async_playwright() as p:
        # Launch Chromium browser in non-headless mode for visibility
        browser = await p.chromium.launch(headless=False)

        # Create a customized browser context to mimic a real user
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080},
            locale="en-US"
        )

        page = await context.new_page()

        # Apply stealth plugin to avoid anti-bot detection
        stealth = Stealth()
        stealth.use_async(page)

        # Navigate to the target search URL
        await page.goto(url)
        await page.wait_for_timeout(2000)

        page_num = 2  # Start pagination from page 2

        try:
            while True:
                # Select all product cards on the current page
                phones = await page.query_selector_all(
                    'div[class="list--gallery--C2f2tvm search-item-card-wrapper-gallery"]')

                for phone in phones:
                    # Extract product URL
                    phone_url_elem = await phone.query_selector(
                        'a[class="us--container--3_xK0hW cards--card--3PJxwBm search-card-item"]')
                    phone_url = await phone_url_elem.get_attribute('href') if phone_url_elem else None

                    # Extract product title
                    title_elem = await phone.query_selector('h3[class="us--titleText--WpU1HVZ"]')
                    title = await title_elem.inner_text() if title_elem else None

                    # Extract product price
                    price_elem = await phone.query_selector('div[class="us--price-sale--8S2hu0e"]')
                    price = await price_elem.inner_text() if price_elem else None

                    # Extract product rating
                    rate_elem = await phone.query_selector('span[class="us--starRating--ebGM4Ii"]')
                    rate = await rate_elem.inner_text() if rate_elem else None

                    # Extract number of sold items
                    sold_elem = await phone.query_selector('span[class="us--trade--1lEAXth"]')
                    sold = await sold_elem.inner_text() if sold_elem else None

                    # Extract delivery info
                    delivery_elem = await phone.query_selector('div[class="us--serviceItem--3c4WJ1p"]')
                    delivery = await delivery_elem.inner_text() if delivery_elem else None

                    # Print extracted item to console
                    print('https:' + phone_url, title, price, rate, sold, delivery)

                    # Store item into data dictionary
                    addToData('https:' + phone_url, title, price, rate, sold, delivery)

                # Wait before navigating to the next page
                await page.wait_for_timeout(1000)

                # Navigate to the next page via URL modification
                await page.goto(
                    f'https://www.aliexpress.us/w/wholesale-mobile-phones-xiaomi.html?page={page_num}&g=y&SearchText=mobile+phones+xiaomi')
                page_num += 1

        except Exception as e:
            print(f"An error occurred during scraping: {e}")

        finally:
            # Export collected data to a CSV file upon completion or error
            exportToCsv(products)
            await page.wait_for_timeout(5000)
            await browser.close()


# Run the asynchronous scraper
asyncio.run(
    phones_scraping('https://www.aliexpress.us/w/wholesale-mobile-phones-xiaomi.html?spm=a2g0o.productlist.search.0'))