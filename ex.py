from selenium import webdriver
from time import sleep
import time

driver = webdriver.Chrome(r'C:\chromedriver.exe') ## webdriver 경로 설정
driver.implicitly_wait(3)  ## 주로 첫 로딩시에 쓰임.
 
driver.get('http://192.168.10.161:9090/renobit/login.do')  ## 접속 페이지
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
driver.find_element_by_xpath('//*[@id="nav"]/li[1]/a').click()
print('재난관제 이동')
time.sleep(10)
driver.find_element_by_xpath('//*[@id="a02560d1-3335-49f8-b230-e1553e25c420"]/div[1]/div[2]/li/div[2]/ul/li/ul/li[1]/span/div').click()
print('1발전처선택')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="a02560d1-3335-49f8-b230-e1553e25c420"]/div[1]/div[2]/li/div[2]/ul/li/ul/li[1]/ul/li[1]/span/div').click()
print('1보일러동선택')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="a02560d1-3335-49f8-b230-e1553e25c420"]/div[1]/div[2]/li/div[2]/ul/li/ul/li[1]/ul/li[1]/ul/li[1]/span/label').dbclick()
print('EL109900이동')















