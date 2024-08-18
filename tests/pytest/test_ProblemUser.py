import time
import utils
import PageClasses as pc
from selenium.webdriver.remote.webelement import WebElement
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from conftest import suite_conftest

# Success credentials
username = 'problem_user'
password = 'secret_sauce'

@pytest.fixture(scope='module')
def setup_teardown(suite_conftest):
    '''Setup'''
    loginPage = pc.LoginPage(suite_conftest)
    loginPage.openLoginPage()
    
    yield loginPage


def test_problem_user(setup_teardown):
    test_case = "problem_user"
    error_list = []
    loginPage = setup_teardown
    
    '''
    ## Check Login Functionality
    - login() function has built in logic that raises exception if an error message pops up
    '''
    inventoryPage = loginPage.login(username, password)

    '''
    ## Test inventory page
    - Should sort the items accordingly
    - Should add to cart n items
    '''
    inventoryPage.sortItemsBy(utils.Constants.SORT_METHOD)
    try:
        checkedOutItems = [inventoryPage.clickItemBtn(1), inventoryPage.clickItemBtn(2)]
        removedItems = [inventoryPage.clickItemBtn(1)]
        item_count = len(checkedOutItems) - len(removedItems)
    except Exception as e:
        utils.takeScreenshot(test_case, inventoryPage.driver)
        error_list.append(f"{str(e)}")

    '''
    ## Test cart page 
    - Cart info should be same as items clicked on previous test
    '''
    cartPage = inventoryPage.checkCart()
    cart_items = cartPage.itemList 
    
    inventoryPage.logout()
    
    assert len(error_list) == 0, f"{error_list}"
  