from components.fascination import FascinationCarousel
from components.price_filter import PriceFilter
from components.kilometer_filter import KilomterFilter
from components.year_filter import YearFilter
from components.region_filter import RegionalFilter
from components.emirates_filter import EmiratesFilter
from components.pagination import PaginationValidator
from components.sorting import Sorting
from components.type_of_seller import TypeOfSeller
from components.more_filters import MoreFilters
import pytest, json

def test_filters(page, cars_page):
    price = PriceFilter(cars_page)
    km_filter = KilomterFilter(cars_page)
    year_filter = YearFilter(cars_page)
    region_filter = RegionalFilter(cars_page)
    emirates_filter = EmiratesFilter(cars_page)
    fascination = FascinationCarousel(cars_page)
    paginator = PaginationValidator(cars_page)
    seller_type = TypeOfSeller(cars_page)

    print("\n--- Applying Multiple Filters ---")
    emirates_filter.apply()
    price_range = price.apply(100, 200000)
    selected_regions = region_filter.apply(["American", "GCC"])
    year_range = year_filter.apply(2014, 2022)
    km_range = km_filter.apply(5000, 100000)

    cars_page.wait_for_timeout(2000)  

    def validate_all_filters():
        price.validate(*price_range)
        year_filter.validate(*year_range)
        region_filter.validate(selected_regions)
        km_filter.validate(*km_range)
        emirates_filter.validate()

    paginator.validate_all_pages(
        validate_filters_fn=validate_all_filters,
        validate_fascination_fn=fascination.validate_fascination,
        max_pages=3,
    )

# def test_type_of_seller(cars_page):
#     seller_type = TypeOfSeller(cars_page)
#     seller_type.select_seller_type("Dealer")
#     seller_type.validate_seller_type("Dealer")
#     seller_type.select_seller_type("Owner")
#     seller_type.validate_seller_type("Owner")

def test_sorting(cars_page):
    sort = Sorting(cars_page)

    sort.apply("Price: Low to High")
    prices = sort.get_price_sort_by()
    assert prices == sorted(prices), "❌ Prices are not sorted Low to High after applying filters!"


    sort.apply("Price: High to Low")
    prices = sort.get_price_sort_by()
    assert prices == sorted(prices, reverse=True), "❌ Prices are not sorted High to Low after applying filters!"

    sort.apply("Kilometers: Low to High")
    sorted_kms = sort.get_km_sort_by()
    assert sorted_kms == sorted(sorted_kms), "❌ Kilometers are not sorted Low to High!"
 
    sort.apply("Kilometers: High to Low")
    sorted_kms = sort.get_km_sort_by()
    assert sorted_kms == sorted(sorted_kms, reverse=True), "❌ Kilometers are not sorted High to Low after applying filters!"
  
    sort.apply("Year: Low to High")
    sorted_years = sort.get_year_sort_by()
    assert sorted_years == sorted(sorted_years), "❌ Years are not sorted by Low to High!"
  
    sort.apply("Year: High to Low")
    sorted_years = sort.get_year_sort_by()
    assert sorted_years == sorted(sorted_years, reverse=True), "❌ Years are not sorted by High to Low!"

def test_fascination_flow(cars_page):
    fascination = FascinationCarousel(cars_page)

    make_labels = fascination.validate_visible()
    assert len(make_labels) > 0, "❌ No Make list shown"
    fascination.click_first()
    cars_page.wait_for_timeout(3000)

    model_labels = fascination.validate_visible()
    assert len(model_labels) > 0, "❌ No model list shown after selecting a Make!"
    fascination.click_first()
    cars_page.wait_for_timeout(3000)
    

    year_labels = fascination.validate_visible()
    assert len(year_labels) > 0, "❌ No year list shown after selecting a Model!"
    fascination.click_first()



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

    