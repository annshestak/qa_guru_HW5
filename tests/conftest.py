import pytest
from selene import browser, be, have


@pytest.fixture(autouse=True)
def open_browser():
    browser.config.base_url ='https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1000
    browser.config.window_height = 1000

    yield

    browser.quit()
