import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-gb")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    #print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    #print("\nquit browser..")
    browser.quit()
    #return user_language