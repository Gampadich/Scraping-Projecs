from playwright.sync_api import sync_playwright
import pandas

class Scraper:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.df = None
        self.carUrl = None
        self.model = None
        self.generation = None
        self.cost = None
        self.mileage = None
        self.fuelType = None
        self.gearbox = None
        self.location = None
        self.shortDescription = None
        self.time = None
        self.data = {
            'URL': [],
            'Model': [],
            'Generation': [],
            'Cost': [],
            'Mileage': [],
            'Fuel Type': [],
            'Gearbox': [],
            'Location': [],
            'Short Description': [],
            'Time': []
        }

    def clear_and_create_xlsx_table(self):
        self.df = pandas.DataFrame(self.data)
        clear_data = self.df.drop_duplicates().fillna(' ')
        clear_data.to_excel(f'./{self.filename}', index=False)

    def add_to_data(self):
        self.data['URL'].append(self.carUrl)
        self.data['Model'].append(self.model)
        self.data['Generation'].append(self.generation)
        self.data['Cost'].append(self.cost)
        self.data['Mileage'].append(self.mileage)
        self.data['Fuel Type'].append(self.fuelType)
        self.data['Gearbox'].append(self.gearbox)
        self.data['Location'].append(self.location)
        self.data['Short Description'].append(self.shortDescription)
        self.data['Time'].append(self.time)

    def scrape(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.url)
            page.wait_for_timeout(1000)

            try:
                while True:
                    cars = page.query_selector_all(".link.product-card.horizontal")
                    for car in cars:
                        self.carUrl = "https://auto.ria.com" + car.get_attribute("href")
                        self.model = car.query_selector(".common-text.size-16-20.titleS.fw-bold.mb-4").inner_text()
                        generationEl = car.query_selector(".common-text.size-14-16.ellipsis-1.mb-8")
                        self.generation = generationEl.inner_text() if generationEl else None
                        self.cost = car.query_selector(".common-text.titleM.c-green").inner_text().replace('\xa0', ' ').strip()
                        elements = car.query_selector_all(".common-text.ellipsis-1.body")
                        self.mileage = elements[0].inner_text()
                        self.fuelType = elements[1].inner_text()
                        self.gearbox = elements[2].inner_text()
                        self.location = elements[3].inner_text()
                        shortDescriptionEl = car.query_selector(".common-text.footnote.mt-12")
                        self.shortDescription = shortDescriptionEl.inner_text() if shortDescriptionEl else None
                        timeEl = car.query_selector(".common-text.footnote.c-contrastSecondary")
                        self.time = timeEl.inner_text() if timeEl else None
                        print(f"Saved: {self.carUrl, self.model, self.generation, self.cost, self.mileage, self.fuelType, self.gearbox, self.location, self.shortDescription, self.time}")
                        self.add_to_data()
                    button = page.query_selector(".ml-16 > .size-large")
                    if button:
                        button.click()
                        page.wait_for_timeout(5000)
                    else:
                        break
            except Exception as e:
                print(f'An error occurred during scraping: {e}')

            finally:
                print(f'Saving data to: {self.filename}')
                self.clear_and_create_xlsx_table()
                browser.close()

autoRia = Scraper("https://auto.ria.com/uk/search/?search_type=1&category=1&all[0].any[0].state=16&all[0].any[0].any[0].city=16&abroad=0&customs_cleared=1", "autoRia.xlsx")
autoRia.scrape()