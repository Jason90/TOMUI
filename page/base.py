from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self._element_cache = {}

    def navigate(self,url):
        self.driver.get(url)
    
    def navigate(self):
        self.driver.get(self.url)
    
    #缓存元素，防止重新定位多次，需考虑不同页面locator相同，会不会导致缓存出错？
    def find_element(self, locator):
        if locator not in self._element_cache:
            self._element_cache[locator] = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self._element_cache[locator]

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()