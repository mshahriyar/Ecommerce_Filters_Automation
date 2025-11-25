import re
from pages.base_page import BasePage

class FascinationCarousel(BasePage):

    ITEMS = "//div[contains(@class,'overflow-x-auto')]//button"

    def wait_for_fascination(self):
        items = self.page.locator(self.ITEMS)
        items.first.wait_for(state="visible", timeout=15000)
        return items


    def validate_fascination(self):
        items = self.wait_for_fascination()
        count = items.count()

        assert count > 0, "❌ No fascination items found!"

        for i in range(count):
            el = items.nth(i)
            text = el.inner_text().strip()
            assert el.is_visible(), f"❌ Fascination item '{text}' is NOT visible!"

        
        print(f"✅ Fascination items visible: {count}")
