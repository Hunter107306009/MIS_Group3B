import os
import re
import json
import time
import requests

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from selenium import webdriver
DRIVER_PATH = r"chromedriver.exe"
driver = webdriver.Chrome(DRIVER_PATH)
URL = "https://24h.pchome.com.tw/prod/DBDA20-A900AYQ9R"
ACC = "0939680370"
PWD = "Cs147178753"

def login():
    WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.ID, 'loginAcc'))
    )
    elem = driver.find_element_by_id('loginAcc')
    elem.clear()
    elem.send_keys(ACC)
    elem = driver.find_element_by_id('loginPwd')
    elem.clear()
    elem.send_keys(PWD)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.ID, "btnLogin"))
    )
    driver.find_element_by_id('btnLogin').click()
    print('成功登入')



def click_button(xpath):
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, xpath))
    )
    driver.find_element_by_xpath(xpath).click()



def get_product_id(url):
    pattern = '(?<=prod/)(\w+-\w+)'
    try:
        product_id = re.findall(pattern, url)[0]
        print(product_id)
        return product_id
    except Exception as e:
        print(e.__class__.__name__, ': 取得商品 ID 錯誤！')

def get_product_status(product_id):
    api_url = f'https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/button&id={product_id}'
    resp = requests.get(api_url)
    status = json.loads(resp.text)[0]['ButtonType']
    return status

"""
集中管理需要的 xpath
"""
xpaths = {
    'add_to_cart': "//li[@id='ButtonContainer']/button",
    'check_agree': "//input[@name='chk_agree']",


}

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def main():
    
    cred = credentials.Certificate(r"test-4fa88-firebase-adminsdk-54nig-c645ede062.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    db = firestore.client()

    doc_ref = db.collection('order').document('123456')
    rs = doc_ref.get().to_dict()
    for i in range(len(rs)):
        link = rs[str(i)]
        driver.get(link)
        element = driver.find_element_by_xpath('//*[@id="ButtonContainer"]/button')
        time.sleep(1)
        element.send_keys(Keys.ENTER)
        time.sleep(1)

    time.sleep(1)

    """
    放入購物車
    """
    #click_button(xpaths['add_to_cart'])
    #time.sleep(1)

    """
    前往購物車
    """
    driver.get("https://ecssl.pchome.com.tw/sys/cflow/fsindex/BigCar/BIGCAR/ItemList")

    """
    登入帳戶（注意！若有使用 CHROME_PATH 記住登入資訊，第二次執行時請記得註解掉登入這行！）
    """
    login()




driver = webdriver.Chrome(
    executable_path=DRIVER_PATH)
driver.set_page_load_timeout(120)

"""
抓取商品開賣資訊，並嘗試搶購
"""
curr_retry = 0
max_retry = 5   # 重試達 5 次就結束程式
wait_sec = 1

if __name__ == "__main__":
    product_id = get_product_id(URL)
    while curr_retry <= max_retry:
        status = get_product_status(product_id)
        if status != 'ForSale':
            print('商品尚未開賣！')
            curr_retry += 1
            time.sleep(wait_sec)
        else:
            print('商品已開賣！')
            main()
            break
