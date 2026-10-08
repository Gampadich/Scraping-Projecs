import asyncio
from playwright_stealth import Stealth
from playwright.async_api import async_playwright

from csvDatabase import clean_data_and_export_to_csv
from producsData import productsData


async def scrape():
    """Main function to launch Playwright, scrape Rozetka laptop listings across pages,

    and export clean data to CSV.
    """
    # Target filtered URL: Laptops with 1TB SSD, specific brands, and price range
    url = (
        'https://rozetka.com.ua/ua/notebooks/c80004/'
        'obyom-ssd=1-tb-4280776;price=99-25000;'
        'producer=acer,asus,dell,hp-hewlett-packard,lenovo;20863=48089/'
    )

    # Initialize Playwright browser session
    async with async_playwright() as p:
        # Launch Chromium browser with a custom User-Agent to bypass basic filters
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent=(
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/148.0.0.0 Safari/537.36'
            )
        )
        page = await context.new_page()

        # Apply stealth mode to prevent bot detection
        stealth = Stealth()
        await stealth.apply_stealth_async(page)

        # Navigate to target page and wait for initial network requests to resolve
        await page.goto(url)
        await page.wait_for_load_state('networkidle')

        try:
            while True:
                # Select all product tile containers on the current page
                all_products = await page.query_selector_all('rz-catalog-tile')

                for product in all_products:
                    # Extract title and product URL
                    title_elem = await product.query_selector(
                        'a[class="tile-title black-link text-base"]'
                    )
                    title = (
                        await title_elem.get_attribute('title')
                        if title_elem
                        else None
                    )
                    product_url = (
                        await title_elem.get_attribute('href')
                        if title_elem
                        else None
                    )

                    # Extract price (handling both promotional/red and regular price elements)
                    cost_elem = await product.query_selector(
                        'div[class="price leading-none font-bold color-red"]'
                    )
                    alt_cost_elem = await product.query_selector(
                        'div[class="price leading-none font-bold"]'
                    )

                    if cost_elem:
                        cost = await cost_elem.inner_text()
                    elif alt_cost_elem:
                        cost = await alt_cost_elem.inner_text()
                    else:
                        cost = None

                    print(f'Saved product: {title} | Price: {cost}')

                    # Append scraped details to data structure
                    productsData['URL'].append(product_url)
                    productsData['Title'].append(title)
                    productsData['Price'].append(cost)

                # Locate the pagination button to navigate to the next page
                next_page_btn = await page.query_selector(
                    'button[data-testid="pagination_to_next_page"]'
                )

                if next_page_btn:
                    await next_page_btn.click()
                    await page.wait_for_load_state('networkidle')
                    await page.wait_for_timeout(3000)
                else:
                    # Exit loop if no further pages exist
                    break

        except Exception as err:
            print(f'An error occurred during scraping: {err}')

        finally:
            # Export scraped data regardless of execution status
            await clean_data_and_export_to_csv(productsData)
            await page.wait_for_timeout(5000)
            await browser.close()


if __name__ == '__main__':
    asyncio.run(scrape())