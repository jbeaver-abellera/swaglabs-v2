import PageClasses as pc
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

class LoginPage(pc.BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    @property
    def usernameField(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input.input_error.form_input[data-test='username'][id='user-name'][name='user-name'][placeholder='Username']")
    
    @property
    def passwordField(self):
        return self.driver.find_element(By.XPATH, '//*[@id="password"]')
    
    @property
    def loginBtn(self):
        return self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

    @property
    def loginErrorMessage(self):
        try:
            return self.driver.find_element(By.XPATH, '//h3[@data-test="error"]')
        except NoSuchElementException:
            return None
    
    def openLoginPage(self):
        self.navigateToHome()
    
    def login(self, username, password):
        self.usernameField.send_keys(username)
        self.passwordField.send_keys(password)
        self.loginBtn.click()
        try:
            #TO DO: wait until
            errorMessage = self.driver.find_element(By.CSS_SELECTOR, '[data-test="error"]').text
            raise Exception(f"{errorMessage}")
        except NoSuchElementException:
            return pc.InventoryPage(self.driver)
    
    # def getLoginMessage(self): 
    #     pass   
        
        