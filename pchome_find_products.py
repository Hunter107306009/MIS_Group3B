import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r"test-4fa88-firebase-adminsdk-54nig-c645ede062.json")
firebase_admin.initialize_app(cred)
db = firestore.client()



def categories(prod:str):
  if prod == "中筋麵粉" or prod == "蒜頭":
    category = '其他'  
  elif prod == "洋蔥" or prod =="紅蘿蔔" or prod =="青蔥":
    category = "蔬菜"
  elif prod == "鹽" or prod =="黑胡椒" or prod =="香油":
    category = "調味料"
  elif prod == "五花肉":
    category = "肉類"
  elif prod == "蝦仁":
    category = "海鮮"
  else:
    category = '其他'
  return category

def order(prod:str):
  category = categories(prod)
  query1 = db.collection('pchome',category,prod)
  query2 = query1.order_by(
      u'price', direction=firestore.Query.ASCENDING).limit(1)
  results1 = query2.get()
  ls=[]
  for doc in results1:
        name = doc.to_dict()['name']
        price = doc.to_dict()['price']
        link = doc.to_dict()['link']
        ls.append(name.encode())
        ls.append(price)
        ls.append(category.encode())
        ls.append(prod.encode())
        ls.append(link.encode())
        print(ls)

for i in range(1, len(sys.argv)):
  prod = sys.argv[i]
  order(prod)

