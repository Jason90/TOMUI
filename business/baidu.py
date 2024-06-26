from page.main import MainPage
from page.login import LoginPage
from selenium import webdriver


# 实例化浏览器驱动
driver = webdriver.Chrome()
driver.maximize_window()

# 实例化百度页面
main_page = MainPage(driver)
login_page = LoginPage(driver)

# 百度主页查询
def search(keyword):
    main_page.navigate()
    main_page.search(keyword)

# 进入登录页面
def login(username, password):
    main_page.navigate()
    main_page.show_login_page()
    
    login_page.login(username,password)

# 关闭浏览器 
def quit():
    driver.quit()

