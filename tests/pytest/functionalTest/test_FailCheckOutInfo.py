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
username = 'standard_user'
password = 'secret_sauce'

@pytest.fixture(scope='module')
def setup_teardown(suite_conftest):
    '''Setup'''
    loginPage = pc.LoginPage(suite_conftest)
    loginPage.openLoginPage()
    
    yield loginPage

@pytest.mark.Error
def test_failCheckOutInfo(setup_teardown):
    error_list = []
    test_case = "Failed_Checkout_Info"
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
    - Should remove 1 item
    '''
    inventoryPage.sortItemsBy(utils.Constants.SORT_METHOD)
    try: 
        checkedOutItems = [inventoryPage.clickItemBtn(1)]
        item_count = len(checkedOutItems)
    except Exception as e:
        error_list.append(f"{str(e)}")
        item_count = 1
        pass

    cartPage = inventoryPage.checkCart()
       
    '''
    ## Test on check out information 
    '''
    checkOutInfoPage = cartPage.checkOut()
    firstName = "Swagger"
    lastName = ""
    postalCode = "7332"
    checkOutInfoPage.enterInfo(firstName=firstName,
                                lastName=lastName,
                                postalCode=postalCode)

    '''
    confirm() function has built in logic that raises exception if an error message pops up
    '''
    try:
        checkOutFinalPage = checkOutInfoPage.confirm()
        error_list.append(f"Function error on Info Page. No error message displayed. Expected to have message for incomplete info")
        assert len(error_list) == 0, f"{error_list}"
        checkOutFinalPage.logout()
    except Exception as e:
        assert len(error_list) == 0, f"{error_list}"
        checkOutInfoPage.logout()
    