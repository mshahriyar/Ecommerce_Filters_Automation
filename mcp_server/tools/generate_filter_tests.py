def generate_filter_test(category: str):
    template = f"""
import pytest
from components.more_filters import MoreFilters

@pytest.mark.filters
def test_{category.lower()}_filters(page, config):
    mf = MoreFilters(page)
    mf.apply_all_filters()

    mf.open_first_card()
    mf.validate_overview_details(config["test_data"]["{category.lower()}"])
    """
    return template
