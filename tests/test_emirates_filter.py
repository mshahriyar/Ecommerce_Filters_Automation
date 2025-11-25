from components.emirates_filter import EmiratesFilter

def test_filters(cars_page):

    # Regional
    emirate = EmiratesFilter(cars_page)

    emirate.apply()
    emirate.validate()
    
