import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self):
        self.driver = utils.WebDriverSingleton.get_driver(isHeadless=False)
        
    def navigateToHome(self):
        self.driver.get(utils.Constants.WEBSITE_URL)
    
    @property
    def menuBtn(self):
        return self.driver.find_element(By.ID, "react-burger-menu-btn")
    
    def logout(self):
        self.menuBtn.click()
        resetBtn =  WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "reset_sidebar_link")))  
        resetBtn.click()
        logoutBtn =  WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logoutBtn.click() 
         
        