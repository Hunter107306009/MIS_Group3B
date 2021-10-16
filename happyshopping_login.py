
#讀取帳密, index
import sys
index = sys.argv[1]
account = sys.argv[2]
pw = sys.argv[3]
captcha = sys.argv[4]

#讀取driver_setting(連結資料庫)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r"test-4fa88-firebase-adminsdk-54nig-c645ede062.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection('driver_setting').document(index)
rs = doc_ref.get().to_dict()

session_id = rs['session_id']
executor = rs['exe_id']


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#開啟driver 並傳遞參數進去
driver = webdriver.Remote(command_executor=executor , desired_capabilities={})
driver.session_id = session_id

#簡易操作，測試瀏覽器是否運作
element = driver.find_element_by_id("account")
element.send_keys(account)  ##帳號
element = driver.find_element_by_id("pwd")
element.send_keys(pw)  ##密碼
element = driver.find_element_by_id("checkCode")
element.send_keys(captcha)
driver.find_element_by_class_name("btn_login").send_keys(Keys.ENTER)

try:
    driver.get("https://www.happy-shopping.tw/index.php")
    element = driver.find_element_by_class_name("never")
    element.click()
    python_button = driver.find_elements_by_xpath("//*[@id='market_close']")[0]
    python_button.click()
except:
    print("暫無廣告產生")
else:
    print("已關閉廣告")


##測試是否登入 否則強制退出python
driver.get("https://www.happy-shopping.tw/order_history.php?")
time.sleep(2)
element = driver.find_element_by_class_name("btn_send")

print("登入成功")
##清空購物車
driver.get("https://www.happy-shopping.tw/cart.php")
driver.implicitly_wait(2)
if driver.current_url == 'https://www.happy-shopping.tw/cart.php':
    element = driver.find_element_by_class_name("btn_clear")
    element.send_keys(Keys.ENTER)
    time.sleep(1)
    element = driver.find_element_by_class_name("btn-primary")
    element.send_keys(Keys.ENTER)

time.sleep(1)


##加入購物車

def putIntoCart(url):
    driver.get(url)
    element = driver.find_element_by_class_name("btn_buy")
    element.send_keys(Keys.ENTER)

#for i in range(1, len(sys.argv)):
#  putIntoCart(sys.argv[i])

#0826
##從資料庫內讀取預購買商品，並加入購物車

db = firestore.client()

doc_ref = db.collection('order').document(index)
rs = doc_ref.get().to_dict()

for i in range(len(rs)):
    link = rs[str(i)]
    
    try:
        putIntoCart(link)
    except:
        print("商品缺貨或過期")
    time.sleep(1)



print("結束")

#time.sleep(60)
driver.close()
