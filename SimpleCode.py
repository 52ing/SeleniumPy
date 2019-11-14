from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(r'C:\chromedriver.exe') ## webdriver 경로 설정
driver.implicitly_wait(3)  ## 주로 첫 로딩시에 쓰임.
 
driver.get('http://192.168.10.161:10277/renobit/visual.do#/viewer')  ## 접속 페이지
#driver.get('https://nid.naver.com/nidlogin.login')

print(driver.title)

driver.find_element_by_xpath('//*[@id="tbLogin"]/div/div[2]/div[2]/div[1]/label').click()
driver.find_element_by_name('idInput').send_keys('admin') ## 계정
driver.find_element_by_name('pwInput').send_keys('admin') ## 계정 비번
driver.find_element_by_xpath('//*[@id="tbLogin"]/div/div[2]/div[4]').click()

print('로그인 완료')
#try:
#   driver.find_element_by_xpath('//*[@id="tbLogin"]/div/div[2]/div[2]/div[1]/label').click()
#   driver.find_element_by_name('idInput').send_keys('admin') ## 계정
#   driver.find_element_by_name('pwInput').send_keys('admin') ## 계정 비번
#   driver.find_element_by_xpath('//*[@id="tbLogin"]/div/div[2]/div[4]').click()
#   result='Pass'
#except Exception as e:
#   print("Fail")
#   print(e) # hi
#   result='Fail'
   
#excel = win32com.client.Dispatch("Excel.Application")
#excel.Visible = True
#wb = excel.Workbooks.Open('C:test.xlsx') # excel 불러오는 코드.

time.sleep(15) ## 코드 끝난뒤 대기 시간
driver.find_element_by_xpath('//*[@id="8a5ee369-50eb-4329-9492-314806ed85b4"]/div/div[1]/div[2]/div/ul/li[3]/span/div').click()
print('하위메뉴 선택') ## 처음클릭
target = driver.find_element_by_xpath('//*[@id="8a5ee369-50eb-4329-9492-314806ed85b4"]/div/div[1]/div[2]/div/ul/li[3]/ul/li[1]/span/label')
actionChains = ActionChains(driver)
actionChains.double_click(target).perform()
print('Fire 선택')
time.sleep(1)
target = driver.find_element_by_xpath('//*[@id="8a5ee369-50eb-4329-9492-314806ed85b4"]/div/div[1]/div[2]/div/ul/li[3]/ul/li[2]/span/label')
actionChains = ActionChains(driver)
actionChains.double_click(target).perform()
print('Fire 선택') ## 더블클릭
