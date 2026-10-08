import asyncio
from playwright_stealth import Stealth
from playwright.async_api import async_playwright
from csvDatabase import clean_data_and_export_to_csv
from producsData import productsData

async def scrape():
    # Construct target URL based on pagination state
    url = 'https://rozetka.com.ua/ua/notebooks/c80004/obyom-ssd=1-tb-4280776;price=99-25000;producer=acer,asus,dell,hp-hewlett-packard,lenovo;20863=48089/'

    # Launch Playwright browser session with customized User-Agent
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36')
        page = await context.new_page()
        stealth = Stealth()
        await stealth.apply_stealth_async(page)
        await page.goto(url)

        # Wait until network activity settles
        await page.wait_for_load_state('networkidle')

        try:
            while True:
                # Extract product listing cards
                allProducts = await page.query_selector_all('rz-catalog-tile')

                for product in allProducts:
                    # Extract URL, Title, and Price for each product card
                    titleElem = await product.query_selector('a[class="tile-title black-link text-base"]')

                    title = await titleElem.get_attribute('title') if titleElem else None

                    url = await titleElem.get_attribute('href') if titleElem else None

                    costElem = await product.query_selector('div[class="price leading-none font-bold color-red"]')
                    alternativeCostElem = await product.query_selector('div[class="price leading-none font-bold"]')

                    if costElem:
                        cost = await costElem.inner_text()
                    elif alternativeCostElem:
                        cost = await alternativeCostElem.inner_text()
                    else:
                        cost = None

                    print(f'Saved product: {title}, {cost}')
                    productsData['URL'].append(url)
                    productsData['Title'].append(title)
                    productsData['Price'].append(cost)

                # Check for next page pagination button
                nextPageBtn = await page.query_selector('button[data-testid="pagination_to_next_page"]')

                if nextPageBtn:
                    # Navigate to next page, update DB state, and export current page data
                    await nextPageBtn.click()
                    await page.wait_for_load_state('networkidle')
                    await page.wait_for_timeout(3000)
        except NameError:
            print(f'Error: {NameError}')

        finally:
            await clean_data_and_export_to_csv(productsData)
            await page.wait_for_timeout(5000)
            await browser.close()

# Run async entry point
asyncio.run(scrape())