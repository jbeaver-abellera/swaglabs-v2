import PageClasses as pc
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


class CartPage(pc.BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
            
    @property
    def itemList(self):
        return self.driver.find_elements(By.CLASS_NAME, "item_pricebar")

    def goBack(self):
        back_button = self.driver.find_elements(By.XPATH, "//*[@id='continue-shopping']")
        back_button.click()
        return pc.InventoryPage(self.driver)
    
    def checkOut(self):
        checkout_button = self.driver.find_element(By.XPATH, "//*[@id='checkout']")
        checkout_button.click()
        try:
            error_message = self.driver.find_elemt(By.CLASS_NAME, "error-message-container error")
            print("Error: Cannot checkout. Please see if there are issues on the entered information")
        except:
            return pc.CheckOutInfoPage(self.driver)