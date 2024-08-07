import PageClasses as pc
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException



class CheckOutInfoPage(pc.BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    @property
    def firstNameField(self):
        return self.driver.find_element(By.XPATH, "//*[@id='first-name']")

    @property
    def lastNameField(self):
        return self.driver.find_element(By.XPATH, "//*[@id='last-name']")
    
    @property
    def postalCodeField(self):
        return self.driver.find_element(By.XPATH, "//*[@id  ='postal-code']")

    @property
    def continueBtn(self):
        return self.driver.find_element(By.XPATH, "//*[@id  ='continue']")

    @property
    def cancelBtn(self):
        return self.driver.find_element(By.XPATH, "//*[@id  ='cancel']")


    def enterInfo(self, firstName: str, lastName: str, postalCode: str):
        self.firstNameField.send_keys(firstName)
        self.lastNameField.send_keys(lastName)
        self.postalCodeField.send_keys(postalCode)
        
    def confirm(self):
        self.continueBtn.click()
        try:
            errorMessage = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
            raise Exception(f"{errorMessage}")
        except NoSuchElementException:
            return pc.CheckOutFinalPage(self.driver)
        

    def cancel(self):
        self.cancelBtn.click()
        return pc.CartPage(self.driver) 
        
        