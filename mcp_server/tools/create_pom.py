def create_pom_class(name: str, fields: dict):
    locators = "\n".join([
        f"    {field.upper()} = \"{locator}\""
        for field, locator in fields.items()
    ])

    class_body = f"""
from pages.base_page import BasePage

class {name}(BasePage):
{locators}

    def apply_filters(self, data):
        for key, value in data.items():
            locator = getattr(self, key.upper())
            self.click(locator)

    """
    return class_body
