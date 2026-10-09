import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from dataObject import products
from csvDB import convertToCSV

async def scrape():
    url = 'https://www.amazon.com/s?k=PCs'
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080},
            locale="en-US"
        )
        stealth = Stealth()
        page = await context.new_page()
        stealth.use_async(page)
        await page.goto(url)

        try:
            while True:
                allProducts = await page.query_selector_all('div[data-component-type="s-search-result"]')
                for product in allProducts:
                    titleObject = await product.query_selector(
                        'a[class="a-link-normal s-line-clamp-3 s-link-style a-text-normal"]')
                    productURL = await titleObject.get_attribute('href') if titleObject else None
                    title = await titleObject.inner_text() if titleObject else None
                    optionsObject = await product.query_selector(
                        'span[class="a-size-base a-color-secondary title-differentiators s-line-clamp-1 a-text-normal"]')

                    options = await optionsObject.inner_text() if optionsObject else None

                    rateObject = await product.query_selector('span[class="a-size-small a-color-base"]')

                    rate = await rateObject.inner_text() if rateObject else None

                    if productURL is not None:
                        products['URL'].append('https://www.amazon.com' + productURL)
                        print(f'Saved data: {'https://www.amazon.com' +  productURL}, {title}, {options}, {rate}')
                    else:
                        products['URL'].append(productURL)
                        print(f'Saved data: {productURL}, {title}, {options}, {rate}')

                    products['Title'].append(title)
                    products['Options'].append(options)
                    products['Rate'].append(rate)

                nextBtn = await page.query_selector('a.s-pagination-next')

                await nextBtn.click()
                await page.wait_for_timeout(3000)

        except Exception as e:
            print(e)

        finally:
            convertToCSV(products)
            await page.wait_for_timeout(5000)
            await browser.close()

asyncio.run(scrape())