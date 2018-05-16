from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
# driver.get("https://www.baidu.com/") 

# 学习视频内容
input=driver.find_element_by_css_selector("#kw")
input.send_keys("hello")
input.clear()

driver.find_element_by_class_name("soutu-btn").click()
driver.find_element_by_class_name("upload-pic").send_keys("C:/Users/HZW/Desktop/picture/多种多样的海洋动物图片.jpg")

driver.find_element_by_xpath('//*[@id="kw"]').send_keys("hello")
driver.find_element_by_id("kw").send_keys("hello")
driver.find_element_by_name("wd").send_keys("hello")
driver.find_element_by_class_name("s_ipt").send_keys("hello")
driver.find_element_by_link_text("新闻").click()
driver.find_element_by_partial_link_text("闻").click()

driver.get("file:///E:/VScode.py/index.html")    # 结合index.html
driver.find_element_by_tag_name("a").click()   #标签名称，因为一个页面重复的标签很多，所以该方法用的很少

urls=[]
eles=driver.find_elements_by_class_name("mnav")
print(len(eles),driver.current_url)
for ele in eles:
    # print(ele.text)
    # ele.click()    # 只能点击到第一个，因为页面url已经改变，所以要点一下返回一下
    # driver.back()      # 此时返回到的页面不是原始页面，所以也不会继续点击下一个

    href = ele.get_attribute("href")
    name = ele.get_attribute("name")
    print("text : ",ele.text,"href :",href,"name ：",name)
    urls.append(href)
    

time.sleep(20)

driver.quit()


# 登录百度
driver.get("https://www.baidu.com/")   
# driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()     # xpath语法
# driver.find_element_by_css_selector('#TANGRAM__PSP_10__footerULoginBtn').click()          # css selector

driver.find_element_by_xpath('//*[@id="u1"]/a[last()-2]').click()     # 当存在多个重复值，会默认取第一个

time.sleep(1)
driver.find_element_by_class_name('tang-pass-footerBarULogin').click()

time.sleep(1)  # 代码运行比界面快，在窗口没有加载完全时进行点击就会找不到element
inputUserName = driver.find_element_by_id('TANGRAM__PSP_10__userName')

inputUserName.clear()
inputUserName.send_keys('18699498912')

inputPasswd = driver.find_element_by_id('TANGRAM__PSP_10__password')
inputPasswd.clear()
inputPasswd.send_keys("shawty0216")

driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
time.sleep(15)
driver.quit()


# CNode登录、发布话题、提交
driver.get("http://118.31.19.120:3000/signin")
driver.find_element_by_class_name("input-xlarge").send_keys("testuser6")     # 登录
driver.find_element_by_id("pass").send_keys("123456")
driver.find_element_by_class_name("span-primary").click()
# driver.find_element_by_class_name("span-primary").submit()   # 等同于上面两行，输入密码后直接提交

driver.find_element_by_class_name("span-success").click()      # 点击发布话题
# driver.find_element_by_css_selector(".span-success").click()   # 含义同上

driver.find_element_by_id("tab-value").click()        # 选择板块
driver.find_element_by_xpath('//*[@id="tab-value"]/option[3]').click()
driver.find_element_by_id("title").send_keys("20180513")      # 输入标题

# 此方法行不通
input_content = driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[2]/div[6]/div[1]/div/div/div/div[3]/pre')
input_content.click()
input_content.send_keys("123")

# 用action
input_content = driver.find_element_by_css_selector(".CodeMirror-code")     # 输入文本
ActionChains(driver).move_to_element(input_content).click().send_keys("lalala").perform()

ActionChains(driver).move_to_element(input_content).click().key_down(Keys.CONTROL).send_keys("b").key_up(Keys.CONTROL).perform()   # 快捷键，此处为ctrl+b
ActionChains(driver).move_to_element(input_content).click().send_keys("hellowlrodl").perform()
ActionChains(driver).click(input_content).send_keys_to_element(input_content,"dsdsdsdsdsdsdsds").perform()
# ActionChains(driver).key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).send_keys('老困啦，灵魂出窍。。。').perform()  # 含义同上三行

driver.find_element_by_class_name("span-primary").click()    # 点击提交


# 阿里云拖拽控件（iframe）
driver.get("https://account.aliyun.com/register/register.htm?spm=5176.8142029.388261.7.e9396d3eW4tG48&qrCodeFirst=false&oauth_callback=https%3A%2F%2Fwww.aliyun.com%2F")
driver.switch_to_frame("alibaba-register-box")      # 若没有这句运行会报错，显示找不到这个element,原因在于iframe
kongjian = driver.find_elements_by_id("nc_1_n1z")             
ActionChains(driver).move_to_element(kongjian).drag_and_drop_by_offset(kongjian,500,0).perform()  


# 一些其他方法
from os import path
d = path.dirname(__file__)
xinwen = path.join(d,'xinwen.jpg')
index = path.join(d,'shouye.jpg')

driver.get("https://www.baidu.com/")
driver.maximize_window()

driver.find_element_by_link_text('新闻').click()
time.sleep(1)
driver.save_screenshot(xinwen)

driver.back()
time.sleep(1)
driver.save_screenshot(index)

driver.forward()
driver.minimize_window()    # 估计是BUG
driver.close()

driver.title
driver.current_url
driver.page_source

# 作业：删除一个帖子，需要用到switch_to_frame

