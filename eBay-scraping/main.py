import asyncio
from playwright.async_api import async_playwright
import os
from dotenv import load_dotenv
import urllib.parse
import requests
from sqlDatabase import setupSQL, deletePages, setPages, getPages
from googleSheetsDatabase import addRowIntoGoogleSheets
 
def get_page_html(proxy_api, url):
    changed_url = urllib.parse.quote(url)
    proxied_url = f'https://api.scrape.do?token={proxy_api}&url={changed_url}&render=true'
    response = requests.get(proxied_url)
    return response.text

async def scrape_page(page, proxy_api, url, page_num):
    if page_num > 1:
        paged_url = f'{url}&_pgn={page_num}'
    else:
        paged_url = url

    html = get_page_html(proxy_api, paged_url)
    await page.set_content(html, wait_until='domcontentloaded')
    await page.wait_for_timeout(2000)
    return html

async def main():
    await setupSQL()
    load_dotenv()
    url = 'https://www.ebay.com/sch/i.html?_nkw=laptop&_sacat=0&_from=R40&Type=Notebook%252FLaptop&RAM%2520Size=16%2520GB&Screen%2520Size=15%252D15%252E9%2520in&Storage%2520Type=SSD%2520%2528Solid%2520State%2520Drive%2529%7CNVMe%2520%2528Non%252DVolatile%2520Memory%2520Express%2529%7CHDD%2520%252B%2520SSD&_dcat=177'
    proxyApi = os.getenv('PROXY_API')

    pages = await getPages()

    if pages == 1:
        current_page = 1
    else:
        current_page = pages

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36', )
        page = await context.new_page()

        await page.wait_for_timeout(5000)

        while True:
            productsData = []

            await scrape_page(page, proxyApi, url, current_page)

            allProducts = await page.query_selector_all("li.s-card")

            for product in allProducts:
                titleElem = await product.query_selector("div[class='s-card__title']")
                title = await titleElem.inner_text()

                productURLElem = await product.query_selector(".s-card__link")
                productURL = await productURLElem.get_attribute('href')

                productConditionElem = await product.query_selector("div[class='s-card__subtitle']")
                productCondition = await productConditionElem.inner_text() if productConditionElem else None

                costElem = await product.query_selector(
                    "span[class='su-styled-text primary bold large-1 s-card__price']")
                cost = await costElem.inner_text() if costElem else None

                canBuyElem = await product.query_selector(".s-card__attribute-row:nth-child(2) > .su-styled-text")
                canBuy = await canBuyElem.inner_text() if canBuyElem else None

                deliveryCostElem = await product.query_selector(".s-card__attribute-row:nth-child(3) > .su-styled-text")
                deliveryCost = await deliveryCostElem.inner_text() if deliveryCostElem else None

                locationElem = await product.query_selector(".s-card__attribute-row:nth-child(4) > .su-styled-text")
                location = await locationElem.inner_text() if locationElem else None

                soldElem = await product.query_selector("span[class='su-styled-text primary bold large']")
                sold = await soldElem.inner_text() if soldElem else None

                positiveReplyElem = await product.query_selector(
                    '.su-card-container__attributes__secondary > .s-card__attribute-row:nth-child(1)')
                positiveReply = await positiveReplyElem.inner_text() if positiveReplyElem else None

                refurbishElem = await product.query_selector("span[class='su-styled-text default']")
                refurbish = True if refurbishElem else False

                extraElem = await product.query_selector("span[class='su-styled-text negative bold large']")
                extra = await extraElem.inner_text() if extraElem else None

                productData = ['https://www.ebay.com/' + productURL, title, productCondition, cost, canBuy, deliveryCost, location, sold, positiveReply, refurbish, extra]
                print(productData)
                productsData.append(productData)

            nextPageButton = await page.query_selector('a.pagination__next')

            if nextPageButton:
                current_page += 1
                await setPages(current_page)
                await addRowIntoGoogleSheets(productsData)
            else:
                await deletePages()
                break

        await page.wait_for_timeout(5000)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
