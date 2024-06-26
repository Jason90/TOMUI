from page.base import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver, 'https://www.baidu.com/login') 
        self.username_input = (By.ID, "TANGRAM__PSP_11__userName")
        self.password_input = (By.ID, "TANGRAM__PSP_11__password")
        self.login_button = (By.ID, "TANGRAM__PSP_11__submit")
        self.protocal_checkbox = (By.ID, "TANGRAM__PSP_11__isAgree")

    def login(self, username, password):
        self.input_text(self.username_input, username)
        self.input_text(self.password_input, password)
        self.click_element(self.protocal_checkbox)
        self.click_element(self.login_button)

        
   