import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys


def order(keyword:str):
    category = categories(keyword)
    doc_ref = db.collection('happyshopping',category,keyword)
    query = doc_ref.order_by("price").limit_to_last(1)
    results = query.get()
    ls=[]
    for doc in results:
      name = doc.to_dict()['name']
      price = doc.to_dict()['price']
      link = doc.to_dict()['link']
#print(name,price,link)
      ls.append(name.encode())
      ls.append(price)
      ls.append(category.encode())
      ls.append(keyword.encode())
      ls.append(link.encode())
      print(ls)


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




for i in range(1, len(sys.argv)):
  order(sys.argv[i])


'''


order('中筋麵粉')
order('五花肉') 
'''
