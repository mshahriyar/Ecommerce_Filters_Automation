from pages.base_page import BasePage

class MotorsPage(BasePage):


    CARS_CATEGORY = "https://portal-v2.qa.ayshei.io/uae/ads/motors/cars"
    
    def go_to_cars(self):
        self.page.goto(self.CARS_CATEGORY)
        self.wait_for_url("https://portal-v2.qa.ayshei.io/uae/ads/motors/cars")
