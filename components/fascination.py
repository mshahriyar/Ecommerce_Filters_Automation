import re

import pytest
from pages.base_page import BasePage
from playwright.sync_api import expect

class FascinationCarousel(BasePage):

    ITEMS = "//div[contains(@class,'overflow-x-auto')]//button"

    def wait_for_fascination(self):
        items = self.page.locator(self.ITEMS)
        items.first.wait_for(state="visible", timeout=15000)
        return items


    def validate_fascination(self):
        items = self.wait_for_fascination()
        count = items.count()

        self.wait_for_results()

        assert count > 0, "❌ No fascination items found!"

        for i in range(count):
            el = items.nth(i)
            text = el.inner_text().strip()
            assert el.is_visible(), f"❌ Fascination item '{text}' is NOT visible!"


    def get_items(self):
        items = self.page.locator(self.ITEMS)
        items.first.wait_for(state="visible", timeout=10000)
        count = items.count()
        assert count > 0, "❌ No fascination items found!"

        labels = []
        for i in range(count):
            txt = items.nth(i).inner_text().strip()
            labels.append(txt)

        return items, labels

    def validate_visible(self):
        items, labels = self.get_items()
        return labels

    def click_first(self):
        items, labels = self.get_items()
        items.first.click()
        self.page.wait_for_timeout(600)
        return labels[0]

    def click_by_name(self, name):
        button = self.page.locator(f"{self.ITEMS}[.//span[normalize-space()='{name}']]")
        expect(button).to_be_visible()
        button.click()
        self.page.wait_for_timeout(600)
