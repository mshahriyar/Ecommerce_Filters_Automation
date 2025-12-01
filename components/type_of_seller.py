
import pytest
from pages.base_page import BasePage

class TypeOfSeller(BasePage):

    IMG_DEALER = "//span//img[@alt='user avatar']"
    DEALER = "//div[@class='flex gap-2 px-4 md:px-8']//span[text()='Dealer']"
    OWNER = "//div[@class='flex gap-2 px-4 md:px-8']//span[text()='Owner']"
    RESULT_CARD = "//div[@id='ad-cars-card-details']"

    def select_seller_type(self, seller_type):
        if seller_type == "Dealer":
            self.click(self.DEALER)
        elif seller_type == "Owner":
            self.click(self.OWNER)

        self.wait_for_results()
        return seller_type

    def validate_seller_type(self, seller_type):

        cards = self.page.locator(self.RESULT_CARD)
        cards.first.wait_for(state="visible", timeout=15000)

        total = cards.count()
        assert total > 0, "❌ No results found!"

        for i in range(total):
            card = cards.nth(i)

            # Look for avatar INSIDE THIS CARD, not globally
            avatar = card.locator("//span//img[@alt = 'user avatar']")

            avatar_present = avatar.count() > 0 and avatar.is_visible()

            if seller_type == "Dealer":
                assert avatar_present, f"Card #{i+1} → Dealer has not avatar present"
            if seller_type == "Owner":
                assert not avatar_present, f"❌ Card #{i+1} is NOT Owner"

        print(f"✅ All {total} results belong to: {seller_type}")
