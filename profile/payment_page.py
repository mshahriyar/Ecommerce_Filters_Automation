
from pages.base_page import BasePage
from playwright.sync_api import expect

class PaymentPage(BasePage):

    PROFILE_ICON = "//img[@class='object-cover']"
    SETTINGS = "//button[@data-testid='account-button']/following-sibling::span//a[@data-testid='menu-settings']"
    #Go to Settings and Tap payment method tab
    PAYMENT_ADDRESS_TAB = "//button[normalize-space()='Payment Method']"
    PAYMENT_ADDRESS_URL = "https://portal-v2.qa.ayshei.io/dashboard/settings?tab=payment-methods"
    #ADD PAYMENT
    ADD_NEW_PAYMENT_BTN = "//button[normalize-space()='Add New Payment Method']"
    ADD_PAYMENT_BTN = "//button[normalize-space()='Add Payment Method']"
    #ADD PAYMENT POP UP LOCATORS
    CARD_HOLDER_NAME = "//input[@id = 'cardholder-name']"
    CARD_NUMBER = "input[name='number']"
    EXPIRY = "input[name='expiry']"
    CVC = "input[name='cvc']"
    COUNTRY = "//select[@name='country']"
    ADD_CARD_BTN = "//button[text()='Add Card']"
    CANCEL_BTN = "//button[text()='Cancel']"
    
    #Successfull pop up
    MODAL = "(//div[@id='modal-body'])[2]" 
    IMG_SUCCESS = "(//img[@alt='confirm'])[2]"
    CONGRATS_HEADING = "//h5[text()='Congratulations!']"
    SUCCESS_MESSAGE = "//p[text()='Added payment method Successfully']"
    CLOSE_BTN = "//button[text() ='Close']"


    #POP UP CONTENT
    IMG = "//img[@alt='confirm']"
    HEADING = "(//h3[text()='Add Payment Method'])[2]"
    MESSAGE = "//p[text()='Enter your card details to add a new payment method to your account.']"
    DISCLAIMER = "//p[normalize-space()= 'By providing your card information, you allow Ayshei-QA to charge your card for future payments in accordance with their terms.']"
    
    #MAIN PAGE
    PAYMENT_CONTAINER = "//div[@id='delivery-addresses']"
    DELETE_BTN = "(//span[text()='Remove'])[1]"

    #DELETE POP UP CONTENT
    REMOVE_ICON = "(//img[@alt='delete'])[1]"
    HEADING_MSG = "//h5[normalize-space()='Remove payment method']"
    MESSAGE_TEXT = "//p[text() = 'Are you sure you want to remove this payment method?']"
    CONFIRM_DELETE_BTN = "//button[text()='Yes, Remove!']"

    def go_to_payment_page(self):
        self.page.locator(self.PROFILE_ICON).click()
        self.page.locator(self.SETTINGS).click()
        self.page.locator(self.PAYMENT_ADDRESS_TAB).click()
        expect(self.page).to_have_url(self.PAYMENT_ADDRESS_URL)

    def open_payment_form(self):
        container = self.page.locator(self.PAYMENT_CONTAINER)
    
        try:
            expect(container).to_be_visible()
            add_new_payment = self.page.locator(self.ADD_NEW_PAYMENT_BTN)
            add_new_payment.wait_for(state="visible", timeout=5000)
            add_new_payment.click()
        except:
            title = self.page.locator("//h4[normalize-space()='Add New Payment Method']")
            assert title.is_visible(), "❌ Add New Payment Method title not visible"
            sub_title =self.page.locator("//p[normalize-space()='Add a payment method for easy checkout.']")
            assert sub_title.is_visible(), "❌ Add New Payment Method subtitle not visible"
            card_img = self.page.locator("//img[@alt = 'icon']")
            assert card_img.is_visible(), "❌ Card image not visible"
            add_payment = self.page.locator(self.ADD_PAYMENT_BTN)
            expect(add_payment).to_be_visible()
            add_payment.click()

        self.page.locator("//div[@id='modal-body']").wait_for(
            state="visible", timeout=5000
        )


    def fill_payment_form(self, card_holder_name, card_number, expiry, cvc):

        self.page.locator(self.CARD_HOLDER_NAME).wait_for(state="visible", timeout=5000)
        self.page.locator(self.CARD_HOLDER_NAME).fill(card_holder_name)

        # Stripe iframe (ALWAYS iframe-based)
        stripe_frame = self.page.frame_locator(
            "iframe[name^='__privateStripeFrame']"
        ).first

        stripe_frame.locator("input[name='number']").wait_for(state="visible", timeout=10000)

        stripe_frame.locator(self.CARD_NUMBER).fill(card_number)
        stripe_frame.locator(self.EXPIRY).fill(expiry)
        stripe_frame.locator(self.CVC).fill(cvc)
        country_dropdown = stripe_frame.locator(self.COUNTRY)
        assert country_dropdown.is_visible(), "❌ Country dropdown not visible"
        disclaimer = stripe_frame.locator(self.DISCLAIMER)
        assert disclaimer.is_visible(), "❌ Missing disclaimer"


    def verify_add_payment_content(self):
        img = self.page.locator(self.IMG)
        heading = self.page.locator(self.HEADING)
        message = self.page.locator(self.MESSAGE)        
        close_btn = self.page.get_by_test_id("button-cancel")
        
        img.wait_for(state="visible", timeout=5000)

        assert img.is_visible(), "❌ Missing confirmation image"
        assert heading.is_visible(), "❌ Missing heading"
        assert message.is_visible(), "❌ Missing message"
        assert close_btn.is_visible(), "❌ Close button not visible"

        
    def save_payment_card(self):
        self.click(self.ADD_CARD_BTN)
        self.page.locator("//h5[text()='Congratulations!']").wait_for(state="visible", timeout=5000)

    def click_close_success_popup(self):
        assert self.page.locator(self.MODAL).is_visible(), "❌ Success modal not visible"
        assert self.page.locator(self.IMG_SUCCESS).is_visible(), "❌ Success image not visible"
        assert self.page.locator(self.CONGRATS_HEADING).is_visible(), "❌ Congratulations heading not visible"
        assert self.page.locator(self.SUCCESS_MESSAGE).is_visible(), "❌ Success message not visible"
        assert self.page.locator(self.CLOSE_BTN).is_visible(), "❌ Close button not visible"
        self.page.locator(self.CLOSE_BTN).click()
        self.page.locator(self.ADD_NEW_PAYMENT_BTN).wait_for(state="visible", timeout=5000)
        self.verify_payment_added(card_number="4242424242424242")

    def verify_payment_added(self, card_number: str):
        container = self.page.locator(self.PAYMENT_CONTAINER)
        container.wait_for(state="visible", timeout=5000)
        total = container.count()
        assert total > 0, "❌ No payment methods found!"
        expected_last4 = card_number[-4:]
        card_text_locator = self.page.locator("//p[contains(text(),'Ending with')]").first
        card_text_locator.wait_for(state="visible", timeout=5000)
        actual_text = card_text_locator.inner_text()
        assert expected_last4 in actual_text, f"❌ Expected card ending with {expected_last4}, but got {actual_text}"


    def open_action_icon(self, action: str):
        container = self.page.locator(self.PAYMENT_CONTAINER)
        container.wait_for(state="visible", timeout=5000)

        if action == "delete":
            icon = self.page.locator(self.REMOVE_ICON)
            button = self.page.locator(self.DELETE_BTN)
            icon.scroll_into_view_if_needed()
            icon.hover()
            expect(icon).to_be_visible()
            button.click()
        else:
            raise ValueError("Unsupported action")


    def verify_remove_payment(self):
        img = self.page.locator(self.IMG)
        heading = self.page.locator(self.HEADING_MSG)
        message = self.page.locator(self.MESSAGE_TEXT)
        confirm_btn = self.page.locator(self.CONFIRM_DELETE_BTN)
        close_btn = self.page.locator("//button[@data-testid= 'button-cancel']")
        heading.wait_for(state="visible", timeout=5000)

        assert img.is_visible(), "❌ Missing confirmation image"
        assert heading.is_visible(), f"❌ Missing heading"
        assert message.is_visible(), f"❌ Missing message"
        assert confirm_btn.is_visible(), "❌ Confirm delete button not visible"
        assert  close_btn.is_visible(), "❌ Close button not visible"

        confirm_btn.click()
        container = self.page.locator(self.PAYMENT_CONTAINER)
        container.wait_for(state="visible", timeout=5000)


    def delete_payment(self):
        self.open_action_icon("delete")

        self.verify_remove_payment()

