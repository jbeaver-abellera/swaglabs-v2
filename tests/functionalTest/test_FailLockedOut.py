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
username = 'locked_out_user'
password = 'secret_sauce'

@pytest.fixture(scope='module')
def setup_teardown(suite_conftest):
    '''Setup'''
    loginPage = pc.LoginPage(suite_conftest)
    loginPage.openLoginPage()
    
    yield loginPage

# @pytest.mark.xfail(raises=Exception, strict=True)
@pytest.mark.Error
def test_locked_out_user(setup_teardown):
    error_list = []
    loginPage = setup_teardown
    
    '''
    ## Check Login Functionality
    - login() function has built in logic that raises exception if an error message pops up
    '''
    try:
        inventoryPage = loginPage.login(username, password)
        inventoryPage.navigateToHome()
        raise Exception(f"Test fail. User {username} was not locked out. This user is expected to be locked out")
    except Exception as e:
        loginPage.navigateToHome()
        

    
    