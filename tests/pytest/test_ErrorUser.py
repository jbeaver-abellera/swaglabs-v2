import utils
import PageClasses as pc
from selenium.webdriver.remote.webelement import WebElement
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from conftest import suite_conftest
from selenium.webdriver.common.alert import Alert 
import time

# Success credentials
username = 'error_user'
password = 'secret_sauce'

@pytest.fixture(scope='module')
def setup_teardown(suite_conftest):
    '''Setup'''
    loginPage = pc.LoginPage(suite_conftest)
    loginPage.openLoginPage()
    
    yield loginPage
    

def test_error_user(setup_teardown):
    error_list = []
    test_case = "error_user"
    loginPage = setup_teardown
    x = 9999
    
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
        checkedOutItems = [inventoryPage.clickItemBtn(1), inventoryPage.clickItemBtn(2), inventoryPage.clickItemBtn(3)]
        removedItems = [inventoryPage.clickItemBtn(3)]
        item_count = len(checkedOutItems) - len(removedItems)
    except UnexpectedAlertPresentException as e:
        utils.takeScreenshot(test_case, inventoryPage.driver)
        error_list.append(f"Unexpected Alert Error: {e.alert_text}")
        item_count = 0
    except Exception as e:
        error_list.append(f"{str(e)}")
        item_count = 2
    
    '''
    ## Test cart page 
    - Cart info should be same as items clicked on previous test
    '''
    cartPage = inventoryPage.checkCart()
    cart_items = cartPage.itemList 
    if len(cart_items) != item_count:
        utils.takeScreenshot(test_case, cartPage.driver)
        error_list.append(f"Error on cart page. Items in cart not equal to clicked items")
       
    '''
    ## Test on shipping information 
    '''
    checkOutInfoPage = cartPage.checkOut()
    firstName = "Swagger"
    lastName = "User"
    postalCode = "1234"
    checkOutInfoPage.enterInfo(firstName=firstName,
                                lastName=lastName,
                                postalCode=postalCode)

    '''
    confirm() function has built in logic that raises exception if an error message pops up
    '''
    checkOutFinalPage = checkOutInfoPage.confirm()

    '''
    ## Test final order info
    - Items should be equal to added items on inventory page
    - TO DO: confirm correct checkout info (Name, Address, Payment Method, Total)
    '''
    checkOutFinalItemList = checkOutFinalPage.itemList
    if len(checkOutFinalItemList) != item_count:
        utils.takeScreenshot(test_case, checkOutFinalPage.driver)
        error_list.append("Error on final info page. Items in final info not equal to clicked items")
    
    '''
    ## Go to final / result page
    Checks if order was successful
    '''
    try:
        orderSuccessPage = checkOutFinalPage.finish()
    except Exception as e:
        utils.takeScreenshot(test_case, orderSuccessPage.driver)
        error_list.append(f"{str(e)}")
        checkOutFinalPage.logout()
        assert False, f"{error_list}"
    
    orderMessage = orderSuccessPage.message
    '''
    ## Final test
    - Should have a "Thank you" or successful message
    '''
    if "Thank you" not in orderMessage:
        utils.takeScreenshot(test_case, orderSuccessPage.driver)
        error_list.append("Error on end page. Order not successful")
    
    orderSuccessPage.logout()
    assert len(error_list) == 0, f"{error_list}"
    
    
