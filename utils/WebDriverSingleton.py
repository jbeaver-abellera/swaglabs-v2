# webdriver_singleton.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverSingleton:
    _instance = None
    _driver = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebDriverSingleton, cls).__new__(cls)
            cls._driver = webdriver.Chrome()  # or any other browser driver
        return cls._instance

    @classmethod
    def get_driver(cls, isHeadless=False):
        if not cls._driver:
            chrome_options = Options()
            if isHeadless != False:
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu")
            cls._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        return cls._driver
    
    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None  # Reset the driver instance