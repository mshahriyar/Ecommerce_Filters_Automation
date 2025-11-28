from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(str(value))

    def wait_for_url(self, url, timeout=10000):
        self.page.wait_for_url(url, timeout=timeout)

    def wait_for_visible(self, locator, timeout=10000):
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

    def wait_for_results(self):
        cards = self.page.locator("//div[@id='ad-cars-card']")
        cards.first.wait_for(state="visible", timeout=15000)
        self.page.wait_for_timeout(3000)
