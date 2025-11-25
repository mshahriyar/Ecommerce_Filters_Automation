from components.price_filter import PriceFilter

def test_filters(cars_page):

    # Price
    price = PriceFilter(cars_page)

    min_val, max_val = price.apply(100, 20000)
    price.validate(min_val, max_val)
