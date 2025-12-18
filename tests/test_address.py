

import pytest
from profile.address_page import AddressPage


@pytest.fixture
def address_page(logged_in_page):
    page = AddressPage(logged_in_page)
    page.go_to_address_page()
    return page



@pytest.mark.address
def test_add_new_address(address_page):
    address_page.open_address_form()

    address_page.fill_address_form(
        first_name="John",
        last_name="Doe",
        mobile_number="0501234567",
        emirate="Abu Dhabi",
        area="Downtown",
        street="Main St",
        building="Building A",
        apt_villa_no="101",
        landmark="Near Mall"
    )

    address_page.save_address()

    address_page.verify_popup(
        heading_text="Congratulations!",
        message_text="Address added Successfully"
    )

@pytest.mark.address
def test_edit_address(address_page):
    address_page.edit_address()

    address_page.fill_address_form(
        first_name="Jane",
        last_name="Doe",
        mobile_number="0507654321",
        emirate="Dubai",
        area="Uptown",
        street="Second St",
        building="Building B",
        apt_villa_no="202",
        landmark="Near Park"
    )

    address_page.save_address()
    address_page.verify_edit_success()



@pytest.mark.address
def test_delete_address(address_page):
    address_page.delete_address()
