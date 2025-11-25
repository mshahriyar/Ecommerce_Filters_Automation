from pages.base_page import BasePage
from playwright.sync_api import TimeoutError


class PaginationValidator(BasePage):

    NEXT_BTN = "//button[@data-testid='pagination-next-button']"
    RESULT_CARD = "//div[@id='ad-cars-card']"

    def wait_for_results(self):
        """
        Wait for result cards to appear to avoid validating empty or loading state.
        """
        cards = self.page.locator(self.RESULT_CARD)
        cards.first.wait_for(state="visible", timeout=15000)
        self.page.wait_for_timeout(300)


    def validate_all_pages(self, validate_filters_fn, validate_fascination_fn=None, max_pages=3):
        for page_no in range(1, max_pages + 1):

            print(f"\n===== VALIDATING PAGE {page_no} =====")

            # 1. Make sure results are loaded
            self.wait_for_results()

            # 2. Validate filters
            validate_filters_fn()

            # 3. Validate fascination if provided
            if validate_fascination_fn:
                validate_fascination_fn()

            # 4. Try to go to next page
            next_btn = self.page.locator(self.NEXT_BTN)

            # If next button is not visible → stop
            if not next_btn.is_visible():
                print("🚫 No next page. Pagination finished.")
                break

            try:
                next_btn.click(force=True)
            except:
                print("⚠️ Next button click failed due to overlay or obstruction. Stopping.")
                break

            self.wait_for_results()

        print("\n🎉 Pagination Validation Complete\n")







