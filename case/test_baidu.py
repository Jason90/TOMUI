from business import baidu

#todo 继承自unittest？ clearup里管理浏览器。
def test_search():
    baidu.search('selenium')
    # baidu.main_page.verify()
    #todo:如何校验查询结果？
    
    # baidu.quit()

    assert True,"Pass"


def test_login():
    baidu.login("13811088178","password")
    
    # baidu.quit()
    
    assert True,"Pass"
