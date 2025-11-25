from components.kilometer_filter import KilomterFilter

def test_filters(cars_page):

    # Regional
    km = KilomterFilter(cars_page)

    min, max = km.apply(5000, 50000)
    km.validate(min, max)
    
