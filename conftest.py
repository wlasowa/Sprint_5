import pytest
from tests import locators
from selenium import webdriver

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(locators.DOSKA_URL)
    yield browser
    browser.quit()
