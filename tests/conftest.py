import pytest
import utils
from selenium import webdriver
from selenium.webdriver import ChromeOptions

def pytest_addoption(parser):
    parser.addoption(
        "--isHeadless", action="store", default="y", help="Switch between headless or not"
    )
  
@pytest.fixture(scope="session")
def headlessOpt(request):
    return request.config.getoption("--isHeadless")

@pytest.fixture(scope="session")
def suite_conftest(headlessOpt):
    isHeadless = True if headlessOpt == "y" else False
    driver = utils.WebDriverSingleton.get_driver(isHeadless=isHeadless)
         
    yield driver
    
    utils.WebDriverSingleton.quit_driver()
    
    