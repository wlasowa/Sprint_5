import pytest
import urls
from selenium import webdriver

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(urls.DOSKA_URL)
    yield browser
    browser.quit()
