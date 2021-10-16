import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r"test-4fa88-firebase-adminsdk-54nig-c645ede062.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


login = False
index = 0

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2F")
element = driver.find_element_by_name("loginKey")
element.send_keys("0939680370")  ##帳號
element = driver.find_element_by_name("password")
element.send_keys("Cs147178753")  ##密碼

element = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button')

time.sleep(1)
element.send_keys(Keys.ENTER)
time.sleep(2)

element = driver.find_element_by_class_name("_25oo_3")
time.sleep(1)
element.send_keys(Keys.ENTER)

timer = -1
while driver.current_url == "https://shopee.tw/verify/link" :
    time.sleep(1)
    timer +=1
    if timer == 60:
        driver.find_element_by_class('123')


##checkbox


##加入購物車

def putIntoCart(url):
    driver.get(url)
    time.sleep(1)
    try:
        element = driver.find_elements_by_css_selector("div._2oeDUI")
        for i in range(len(element)):
            element[i].find_element_by_css_selector("button.product-variation:not(.product-variation--disabled)").click()
    except:
        print("沒有規格")

    element = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[1]')
    time.sleep(1)
    element.send_keys(Keys.ENTER)
    
    
time.sleep(5)

doc_ref = db.collection('order').document('7891011')
rs = doc_ref.get().to_dict()

for i in range(len(rs)):
    link = rs[str(i)]
    
    putIntoCart(link)
    time.sleep(1)
    
driver.get("https://shopee.tw/cart")

