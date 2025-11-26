import re
from pages.base_page import BasePage

class PriceFilter(BasePage):

    FILTER_BTN = "//span[text()='Price']"
    FROM_INPUT = "//span[normalize-space()='From']/parent::div/input"
    TO_INPUT = "//span[normalize-space()='To']/parent::div/input"
    APPLY_BTN = "(//*[@data-testid='button-show-results'])[1]"
    PRICE_VALUES = "//div[@id='ad-cars-card-price-info']//p[not(contains(text(), 'AED'))]"

    def apply(self, min_price, max_price):
        """Apply the price filter and store the active range for later validation."""
        self.click(self.FILTER_BTN)
        self.fill(self.FROM_INPUT, min_price)
        self.fill(self.TO_INPUT, max_price)
        self.click(self.APPLY_BTN)
        self.wait_for_results() 

        self._active_range = (int(min_price), int(max_price))
        return self._active_range


    def validate(self, min_val=None, max_val=None):
        if min_val is None or max_val is None:
            assert hasattr(self, "_active_range"), "No active price range to validate."
            min_val, max_val = self._active_range

        prices_locator = self.page.locator(self.PRICE_VALUES)
        prices_locator.first.wait_for(state="visible", timeout=15000)
        count = prices_locator.count()

        assert count > 0, "❌ No results found!"

        for i in range(count):
            text = prices_locator.nth(i).inner_text()
            price = int(re.sub(r"[^\d]", "", text))
            assert min_val <= price <= max_val, f"❌ {price} is outside range"

        print(f"✅ All prices are within {min_val} – {max_val} AED")
