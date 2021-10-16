from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import urllib
import re
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys

def categories(keyword:str)->str:
  if keyword == "中筋麵粉" or keyword == "蒜頭":
    category = '其他'  
  elif keyword == "洋蔥" or keyword =="紅蘿蔔" or keyword =="青蔥":
    category = "蔬菜"
  elif keyword == "鹽" or keyword =="黑胡椒" or keyword =="香油":
    category = "調味料"
  elif keyword == "五花肉":
    category = "肉類"
  elif keyword == "蝦仁":
    category = "海鮮"
  return category

cred = credentials.Certificate(r"test-4fa88-firebase-adminsdk-54nig-c645ede062.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def order(keyword):
  category = categories(keyword)
  doc_ref = db.collection('shopee',category,keyword)
  list = doc_ref.get()
  for doc in list:
      name = doc.to_dict()['name']
  priceQ = doc_ref.order_by(u'price', direction = firestore.Query.ASCENDING).limit_to_last(1)
  Plist = priceQ.get()

  ls = []


  for doc in Plist:
      name = doc.to_dict()['name']
      price = doc.to_dict()['price']
      link = doc.to_dict()['link']
      ls.append(name.encode())
      ls.append(price)
      ls.append(category.encode())
      ls.append(keyword.encode())
      ls.append(link.encode())
      print(ls)



for i in range(1, len(sys.argv)):
  order(sys.argv[i])









