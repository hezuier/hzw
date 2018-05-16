from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("http://118.31.19.120:3000/signin")
driver.find_element_by_class_name("input-xlarge").send_keys("testuser6")     # 登录
driver.find_element_by_id("pass").send_keys("123456")
driver.find_element_by_class_name("span-primary").click()

driver.find_element_by_class_name("span-success").click()      # 点击发布话题

driver.find_element_by_id("tab-value").click()        # 选择板块
driver.find_element_by_xpath('//*[@id="tab-value"]/option[3]').click()
driver.find_element_by_id("title").send_keys("20180517")      # 输入标题

input_content = driver.find_element_by_css_selector(".CodeMirror-code")     # 输入文本
ActionChains(driver).move_to_element(input_content).click().send_keys("lalala").perform()

driver.find_element_by_class_name("span-primary").click()    # 点击提交

time.sleep(2)

driver.find_element_by_class_name("delete_topic_btn").click()    # 点击删除
time.sleep(2)

driver.switch_to_alert().accept()
