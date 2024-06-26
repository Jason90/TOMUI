from page.base import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class MainPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver, 'https://www.baidu.com') 
        self.search_box = (By.ID, "kw")
        self.search_button = (By.ID, "su")
        self.login_button = (By.ID, "s-top-loginbtn")

    def navigate(self):
        self.driver.get(self.url)

    def search(self, keyword):
        self.input_text(self.search_box, keyword)
        self.click_element(self.search_button)

        
    def show_login_page(self):
        self.click_element(self.login_button)

   