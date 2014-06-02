from pymongo import MongoClient

def open():
  client = MongoClient()
  db = client.pieces
  return db
  
#adds pieces
def addPiece(piece, color, x, y):
  db = open()
  db.insert({'piece': piece, 'color': color, 'x': x, 'y': y})
  return True

#one array of 32 pieces
def newBoard(): #or newGame? hmmm
  db = open()
  
  for x in range(0, 8):
    addPiece("Pawn", "black", 7, x)
    
  for x in range(0, 8):
    addPiece("Pawn", "white", 1, x)
    
  # rows and columns are numbered from 0 to 7  (0,0) is the bottom left corner
  addPiece("Rook", "black", 7, 0)
  addPiece("Rook", "black", 7, 7)
  addPiece("Rook", "white", 0, 0)
  addPiece("Rook", "white", 0, 7)
  
  addPiece("Knight", "black", 7, 1)
  addPiece("Knight", "black", 7, 6)
  addPiece("Knight", "white", 0, 1)
  addPiece("Knight", "white", 0, 6)
  
  addPiece("Bishop", "black", 7, 2)
  addPiece("Bishop", "black", 7, 5)
  addPiece("Bishop", "white", 0, 2)
  addPiece("Bishop", "white", 0, 5)
  
  addPiece("King", "black", 7, 4)
  addPiece("King", "white", 0, 4)
  
  addPiece("Queen", "black", 7, 3)
  addPiece("Queen", "white", 0, 3)
  return True
  
#finds a piece and updates its coordinates and/or status
def updatePiece(piece, color, x, y):
  db = open()
  piece = db.find_one({'piece': piece, 'color':color}, fields={'_id': False})
  db.update({'piece': piece}, {'$set':{'x': x, 'y': y}})
  
