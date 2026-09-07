import asyncio
from xml.sax.handler import all_properties

from playwright.async_api import async_playwright
from sqlDatabase import setupSQL, deletePages, setPages, getPages
from googleSheetsDatabase import addRowIntoGoogleSheets

async def scrape():
    await setupSQL()
    pages = await getPages()
    if pages == 1:
        url = 'https://rozetka.com.ua/ua/notebooks/c80004/obyom-ssd=1-tb-4280776;price=99-25000;producer=acer,asus,dell,hp-hewlett-packard,lenovo;20863=48089/'
    else:
        url = f'https://rozetka.com.ua/ua/notebooks/c80004/obyom-ssd=1-tb-4280776;page={pages};price=99-25000;producer=acer,asus,dell,hp-hewlett-packard,lenovo;20863=48089/'

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36')
        page = await context.new_page()
        await page.goto(url)

        await page.wait_for_load_state('networkidle')

        while True:
            productsData = []
            allProducts = await page.query_selector_all('.item')

            for product in allProducts:
                titleElem = await product.query_selector('.tile-title')

                title = await titleElem.get_attribute('title') if titleElem else None

                url = await titleElem.get_attribute('href') if titleElem else None

                costElem = await product.query_selector('rz-product-tile .price')

                cost = await costElem.inner_text() if costElem else None

                productProperties = [url, title, cost]

                print(productProperties)

                productsData.append(productProperties)

            nextPageBtn = await page.query_selector('a[data-testid="pagination_to_next_page"]')

            if nextPageBtn:
                await nextPageBtn.click()
                await page.wait_for_load_state('networkidle')
                await page.wait_for_timeout(2000)
                pages = await getPages()
                print(pages)
                await setPages(pages + 1)
                await addRowIntoGoogleSheets(productsData)
            else:
                await deletePages()
                break

        await page.wait_for_timeout(5000)
        await browser.close()

asyncio.run(scrape())
