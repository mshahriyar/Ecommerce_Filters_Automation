from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL = 'input[type="email"]'
    PASSWORD = 'input[type="password"]'
    SUBMIT_BTN = 'button[type="submit"]'

    def open(self, base_url):
        self.page.goto(base_url)

    def login(self, email, password):
        self.fill(self.EMAIL, email)
        self.fill(self.PASSWORD, password)
        self.click(self.SUBMIT_BTN)
        self.wait_for_url("https://ayshei.com/uae/ads")
