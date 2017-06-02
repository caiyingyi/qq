# coding:utf-8
__author__ = 'Windows'

from selenium import webdriver
import time
import os

def init(driver,qq):
    #判断是否需要登录
    try:
        driver.find_element_by_class_name("login_wrap")
        a = True
    except:
        a = False

    #模拟登录
    if a == True:
        driver.switch_to.frame("login_frame")
        driver.find_element_by_id("switcher_plogin").click()
        driver.find_element_by_id("u").clear()
        driver.find_element_by_id("u").send_keys("qq号码")
        driver.find_element_by_id("p").clear()
        driver.find_element_by_id("p").send_keys("qq密码")
        driver.find_element_by_id("login_button").click()
        time.sleep(5)
        print "ok"

def get_shuoshuo(driver):
    #获取说说的文字内容和时间
    driver.implicitly_wait(20)
    driver.switch_to.frame("app_canvas_frame")
    content = driver.find_elements_by_class_name("content")
    #stime = driver.find_elements_by_css_selector(".c_tx.c_tx3.goDetail")
    stime = driver.find_elements_by_xpath("//div[@class='box bgr3']/div[@class='ft']/div[@class='info']/span[@class='c_tx3']/a")
    for con,sti in zip(content,stime):
        print u"时间是:"+sti.text
        print u"内容是:"+con.text
        print u"======================================="

    #获取cookie
    cookie = driver.get_cookies()
    cookie_dict = []
    for c in cookie:
        ck = "{0}={1}".format(c["name"],c["value"])
        cookie_dict.append(ck)
    print cookie_dict

#初始化webdriver对象
#driver = webdriver.Firefox(executable_path="D:\Program Files\geckodriver\geckodriver.exe")
#driver = webdriver.PhantomJS(executable_path="D:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe")

#chromedriver = "C:/Users/Windows/AppData/Local/Google/Chrome/Application/chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = chromedriver
#driver = webdriver.Chrome(chromedriver)

driver = webdriver.PhantomJS(executable_path=r"D:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.maximize_window()

#向页面发送请求
qq = "即将偷窥的QQ号"
driver.get("http://user.qzone.qq.com/{0}/taotao".format(qq))
time.sleep(5)
init(driver,qq)
#get_shuoshuo(driver)
#翻页
for c in range(0,53):
    get_shuoshuo(driver)
    path = "pager_next_{0}".format(c)
    print path
    driver.find_element_by_id(path).click()
    time.sleep(5)
    driver.switch_to.default_content()

driver.close()
driver.quit()