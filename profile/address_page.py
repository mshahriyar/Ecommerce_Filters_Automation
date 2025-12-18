

from pages.base_page import BasePage
from playwright.sync_api import expect


class AddressPage(BasePage):

    PROFILE_ICON = "//img[@class='object-cover']"
    SETTINGS = "//button[@data-testid='account-button']/following-sibling::span//a[@data-testid='menu-settings']"
    DELIVERY_ADDRESS_TAB = "//button[text()='Delivery Address']"
    ADDRESS_URL = "https://portal-v2.qa.ayshei.io/dashboard/settings?tab=delivery-addresses"

    ADD_NEW_ADDRESS_BTN = "//button[text()='Add New Delivery Address']"

    FIRST_NAME_INPUT = "//input[@placeholder='First Name']"
    LAST_NAME_INPUT = "//input[@placeholder='Last Name']"
    MOBILE_NUMBER_INPUT = "input[name='mobile_number']"

    EMIRATES_DROPDOWN = "//div[@aria-label='emirate']//div[@id='emirate']"
    EMIRATE_OPTION = "//li[@role='option' and normalize-space()='{}']"

    AREA = "//input[@placeholder='Area']"
    STREET_ADDRESS = "//input[@placeholder='Street']"
    BUILDING_INPUT = "//input[@placeholder='Building Name']"
    APT_VILLA_NUMBER_INPUT = "//input[@placeholder='Apt/Villa No.']"
    NEAREST_LANDMARK_INPUT = "//input[@placeholder='Nearest Landmark']"

    SAVE_ADDRESS_BTN = "//button[@data-testid='form-submit-button']"

    DELIVERY_CONTAINER = "//div[@id='delivery-addresses']"

    EDIT_ICON = "(//img[@src='/icons/edit-addr.svg'])[1]"
    DELETE_ICON = "(//img[@src='/icons/remove-addr.svg'])[1]"

    EDIT_BTN = "(//span[text()='Edit'])[1]"
    DELETE_BTN = "(//span[text()='Remove'])[1]"

    CONFIRM_DELETE_BTN = "//button[text()='Yes, Remove!']"

    def go_to_address_page(self):
        self.page.locator(self.PROFILE_ICON).click()
        self.page.locator(self.SETTINGS).click()
        self.page.locator(self.DELIVERY_ADDRESS_TAB).click()
        expect(self.page).to_have_url(self.ADDRESS_URL)

    def open_address_form(self):
        container = self.page.locator(self.DELIVERY_CONTAINER)
    
        try:
            expect(container).to_be_visible()
            add_new_address = self.page.locator(self.ADD_NEW_ADDRESS_BTN)
            add_new_address.wait_for(state="visible", timeout=5000)
            add_new_address.click()
        except:
            title = self.page.locator("//h4[normalize-space()='Add New Delivery Address']")
            assert title.is_visible(), "❌ Add New Payment Method title not visible"
            sub_title =self.page.locator("//p[normalize-space()='Add a delivery address for...']")
            assert sub_title.is_visible(), "❌ Add New Payment Method subtitle not visible"
            address_img = self.page.locator("//img[@alt = 'icon']")
            assert address_img.is_visible(), "❌ Card image not visible"
            add_address = self.page.locator(self.ADD_NEW_ADDRESS_BTN)
            expect(add_address).to_be_visible()
            add_address.click()

        self.page.locator("//div[@id='modal-body']").wait_for(
            state="visible", timeout=5000)


    def fill_address_form(
        self,
        first_name,
        last_name,
        mobile_number,
        emirate,
        area,
        street,
        building,
        apt_villa_no,
        landmark
    ):
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.MOBILE_NUMBER_INPUT, mobile_number)

        self.click(self.EMIRATES_DROPDOWN)
        emirate_option = self.page.locator(self.EMIRATE_OPTION.format(emirate))
        emirate_option.wait_for(state="visible", timeout=5000)
        emirate_option.click()

        self.fill(self.AREA, area)
        self.fill(self.STREET_ADDRESS, street)
        self.fill(self.BUILDING_INPUT, building)
        self.fill(self.APT_VILLA_NUMBER_INPUT, apt_villa_no)
        self.fill(self.NEAREST_LANDMARK_INPUT, landmark)

    def save_address(self):
        self.click(self.SAVE_ADDRESS_BTN)
        self.page.locator("//h5[text()='Congratulations!']").wait_for(state="visible", timeout=5000)


    def verify_popup(self, heading_text, message_text, confirm=False):
        img = self.page.locator("//img[@alt='confirm']")
        heading = self.page.locator(f"//h5[normalize-space()='{heading_text}']")
        message = self.page.locator(f"//p[normalize-space()='{message_text}']")
        close_btn = self.page.get_by_test_id("button-close")

        img.wait_for(state="visible", timeout=5000)

        assert heading.is_visible(), f"❌ Missing heading: {heading_text}"
        assert message.is_visible(), f"❌ Missing message: {message_text}"

        if confirm:
            self.page.locator(self.CONFIRM_DELETE_BTN).click()
        else:
            assert close_btn.is_visible(), "❌ Close button not visible"
            close_btn.click()



    def open_action_icon(self, action: str):
        container = self.page.locator(self.DELIVERY_CONTAINER)
        container.wait_for(state="visible", timeout=5000)

        if action == "edit":
            icon = self.page.locator(self.EDIT_ICON)
            button = self.page.locator(self.EDIT_BTN)
        elif action == "delete":
            icon = self.page.locator(self.DELETE_ICON)
            button = self.page.locator(self.DELETE_BTN)
        else:
            raise ValueError("Unsupported action")

        icon.scroll_into_view_if_needed()
        icon.hover()
        expect(icon).to_be_visible()
        button.click()

    def edit_address(self):
        self.open_action_icon("edit")

    def verify_edit_success(self):
        self.verify_popup(
            heading_text="Congratulations!",
            message_text="Address updated successfully."
        )

    def delete_address(self):
        self.open_action_icon("delete")

        self.verify_popup(
            heading_text="Remove Delivery Address",
            message_text="Are you sure you want to remove this Delivery Address?",
            confirm=True
        )

        self.page.locator("//h5[text()='Congratulations!']").wait_for(
            state="detached",
            timeout=5000
        )
