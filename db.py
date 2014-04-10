from pymongo import MongoClient

def open():
  client = MongoClient()
  db = client.gm.users
  return db
  
def register(username, password, nickname):
    db = open()
    check = db.find_one({'username' : username}, fields={'_id':False})
    if check == None:
        db.insert({'username' : username, 'password' : password, 'nickname' : nickname})
        return True
    else:
        return False
        
def getNickName(username):
    db = open()
    check = db.find_one({'username':username}, fields={'_id':False})
    return check['nickname']
    
def login(username, password):
    db = open()
    user = db.find_one({'username' : username, 'password' : password}, fields={'_id':False})
    if user == None:
        return False
    else:
        return True
        
