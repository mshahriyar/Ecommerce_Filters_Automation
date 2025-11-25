from components.region_filter import RegionalFilter

def test_filters(cars_page):

    # Regional
    region = RegionalFilter(cars_page)
    selected = region.apply(["American", "Korean", "GCC"])
    region.validate(selected)
    
