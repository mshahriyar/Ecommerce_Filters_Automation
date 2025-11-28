from pages.base_page import BasePage
import re

class RegionalFilter(BasePage):

    FILTER_BTN = "//span[text()='Regional Spec']"
    APPLY_BTN = "(//*[@data-testid='button-show-results'])[1]"
    DETAILS = "//div[@id='ad-cars-card-more-details']//p"

    def apply(self, regions):

        self.click(self.FILTER_BTN)

        for region in regions:
            locator =self.page.locator(f"//span[text()='{region}']")
            locator.wait_for(state="visible", timeout=5000)
            locator.click()

        self.click(self.APPLY_BTN)
        self.wait_for_results() 
        return regions

    def validate(self, allowed):
        details = self.page.locator(self.DETAILS)
        details.first.wait_for(state="visible", timeout=20000)
        count = details.count()
        assert count > 0, "❌ No car details found to validate!"

        pattern = "|".join([rf"\b{reg}\b" for reg in allowed])
        matched = []
        for i in range(count):
            text = details.nth(i).inner_text().strip()

            if re.search(pattern, text, re.IGNORECASE):
                matched.append(text)
            else:
                continue
 
        assert len(matched) > 0, (
            f"❌ No region info found in the results!\nAllowed: {allowed}"
        )
    
        for found in matched:
            assert any(reg.lower() in found.lower() for reg in allowed), \
                f"❌ Invalid region '{found}' not in allowed list {allowed}"
        print(f"✅ All validated regions are within allowed: {allowed}")

    
