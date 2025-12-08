import pytest
from pages.base_page import BasePage
from playwright.sync_api import expect

class PaginationValidator(BasePage):

    NEXT_BTN = "//button[@data-testid='pagination-next-button']"
    RESULT_CARD = "//div[@id='ad-cars-card']"
    NO_RESLUTTS_MSG = "//*[text() ='Sorry! No result found :(']"
    ITEMS = "//div[contains(@class,'overflow-x-auto')]//button"

    def wait_for_results(self):
        cards = self.page.locator(self.RESULT_CARD)
        cards.first.wait_for(state="visible", timeout=15000)
        self.page.wait_for_timeout(300)


    def validate_all_pages(self, validate_filters_fn, validate_fascination_fn=None, max_pages=3):
        items = self.page.locator(self.ITEMS)
        no_result = self.page.locator(self.NO_RESLUTTS_MSG)
        next_btn = self.page.locator(self.NEXT_BTN)

        for page_no in range(1, max_pages + 1):            
            print(f"\n===== VALIDATING PAGE {page_no} =====")
            if items.count() > 0:
                expect(no_result).not_to_be_visible(timeout=2000)

            else:
                expect(no_result).to_be_visible(timeout=3000)
                pytest.skip("⏭ Skipped: No results found for the applied filters.")
            self.wait_for_results()

            validate_filters_fn()

            if validate_fascination_fn:
                validate_fascination_fn()

            if not next_btn.is_visible():
                print("🚫 No next page. Pagination finished.")
                break

            try:
                next_btn.click(force=True)
            except:
                print("⚠️ Next button click failed due to overlay or obstruction. Stopping.")
                break

            self.wait_for_results()









