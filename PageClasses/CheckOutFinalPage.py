import PageClasses as pc
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class CheckOutFinalPage(pc.BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
            
    @property
    def itemList(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")

    def finish(self):
        finishBtn = self.driver.find_element(By.ID, "finish")
        finishBtn.click()
        try:
            finishBtn.is_displayed()
            raise Exception("Failure on checkout finalization page. Cannot finish order")    
        except NoSuchElementException as e:
            return pc.OrderSuccessPage(self.driver)
        except StaleElementReferenceException as e:
            return pc.OrderSuccessPage(self.driver)
    
    def cancel(self):
        cancelBtn = self.driver.find_element(By.XPATH, "//*[@id='cancel']")
        cancelBtn.click()
        return pc.CheckOutInfoPage(self.driver)