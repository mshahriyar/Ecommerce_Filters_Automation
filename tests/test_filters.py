from components.fascination import FascinationCarousel
from components.price_filter import PriceFilter
from components.kilometer_filter import KilomterFilter
from components.year_filter import YearFilter
from components.region_filter import RegionalFilter
from components.emirates_filter import EmiratesFilter
from components.pagination import PaginationValidator


def test_filters(page, cars_page):
    price = PriceFilter(cars_page)
    km_filter = KilomterFilter(cars_page)
    year_filter = YearFilter(cars_page)
    region_filter = RegionalFilter(cars_page)
    emirates_filter = EmiratesFilter(cars_page)
    fascination = FascinationCarousel(cars_page)
    paginator = PaginationValidator(cars_page)

    # Apply filters once before traversing pages
    price_range = price.apply(100, 200000)
    selected_regions = region_filter.apply(["American", "GCC"])
    year_range = year_filter.apply(2014, 2022)
    km_range = km_filter.apply(5000, 100000)
    emirates_filter.apply()
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
