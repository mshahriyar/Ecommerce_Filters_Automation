from pages.base_page import BasePage
import re

class EmiratesFilter(BasePage):

    FILTER_BTN = "//span[text()='Emirate']"
    SELECT_EMIRATE = "//label//span[text()='Dubai']"
    APPLY_BTN = "(//*[@data-testid='button-show-results'])[1]"
    CITY = "//h2/following-sibling::div[@id='ad-cars-card-location']//p"

    def apply(self, emirate="Dubai"):
        self.click(self.FILTER_BTN)
        self.click(self.SELECT_EMIRATE)
        self.click(self.APPLY_BTN)
        self.wait_for_results()
        return emirate


    def validate(self):
        
        self.page.locator("//div[@id='ad-cars-card']").first.wait_for(state="visible", timeout=15000)
        location = self.page.locator(self.CITY)
        count = location.count()

        assert count > 0, "❌ No results found!"

        for i in range(count):
            text = location.nth(i).inner_text(timeout=2000).strip()

            assert "Dubai" in text, f"❌ {text} is outside Dubai"



