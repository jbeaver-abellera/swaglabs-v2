import PageClasses as pc
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


class OrderSuccessPage(pc.BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    @property
    def message(self):
        return self.driver.find_element(By.ID, "checkout_complete_container").text

    @property
    def homeBtn(self):
        return self.driver.find_element(By.XPATH, "//*[@id='back-to-products']")


    def goHome(self):
        self.homeBtn.click()
        return pc.InventoryPage(self.driver)