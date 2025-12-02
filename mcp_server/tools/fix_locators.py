def fix_locators(failure_log: str):
    suggestions = []

    if "TimeoutError" in failure_log:
        suggestions.append("Increase wait time or use scroll_into_view_if_needed().")

    if "not visible" in failure_log:
        suggestions.append("Locator exists but hidden — ensure section is expanded.")

    if "strict mode violation" in failure_log:
        suggestions.append("Use nth(0) or first() to target a specific element.")

    return "\n".join(suggestions)
