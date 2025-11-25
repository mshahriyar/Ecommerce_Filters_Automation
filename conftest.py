import sys, os
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from playwright.sync_api import sync_playwright
from config.config import load_config
from pages.login_page import LoginPage
from pages.motors_page import MotorsPage


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local")


@pytest.fixture(scope="session")
def config(pytestconfig):
    env = pytestconfig.getoption("env")
    return load_config(env)


# -------------------------
# BROWSER + CONTEXT FIXTURE
# -------------------------
@pytest.fixture(scope="function")
def context():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)    # remove slow_mo for faster exit
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


# -------------------------
# PAGE FIXTURE (corrected)
# -------------------------
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    return page


# -------------------------
# AUTHENTICATED CARS PAGE FIXTURE
# -------------------------
@pytest.fixture(scope="function")
def cars_page(page, config):
    """Login once and land on the Cars listing page for each test."""
    login = LoginPage(page)
    login.open(config["base_url"])
    login.login(config["email"], config["password"])

    motors = MotorsPage(page)
    motors.go_to_cars()
    return page


# -------------------------
# SCREENSHOT ON FAILURE
# -------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store test report attributes on the item for later inspection."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    """
    Capture a screenshot when a test using a Playwright page fails.
    Depends on the page fixture so the browser is still alive when we capture.
    Screenshots are saved under reports/screenshots and attached to pytest-html.
    """
    yield

    rep = getattr(request.node, "rep_call", None)
    if not rep or not rep.failed:
        return

    screenshots_dir = Path("reports") / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    name = request.node.nodeid.replace("::", "__").replace("/", "_")
    file_path = screenshots_dir / f"{name}.png"

    image_bytes = page.screenshot(path=str(file_path), full_page=True)

    html_plugin = request.config.pluginmanager.getplugin("html")
    if html_plugin:
        try:
            from pytest_html import extras

            extra = getattr(rep, "extra", [])
            extra.append(extras.png(image_bytes, mime_type="image/png"))
            rep.extra = extra
        except Exception:
            # Avoid blocking test teardown if pytest-html is unavailable.
            pass

    print(f"[screenshot saved] {file_path}")
