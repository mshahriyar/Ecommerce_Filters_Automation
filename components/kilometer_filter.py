import re
from pages.base_page import BasePage


class KilomterFilter(BasePage):
    FILTER_BTN = "//span[text()='Kilometers']"
    FROM_INPUT = "//span[normalize-space()='From']/parent::div/input"
    TO_INPUT = "//span[normalize-space()='To']/parent::div/input"
    APPLY_BTN = "(//*[@data-testid='button-show-results'])[1]"
    KM_VALUES = "//div[@id='ad-cars-card-more-details']//p[contains(text(),'km')]"

    def apply(self, min_km, max_km):
        self.click(self.FILTER_BTN)
        self.wait_for_visible(self.FROM_INPUT, timeout=10000)
        self.fill(self.FROM_INPUT, min_km)
        self.fill(self.TO_INPUT, max_km)
        self.click(self.APPLY_BTN)
        self.wait_for_results() 

        self._active_range = (int(min_km), int(max_km))
        return self._active_range

    def validate(self, min_km=None, max_km=None):

        kilometer_locator = self.page.locator(self.KM_VALUES)
        kilometer_locator.first.wait_for(state="visible", timeout=15000)
        count = kilometer_locator.count()

        assert count > 0, "❌ No results found!"
        for i in range(count):
            text = kilometer_locator.nth(i).inner_text()
            km = int(re.sub(r"[^\d]", "", text))
            assert min_km <= km <= max_km, f"❌ {km} is outside range"


