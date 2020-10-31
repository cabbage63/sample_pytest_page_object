import pytest
from selenium import webdriver

@pytest.fixture(scope="function", autouse=True)
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
