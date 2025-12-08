from pages.base_page import BasePage

class MakeAndModelFilter(BasePage):
    
    MORE_FILTERS_BTN = "//span[text() ='More Filters']"
    MAKE_DROPDOWN = "//*[text() ='Make']"
    SEARCH_OPTION = "//*[@id ='input-search-text']"
    SELECT_MAKE = "//label/span[text()='AUDI']"
    SAVE_BTN = "//button[text()='Save']"
    MODEL_DROPDOWN = "//*[text() ='Model']"
    SELECT_MODEL = "//label/span[text()='A6']"
    SHOW_RESULTS = "//button[text()='Show Results']"
    RESULT_CARD = "//div[@id='ad-cars-card-details']"

    def select_make(self, make):
        self.click(self.MORE_FILTERS_BTN)
        self.click(self.MAKE_DROPDOWN)
        self.fill(self.SEARCH_OPTION, make)
        self.click(self.SELECT_MAKE)
        self.click(self.SAVE_BTN)
        self.click(self.SHOW_RESULTS)
        self.wait_for_results()
        return make
    
    def select_model(self, model):
        self.click(self.MORE_FILTERS_BTN)
        self.click(self.MODEL_DROPDOWN)
        self.fill(self.SEARCH_OPTION, model)
        self.click(self.SELECT_MODEL.format(model))
        self.click(self.SAVE_BTN)
        self.click(self.SHOW_RESULTS)
        self.wait_for_results()
        return model


    def validate_make_and_model(self, make, model):

        cards = self.page.locator(self.RESULT_CARD)
        cards.first.wait_for(state="visible", timeout=15000)

        total = cards.count()
        assert total > 0, "❌ No results found!"

        validated = 0

        for i in range(total):
            card = cards.nth(i)

            mm = card.locator("xpath=.//div[@id='ad-cars-card-make']")

            if mm.count() == 0:
                print(f"⚠️  Card #{i+1} has no Make/Model block — skipping.")
                continue

            raw = mm.inner_text().strip()

            parts = raw.split()

            card_make = parts[0]
            card_model = parts[-1]

            assert make.lower() in card_make.lower(), \
                f"❌ Card #{i+1}: Expected Make '{make}', got '{card_make}'."

            assert model.lower() in card_model.lower(), \
                f"❌ Card #{i+1}: Expected Model '{model}', got '{card_model}'."

            validated += 1

        assert validated > 0, f"❌ No valid cards matched '{make} {model}'."
        
