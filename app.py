from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from case import test_baidu
from page.main import MainPage
# from business.baidu import baidu
import business.baidu
#from app import ui_test

# import sys
# import os
# path=os.getcwd() 
# sys.path.append(path) #用于pytest自动发现测试案例，跨包引用




if __name__ == "__main__":
    
    test_baidu.test_search()
    test_baidu.test_login()
    # business.baidu.search("selenium")
    # business.baidu.login("13811088178","Zongheng")
    # ui_act()
    
    # baidu=MainPage()
    # baidu.search("selenium")
    
    # ui_test()
    
    pass

