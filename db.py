from pymongo import MongoClient

def open():
  client = MongoClient()
  db = client.pieces
  return db
  
def newBoard(): #or newGame? hmmm
  #should create 2 arrays, 1 for black, 1 for white
  #these should keep track of position and status (taken or not)
