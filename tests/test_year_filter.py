from components.year_filter import YearFilter


def test_filters(cars_page):


    # Year
    year = YearFilter(cars_page)
    y1, y2 = year.apply(2014, 2022)
    year.validate(y1, y2)

    
