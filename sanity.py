import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import sys
import time

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4723/wd/hub',
    desired_capabilities={
      "platformName": "Android",
      "platformVersion": "7.0",
      "deviceName": "BeWhy",
      "app": "C:\\apk\\app-internal-debug.apk",
      "automationName": "Appium",
      "appPackage": "com.allbit.internal.debug",
      "udid": "2854134912017ece", # BeWhy 9TSDU17B07000371
      "noReset": "true",
     "appActivity": "com.allbit.SplashActivity"
})
#첫 스플래쉬
driver.implicitly_wait(5)
driver.find_element_by_id("com.allbit.internal.debug:id/info_btn_close").click()

#아무키나 눌러주세요.
def wait():
    m.getch()

#로그인
def Login(usedId, userPw):
    driver.find_element_by_accessibility_id("계정").click()
    driver.find_element_by_id("com.allbit.internal.debug:id/btn_login").click()
    id_input = driver.find_element_by_xpath("//android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.EditText")
    id_input.send_keys(usedId)
    pw_input = driver.find_element_by_xpath("//android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText")
    pw_input.send_keys(userPw)
    driver.find_element_by_id("com.allbit.internal.debug:id/button").click()

    input("캡차가 통과되었으면 ENTER를 눌러주세요.")
    driver.find_element_by_accessibility_id("거래소").click()

#지갑 선택
def WalletSelect():
    driver.find_element_by_accessibility_id("계정").click()
    driver.find_element_by_id("com.allbit.internal.debug:id/add_wallet").click()
    wallet_2 = driver.find_element_by_xpath("//android.widget.LinearLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.CheckBox")
    wallet_2.click()
    #다른 월렛 선택시 딜레이 필요
    time.sleep(2)
    wallet_1 = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.CheckBox")
    wallet_1.click()

    #여기 코드 안먹힘
    #driver.find_element_by_accessibility_id("위로 이동").click()
    #driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='위로 이동']")
    time.sleep(2)
    driver.back()
    driver.find_element_by_accessibility_id("거래소").click()

#매수하기
def BTC_ETH_BUY():

    driver.find_element_by_accessibility_id("거래소").click()
    BTC_ETH = driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout/android.view.ViewGroup")
    BTC_ETH.click()
    driver.find_element_by_id("com.allbit.internal.debug:id/amount_radio_25p").click()

    read_price = driver.find_element_by_id("com.allbit.internal.debug:id/order_price_edit_text")
    price_half = read_price.text
    # 현재가의 절반가로 구매
    set_price_half = float(price_half) / 2
    set_price_half = round(set_price_half, 8)
    set_price_half = str(set_price_half)

    read_price.click()
    driver.implicitly_wait(3)
    input_price = driver.find_element_by_id("com.allbit.internal.debug:id/input_aid_edit_text")
    input_price.clear()
    input_price.send_keys(set_price_half)

    driver.back()
    driver.find_element_by_id("com.allbit.internal.debug:id/btn_trade").click()
    second_pwd("001223")

    driver.implicitly_wait(5)
    driver.find_element_by_id("com.allbit.internal.debug:id/btn_ok").click()
    driver.back()
    driver.find_element_by_accessibility_id("거래소").click()

def BTC_ETH_CANCEL():
    driver.find_element_by_accessibility_id("자산관리").click()

    driver.find_element_by_id("android:id/text1").click()
    el2 = driver.find_element_by_xpath("//android.widget.ListView/android.widget.CheckedTextView[2]").click()

    driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.Button").click()
    second_pwd("001223")
    time.sleep(2)

    driver.find_element_by_id("com.allbit.internal.debug:id/btn_ok").click()
    driver.find_element_by_accessibility_id("거래소").click()

def ETH_BTC_SELL():
    driver.find_element_by_accessibility_id("거래소").click()
    #driver.find_element_by_accessibility_id("ETH").click()
    driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout/android.view.ViewGroup").click()

    driver.find_element_by_accessibility_id("매도").click()
    driver.find_element_by_id("com.allbit.internal.debug:id/amount_radio_25p").click()

    read_price = driver.find_element_by_id("com.allbit.internal.debug:id/order_price_edit_text")
    price_2x = read_price.text
    # 현재가의 2배가로 구매
    set_price_2x = float(price_2x) * 2
    set_price_2x = round(set_price_2x, 8)
    set_price_2x = str(set_price_2x)

    read_price.click()
    driver.implicitly_wait(3)
    input_price = driver.find_element_by_id("com.allbit.internal.debug:id/input_aid_edit_text")
    input_price.clear()
    input_price.send_keys(set_price_2x)

    driver.back()
    driver.find_element_by_id("com.allbit.internal.debug:id/btn_trade").click()
    second_pwd("001223")

    driver.implicitly_wait(5)
    driver.find_element_by_id("com.allbit.internal.debug:id/btn_ok").click()
    driver.back()
    driver.find_element_by_accessibility_id("거래소").click()

def ETH_BTC_CANCEL():
    driver.find_element_by_accessibility_id("자산관리").click()
    driver.find_element_by_id("android:id/text1").click()
    driver.find_element_by_xpath("//android.widget.ListView/android.widget.CheckedTextView[3]").click()

    driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.Button").click()
    second_pwd("001223")
    time.sleep(2)

    driver.find_element_by_id("com.allbit.internal.debug:id/btn_ok").click()
    driver.find_element_by_accessibility_id("거래소").click()

def TXview():
    driver.find_element_by_accessibility_id("자산관리").click()
    driver.find_element_by_accessibility_id("TX").click()

    x = 0
    for x in range(2, 10):
        driver.find_element_by_id("android:id/text1").click()
        tx_listbox_select = driver.find_element_by_xpath("//android.widget.ListView/android.widget.CheckedTextView["+ str(x) + "]")
        tx_listbox_select.click()
    driver.find_element_by_id("android:id/text1").click()
    driver.find_element_by_xpath("//android.widget.ListView/android.widget.CheckedTextView[1]").click()
    driver.find_element_by_accessibility_id("거래소").click()

def second_pwd(walletPw):
    driver.find_element_by_id("com.allbit.internal.debug:id/input").send_keys(walletPw)
    driver.find_element_by_id("com.allbit.internal.debug:id/button").click()

def exchange_search(token):
    driver.find_element_by_accessibility_id("거래소").click()
    driver.find_element_by_id("com.allbit.internal.debug:id/search_button").click()
    driver.find_element_by_id("com.allbit.internal.debug:id/search_src_text").send_keys(token)
    driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout/android.view.ViewGroup").click()
    driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="위로 이동"]')
    x = 0
    for x in range(5):
        driver.back()
    driver.find_element_by_accessibility_id("거래소").click()

Login("chan@dxmcorp.com", "qwerty123!")

number = ""
while number != "5":
    print('확인할 케이스를 선택하세요')
    print()
    print('1. 로그인')
    print('2. 지갑선택')
    print('3. 거래소 코인 검색')
    print('4. 매수하기')
    print('5. 매수 취소하기')
    print('6. 매도하기')
    print('7. 매도 취소하기')
    print('8. TX 정보 조회')
    print('9. 끝내기')
    number = input('선택하세요 : ')

    if number == "1":
        Login("chan@dxmcorp.com", "qwerty123!")
    elif number == "2":
        WalletSelect()
    elif number == "3":
        exchange_search("trx")
    elif number == "4":
        BTC_ETH_BUY()
    elif number == "5":
        BTC_ETH_CANCEL()
    elif number == "6":
        ETH_BTC_SELL()
    elif number == "7":
        ETH_BTC_CANCEL()
    elif number == "8":
        TXview()
    if number == "9":
        driver.quit()
        sys.exit(1)
        break