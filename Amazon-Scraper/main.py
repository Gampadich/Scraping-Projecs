import asyncio
from playwright.async_api import async_playwright
from sqlDatabase import setupSQL, deletePages, setPages, getPages
from googleSheetsDatabase import addRowIntoGoogleSheets

async def scrape():
    await setupSQL()
    pages = await getPages()
    if pages == 1:
        url = 'https://www.amazon.com/s?k=PCs'
    else:
        url = f'https://www.amazon.com/s?k=PCs&page={pages}'
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36')
        page = await context.new_page()
        await page.goto(url)

        allProducts = await page.query_selector_all('div[data-component-type="s-search-result"]')

        while True:
            productsData = []

            for product in allProducts:
                titleObject = await product.query_selector(
                    'a[class="a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal"]')
                url = await titleObject.get_attribute('href')
                title = await titleObject.inner_text()
                optionsObject = await product.query_selector(
                    'span[class="a-size-small s-variation-options-text s-variations-options-justify-content"]')

                if optionsObject:
                    options = await optionsObject.inner_text()
                else:
                    options = "Haven`t options yet"

                rateObject = await product.query_selector('span[class="a-size-small a-color-base"]')

                if rateObject:
                    rate = await rateObject.inner_text()
                else:
                    rate = "Haven`t rate yet"

                costObject = await product.query_selector('span[class="a-color-base"]')

                if costObject:
                    cost = await costObject.inner_text()
                else:
                    cost = "Haven`t cost yet"

                productData = ['https://www.amazon.com' + url, title, options, rate, cost]
                print(productData)
                print(productsData)
                productsData.append(productData)
                await page.wait_for_timeout(2000)

            nextBtn = await page.query_selector('a[class="s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator"]')

            if nextBtn:
                await nextBtn.click()
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