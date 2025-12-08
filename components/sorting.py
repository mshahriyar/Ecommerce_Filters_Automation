from pages.base_page import BasePage
import re


class Sorting(BasePage):

    SORT_BTN = "//div[contains(@class, 'border-stroke')]/following-sibling::div//span[text() = 'Sort by']"
    PRICE_VALUES = "//div[@id='ad-cars-card-price-info']//p[not(contains(text(), 'AED'))]"
    KM_VALUES = "//div[@id='ad-cars-card-more-details']//p[contains(text(),'km')]"
    YEARS_VALUES = "//div[@id='ad-cars-card-more-details']//p"

    def apply(self, option):
        self.click(self.SORT_BTN)
        option_locator = self.page.locator(f"//p[text() = '{option}']")
        option_locator.wait_for(state="visible", timeout=5000)
        option_locator.click()
        self.wait_for_results() 
        return option
    
    def get_price_sort_by(self):
        prices_locator = self.page.locator(self.PRICE_VALUES)
        prices_locator.first.wait_for(state="visible", timeout=15000)

        count = prices_locator.count()

        assert count > 0, "❌ No results found!"

        prices = []
        for i in range(count):
            text = prices_locator.nth(i).inner_text()
            price = int(re.sub(r"[^\d]", "", text))
            prices.append(price)

        return prices
    
    def get_km_sort_by(self):

        cards = self.page.locator(self.KM_VALUES)
        total = cards.count()

        mileages = []

        for i in range(total):
            text = cards.nth(i).inner_text().lower().strip()

            if "km" not in text:
                continue

            before_km = text.split("km")[0]

            digits_only = re.sub(r"[^\d]", "", before_km)

            if digits_only:
                mileages.append(int(digits_only))

        return mileages
        
    def get_year_sort_by(self):
        details = self.page.locator(self.YEARS_VALUES)
        total = details.count()

        years = []

        for i in range(total):
            text = details.nth(i).inner_text().strip()

            match = re.search(r"\b(19|20)\d{2}\b", text)
            if not match:
                continue

            year = int(match.group(0))
            years.append(year)

        return years