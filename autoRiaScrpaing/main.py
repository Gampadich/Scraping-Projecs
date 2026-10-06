from playwright.sync_api import sync_playwright
import pandas


class Scraper:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.df = None

        # Temporary fields for current car data
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

        # Storage for scraped records
        self.data = {
            'URL': [],
            'Model': [],
            'Generation': [],
            'Cost': [],
            'Mileage': [],
            'Gearbox': [],
            'Fuel Type': [],
            'Location': [],
            'Short Description': [],
            'Time': []
        }

    def clear_and_create_xlsx_table(self):
        """Processes collected data and exports it to an Excel spreadsheet."""
        self.df = pandas.DataFrame(self.data)
        clear_data = self.df.drop_duplicates().fillna(' ')
        clear_data.to_excel(f'./{self.filename}', index=False)

    def add_to_data(self):
        """Appends current car details into the main dataset dictionary."""
        self.data['URL'].append(self.carUrl)
        self.data['Model'].append(self.model)
        self.data['Generation'].append(self.generation)
        self.data['Cost'].append(self.cost)
        self.data['Mileage'].append(self.mileage)
        self.data['Gearbox'].append(self.gearbox)
        self.data['Fuel Type'].append(self.fuelType)
        self.data['Location'].append(self.location)
        self.data['Short Description'].append(self.shortDescription)
        self.data['Time'].append(self.time)

    def scrape(self):
        """Launches the Playwright browser session and iterates over pagination."""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.url)
            page.wait_for_timeout(1000)

            try:
                while True:
                    # Query all vehicle listing cards on the current page
                    cars = page.query_selector_all(".link.product-card.horizontal")

                    for car in cars:
                        # Direct attribute & element extractions
                        href = car.get_attribute("href")
                        self.carUrl = "https://auto.ria.com" + href if href else None

                        model_el = car.query_selector(".common-text.size-16-20.titleS.fw-bold.mb-4")
                        self.model = model_el.inner_text().strip() if model_el else None

                        generation_el = car.query_selector(".common-text.size-14-16.ellipsis-1.mb-8")
                        self.generation = generation_el.inner_text().strip() if generation_el else None

                        cost_el = car.query_selector(".common-text.titleM.c-green")
                        self.cost = cost_el.inner_text().replace('\xa0', ' ').strip() if cost_el else None

                        # Safe extraction of feature tags (mileage, gearbox, fuel, location)
                        elements = car.query_selector_all(".common-text.ellipsis-1.body")
                        self.mileage = elements[0].inner_text().strip() if len(elements) > 0 else None
                        self.gearbox = elements[1].inner_text().strip() if len(elements) > 1 else None
                        self.fuelType = elements[2].inner_text().strip() if len(elements) > 2 else None
                        self.location = elements[3].inner_text().strip() if len(elements) > 3 else None

                        short_desc_el = car.query_selector(".common-text.footnote.mt-12")
                        self.shortDescription = short_desc_el.inner_text().strip() if short_desc_el else None

                        time_el = car.query_selector(".common-text.footnote.c-contrastSecondary")
                        self.time = time_el.inner_text().strip() if time_el else None

                        print(f"Saved: {self.model} | {self.cost} | {self.location}")
                        self.add_to_data()

                    # Handle pagination ("Show More" button)
                    button = page.query_selector(".ml-16 > .size-large")
                    if button and button.is_visible():
                        button.click()
                        page.wait_for_timeout(4000)
                    else:
                        break

            except Exception as e:
                print(f'An error occurred during scraping: {e}')

            finally:
                print(f'Saving data to: {self.filename}')
                self.clear_and_create_xlsx_table()
                browser.close()


# Execution entry point
autoRia = Scraper(
    "https://auto.ria.com/uk/search/?search_type=1&category=1&all[0].any[0].state=16&all[0].any[0].any[0].city=16&abroad=0&customs_cleared=1",
    "autoRia.xlsx"
)
autoRia.scrape()