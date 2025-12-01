from pages.base_page import BasePage

class MoreFilters(BasePage):

    MAKE_LABEL = "[data-testid='ad-overview-label-make']"
    MAKE_VALUE = "[data-testid='ad-overview-value-make']"

    MODEL_LABEL = "[data-testid='ad-overview-label-model']"
    MODEL_VALUE = "[data-testid='ad-overview-value-model']"

    TRIM_LABEL = "[data-testid='ad-overview-label-trim']"
    TRIM_VALUE = "[data-testid='ad-overview-value-trim']"

    YEAR_LABEL = "[data-testid='ad-overview-label-year']"
    YEAR_VALUE = "[data-testid='ad-overview-value-year']"

    KILOMETRAGE_LABEL = "[data-testid='ad-overview-label-kilometers']"
    KILOMETRAGE_VALUE = "[data-testid='ad-overview-value-kilometers']"

    REGIONAL_SPEC_LABEL = "[data-testid='ad-overview-label-regional-spec']"
    REGIONAL_SPEC_VALUE = "[data-testid='ad-overview-value-regional-spec']"

    BODY_TYPE_LABEL = "[data-testid='ad-overview-label-body-type']"
    BODY_TYPE_VALUE = "[data-testid='ad-overview-value-body-type']"

    FUEL_TYPE_LABEL = "[data-testid='ad-overview-label-fuel-type']"
    FUEL_TYPE_VALUE = "[data-testid='ad-overview-value-fuel-type']"

    TRANSMISSION_LABEL = "[data-testid='ad-overview-label-transmission']"
    TRANSMISSION_VALUE = "[data-testid='ad-overview-value-transmission']"

    EXTERIOR_COLOR_LABEL = "[data-testid='ad-overview-label-exterior-color']"
    EXTERIOR_COLOR_VALUE = "[data-testid='ad-overview-value-exterior-color']"

    STEERING_SIDE_LABEL = "[data-testid='ad-overview-label-steering-side']"
    STEERING_SIDE_VALUE = "[data-testid='ad-overview-value-steering-side']"

    WARRANTY_LABEL = "[data-testid='ad-overview-label-warranty']"
    WARRANTY_VALUE = "[data-testid='ad-overview-value-warranty']"

    NO_OF_DOORS_LABEL = "[data-testid='ad-overview-label-no-of-doors']"
    NO_OF_DOORS_VALUE = "[data-testid='ad-overview-value-no-of-doors']"

    BODY_CONDITION_LABEL = "[data-testid='ad-overview-label-body-condition']"
    BODY_CONDITION_VALUE = "[data-testid='ad-overview-value-body-condition']"

    NO_OF_CYLINDERS_LABEL = "[data-testid='ad-overview-label-no-of-cylinders']"
    NO_OF_CYLINDERS_VALUE = "[data-testid='ad-overview-value-no-of-cylinders']"

    NO_OF_SEATS_LABEL = "[data-testid='ad-overview-label-no-of-seats']"
    NO_OF_SEATS_VALUE = "[data-testid='ad-overview-value-no-of-seats']"

    INSURED_LABEL = "[data-testid='ad-overview-label-insured']"
    INSURED_VALUE = "[data-testid='ad-overview-value-insured']"

 

    # HORSEPOWER_DROPDOWN = "//*[text()='Horsepower']"
    # SELECT_HORSEPOWER = "//label/span[text()='{}']"

    # CYLINDER_DROPDOWN = "//*[text()='No. of Cylinders']"
    # SELECT_CYLINDER = "//label/span[text()='{}']"

    # INTERIOR_COLOR_DROPDOWN = "//*[text()='Interior Colors']"
    # SELECT_INTERIOR_COLOR = "//label/span[text()='{}']"

    MAKE_DROPDOWN = "//*[text() ='Make']"
    SELECT_MAKE = "//label/span[text()='AUDI']"

    MODEL_DROPDOWN = "//*[text() ='Model']"
    SELECT_MODEL = "//label/span[text()='A6']"

    TRIM_DROPDOWN = "//*[text()='Trim']"
    SELECT_TRIM = "//label/span[text()='40 TFSI']"

    BODY_TYPE_DROPDOWN = "//*[text()='Body Type']"
    SELECT_BODY_TYPE = "//label/span[text()='Sedan']"


    SELECT_FUEL_TYPE = "//*[text()='Gasoline']"
    SELECT_AUTOMATIC_TRANSMISSION = "//*[text()='Automatic Transmission']"

    EXTERIOR_COLORS_DROPDOWN = "//*[text()='Exterior Colors']"
    SELECT_EXTERIOR_COLORS = "//label//span[text()='Black']"

    SELECT_STEERING_SIDE = "//*[text()='Left Hand']"
    SELECT_WARRANTY = "//*[text()='No']"
    SELECT_NO_OF_DOORS = "//*[text()='4 Doors']"
    # SELECT_BODY_CONDITION = "//*[text()='Excellent']"
    # SELECT_NO_OF_SEATS = "//*[text()='4 Seats']"

    SAVE_BTN = "//button[text()='Save']"
    MORE_FILTERS_BTN = "//span[text() ='More Filters']"
    SEARCH_OPTION = "//*[@id ='input-search-text']"
    SHOW_RESULTS = "//button[text()='Show Results']"
    RESULT_CARD = "//div[@id='ad-cars-card']"

    SEE_MORE_BTN = "//div[@id='product-overview-section']//span"


    def apply_dropdown_filter(self, dropdown, search_value, option_locator):
        """Dropdown filters using search box."""
        self.click(self.MORE_FILTERS_BTN)
        self.click(dropdown)
        self.fill(self.SEARCH_OPTION, search_value)
        self.click(option_locator)
        self.click(self.SAVE_BTN)

    def apply_direct_filter(self, option_locator):
        """Filters that are not dropdowns (chips/buttons)."""
        self.click(self.MORE_FILTERS_BTN)
        self.click(option_locator)
        self.click(self.SAVE_BTN)

    def apply_all_filters(self):

        # OPEN MORE FILTERS ONLY ONCE
        self.click(self.MORE_FILTERS_BTN)

        # --- DROPDOWN FILTERS ---
        self.click(self.MAKE_DROPDOWN)
        self.fill(self.SEARCH_OPTION, "AUDI")
        self.click(self.SELECT_MAKE)
        self.click(self.SAVE_BTN)

        self.click(self.MODEL_DROPDOWN)
        self.fill(self.SEARCH_OPTION, "A6")
        self.click(self.SELECT_MODEL)
        self.click(self.SAVE_BTN)

        self.click(self.TRIM_DROPDOWN)
        self.fill(self.SEARCH_OPTION, "40 TFSI")
        self.click(self.SELECT_TRIM)
        self.click(self.SAVE_BTN)

        self.click(self.BODY_TYPE_DROPDOWN)
        self.click(self.SELECT_BODY_TYPE)
        self.click(self.SAVE_BTN)

        self.click(self.SELECT_FUEL_TYPE)

        self.click(self.SELECT_AUTOMATIC_TRANSMISSION)

    
        self.click(self.EXTERIOR_COLORS_DROPDOWN)
        self.click(self.SELECT_EXTERIOR_COLORS)
        self.click(self.SAVE_BTN)

        self.click(self.SELECT_STEERING_SIDE)

        # self.click(self.SELECT_WARRANTY)

        # self.click(self.SELECT_NO_OF_DOORS)

        # DONE → APPLY FILTERS
        self.click(self.SHOW_RESULTS)
        self.wait_for_results()


    def open_first_card(self):
        card = self.page.locator(self.RESULT_CARD)
        card.wait_for(state="visible", timeout=15000)
        card.click(force=True)
        self.page.wait_for_load_state("domcontentloaded")
        


    def validate_overview_details(self, expected):
        self.page.locator(self.SEE_MORE_BTN).scroll_into_view_if_needed()
        self.click(self.SEE_MORE_BTN)

        checks = {
            "Make": (self.MAKE_LABEL, self.MAKE_VALUE, expected["make"]),
            "Model": (self.MODEL_LABEL, self.MODEL_VALUE, expected["model"]),
            "Trim": (self.TRIM_LABEL, self.TRIM_VALUE, expected["trim"]),
            "Year": (self.YEAR_LABEL, self.YEAR_VALUE, expected["year"]),
            "Kilometers": (self.KILOMETRAGE_LABEL, self.KILOMETRAGE_VALUE, expected["kilometers"]),
            "Regional Spec": (self.REGIONAL_SPEC_LABEL, self.REGIONAL_SPEC_VALUE, expected["regional_spec"]),
            "Body Type": (self.BODY_TYPE_LABEL, self.BODY_TYPE_VALUE, expected["body_type"]),
            "Fuel Type": (self.FUEL_TYPE_LABEL, self.FUEL_TYPE_VALUE, expected["fuel_type"]),
            "Transmission": (self.TRANSMISSION_LABEL, self.TRANSMISSION_VALUE, expected["transmission"]),
            "Exterior Color": (self.EXTERIOR_COLOR_LABEL, self.EXTERIOR_COLOR_VALUE, expected["exterior_color"]),
            "Steering Side": (self.STEERING_SIDE_LABEL, self.STEERING_SIDE_VALUE, expected["steering_side"]),
            "Warranty": (self.WARRANTY_LABEL, self.WARRANTY_VALUE, expected["warranty"]),
            "No. of Doors": (self.NO_OF_DOORS_LABEL, self.NO_OF_DOORS_VALUE, expected["doors"]),
            "Body Condition": (self.BODY_CONDITION_LABEL, self.BODY_CONDITION_VALUE, expected["body_condition"]),
            "No. of Cylinders": (self.NO_OF_CYLINDERS_LABEL, self.NO_OF_CYLINDERS_VALUE, expected["cylinders"]),
            "No. of Seats": (self.NO_OF_SEATS_LABEL, self.NO_OF_SEATS_VALUE, expected["seats"]),
            "Insured": (self.INSURED_LABEL, self.INSURED_VALUE, expected["insured"]),
        }

        for label_name, (label_sel, value_sel, expected_val) in checks.items():

            label_loc = self.page.locator(label_sel)
            value_loc = self.page.locator(value_sel)

            if label_loc.count() == 0:
                print(f"⚠️ Skipping missing label {label_name}")
                continue

            actual_value = value_loc.inner_text().strip()

            assert expected_val.lower() in actual_value.lower(), \
                f"❌ {label_name} mismatch — expected: {expected_val}, found: {actual_value}"

            print(f"✅ {label_name}: {actual_value}")
