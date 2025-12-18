import pytest
from profile.payment_page import PaymentPage


@pytest.fixture
def payment_page(logged_in_page):
    page = PaymentPage(logged_in_page)
    page.go_to_payment_page()
    return page



@pytest.mark.address
def test_(payment_page):
    payment_page.open_payment_form()

    payment_page.fill_payment_form(
        card_holder_name="John Doe",
        card_number="4242424242424242",
        expiry="1127",
        cvc="111"
    )

    payment_page.verify_add_payment_content()
    payment_page.save_payment_card()
    print('✅ Payment method added successfully!')
    payment_page.click_close_success_popup()
    


# @pytest.mark.address
# def test_delete_payment(payment_page):
#     payment_page.delete_payment()
#     print('✅ Payment method deleted successfully!')
