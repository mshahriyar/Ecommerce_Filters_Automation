from components.more_filters import MoreFilters
import pytest, json

def load_test_data():
    with open("testdata/more_filters.json") as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_test_data())
@pytest.mark.morefilters
def test_more_filters(cars_page, data):
    mf = MoreFilters(cars_page)
    mf.apply_all_filters()
    mf.open_first_card()
    mf.validate_overview_details(data)