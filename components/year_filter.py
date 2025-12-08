import re
from pages.base_page import BasePage

class YearFilter(BasePage):

    FILTER_BTN = "//span[text()='Year']"
    FROM_INPUT = "//span[normalize-space()='From']/parent::div/input"
    TO_INPUT = "//span[normalize-space()='To']/parent::div/input"
    APPLY_BTN = "(//*[@data-testid='button-show-results'])[1]"
    YEAR_VALUES = "//div[@id='ad-cars-card-more-details']//p"

    def apply(self, start, end):
        self.click(self.FILTER_BTN)
        self.fill(self.FROM_INPUT, start)
        self.fill(self.TO_INPUT, end)
        self.click(self.APPLY_BTN)
        self.wait_for_results() 
        self._active_range = (int(start), int(end))
        return self._active_range

    def validate(self, min_year, max_year):
        details = self.page.locator(self.YEAR_VALUES)
        details.first.wait_for(state="visible", timeout=15000)
        count = details.count()

        assert count > 0, "❌ No details found!"

        years = []
        for i in range(count):
            t = details.nth(i).inner_text().strip()
            match = re.findall(r"\b(19\d{2}|20\d{2})\b", t)
            if match:
                year = int(match[0])
                assert min_year <= year <= max_year
                years.append(year)

        assert years, "❌ No valid year found!"
        return years
