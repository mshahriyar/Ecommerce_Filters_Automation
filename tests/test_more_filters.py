from components.more_filters import MoreFilters
import pytest


test_data = {
    "make": "AUDI",
    "model": "A6",
    "trim": "40 TFSI",
    "year": "2025",
    "kilometers": "121000",
    "regional_spec": "GCC",
    "body_type": "Sedan",
    "fuel_type": "Gasoline",
    "transmission": "Automatic",
    "exterior_color": "Black",
    "steering_side": "Left Hand",
    "warranty": "No",
    "doors": "4",
    "body_condition": "Excellent",
    "cylinders": "4",
    "seats": "5",
    "insured": "No",
}

@pytest.mark.morefilters
def test_more_filters(cars_page):
    mf = MoreFilters(cars_page)
    mf.apply_all_filters()
    mf.open_first_card()
    mf.validate_overview_details(test_data)
