from pages.base_page import BasePage

class MotorsPage(BasePage):


    CARS_CATEGORY = "https://ayshei.com/uae/ads/motors/cars"
    
    def go_to_cars(self):
        self.page.goto(self.CARS_CATEGORY)
        self.wait_for_url("https://ayshei.com/uae/ads/motors/cars")
