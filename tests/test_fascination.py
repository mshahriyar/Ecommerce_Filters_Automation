from components.fascination import FascinationCarousel


def test_filters(cars_page):
    FascinationCarousel(cars_page).validate_fascination()
