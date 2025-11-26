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

        
        print(f"✅ Fascination items visible: {count}")


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
        print(f"✨ Fascination options found: {labels}")
        return labels

    def click_first(self):
        items, labels = self.get_items()
        print(f"👉 Clicking fascination: {labels[0]}")
        items.first.click()
        self.page.wait_for_timeout(600)
        return labels[0]

    def click_by_name(self, name):
        button = self.page.locator(f"{self.ITEMS}[.//span[normalize-space()='{name}']]")
        expect(button).to_be_visible()
        button.click()
        self.page.wait_for_timeout(600)

# import re
# from pages.base_page import BasePage


# class FascinationCarousel(BasePage):

#     ITEMS = "//div[contains(@class,'overflow-x-auto')]//button"

#     # ---------------------------------------------------
#     # 1. GET ALL FASCINATION ITEMS + LABELS
#     # ---------------------------------------------------
#     def _get_items(self):
#         items = self.page.locator(self.ITEMS)
#         items.first.wait_for(state="visible", timeout=15000)

#         count = items.count()
#         labels = []

#         for i in range(count):
#             text = items.nth(i).inner_text().strip()
#             labels.append(text)

#         return items, labels

#     # ---------------------------------------------------
#     # 2. DETECT LEVEL TYPE (Make / Model / Year)
#     # ---------------------------------------------------
#     def detect_level(self, labels):
#         if not labels:
#             return "unknown"

#         first = labels[0].strip()

#         # --- YEAR LEVEL ---
#         if re.fullmatch(r"\d{4}", first):
#             return "year"

#         # --- MAKE LEVEL ---
#         # Pattern: NAME(number)
#         # Example: TOYOTA(5) or BMW(2)
#         if re.fullmatch(r"[A-Za-z ]+\(\d+\)", first):
#             return "make"

#         # --- MODEL LEVEL ---
#         # Pattern: any text WITHOUT parentheses
#         # e.g., "FJ Cruiser" , "Corolla", "CAMRY"
#         if "(" not in first:
#             return "model"

#         return "unknown"

#     # ---------------------------------------------------
#     # 3. Validate level + return (level, items, labels)
#     # ---------------------------------------------------
#     def validate_current_level(self):
#         items, labels = self._get_items()
#         level = self.detect_level(labels)

#         print(f"✨ LEVEL DETECTED: {level.upper()} → {labels}")
#         return level, items, labels

#     # ---------------------------------------------------
#     # 4. Click first item helper
#     # ---------------------------------------------------
#     def click_first_item(self, items, labels):
#         label = labels[0]
#         print(f"👉 Clicking: {label}")
#         items.nth(0).click()
#         self.page.wait_for_timeout(800)
#         return label

#     # ---------------------------------------------------
#     # 5. Wait for level change
#     # ---------------------------------------------------
#     def wait_for_level_change(self, previous, timeout=6000):
#         for _ in range(timeout // 300):
#             level, items, labels = self.validate_current_level()
#             if level != previous:
#                 return level, items, labels
#             self.page.wait_for_timeout(300)

#         raise AssertionError(f"❌ Level did NOT change from {previous} within {timeout}ms")

#     # ---------------------------------------------------
#     # 6. Full Auto Flow (Make → Model → Year)
#     # ---------------------------------------------------
#     def auto_fascination_flow(self):
#         print("\n🔮 Starting Auto Fascination Flow...")

#         flow = []

#         # Detect initial level
#         level, items, labels = self.validate_current_level()

#         # ---------------- CASE 1: STARTS AT MAKE ----------------
#         if level == "make":
#             selected_make = self.click_first_item(items, labels)
#             flow.append(("Make", selected_make))
#             level, items, labels = self.wait_for_level_change("make")

#         # ---------------- CASE 2: STARTS AT MODEL ----------------
#         if level == "model":
#             selected_model = self.click_first_item(items, labels)
#             flow.append(("Model", selected_model))
#             level, items, labels = self.wait_for_level_change("model")

#         # ---------------- CASE 3: STARTS AT YEAR ----------------
#         if level == "year":
#             selected_year = self.click_first_item(items, labels)
#             flow.append(("Year", selected_year))

#         print("\n🎉 Auto Fascination Flow Completed:", flow)
#         return flow

