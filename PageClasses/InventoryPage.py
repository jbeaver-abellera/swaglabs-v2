import PageClasses as pc
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert 
import time
from selenium.common.exceptions import UnexpectedAlertPresentException


class InventoryPage(pc.BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    @property
    def checkCartBtn(self):
        return self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link[data-test='shopping-cart-link']")
    @property
    def filterWebElement(self):
        return self.driver.find_element(By.CSS_SELECTOR, "select.product_sort_container") 
        
    @property
    def itemsWebElementList(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"div.inventory_item[data-test='inventory-item']" )
    
    @property
    def shoppingCartBadge(self):
        return self.driver.find_element(By.CSS_SELECTOR, "span.shopping_cart_badge[data-test='shopping-cart-badge']").text
    
    def sortItemsBy(self, visibleText):
        select = Select(self.filterWebElement)
        select.select_by_visible_text(visibleText)
        
        
    def addToCartItem(self, rank):
        addToCartBtns = self.driver.find_elements(By.XPATH, "//button[starts-with(@id,'add-to-cart-')]")
        addToCartBtn = addToCartBtns[rank]
        addToCartBtn.click()
    
    def checkCart(self):
        self.checkCartBtn.click()
        return pc.CartPage(self.driver)
   
    def clickItemBtn(self, n):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        Btn = items[n].find_element(By.CLASS_NAME, "btn_inventory")
        BtnText = Btn.text
        Btn.click()
        newBtnText = items[n].find_element(By.CLASS_NAME, "btn_inventory").text
        if newBtnText == BtnText:
            raise Exception(f"Error: Item {n} button did not change text/state")      
        return items[n]
        
        