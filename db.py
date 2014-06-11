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

#finds a piece and updates its coordinates and/or status
def refreshPiece(piece, color, x, y):
  db = open()
  piece = db.find_one({'piece': piece, 'color':color}, fields={'_id': False})
  db.update({'piece': piece}, {'$set':{'x': x, 'y': y}})
  return True

#should return an array of all the pieces on the board
#this assumes that pieces that have been removed from the board have coordinates (x or y)
#that are less than 0. since the x/y coord's < 0, they shouldn't be on the board to begin with.
def findActivePieces():
  db = open()
  activePieces = db.find({x: {$gt: 0} }, {_id: 0})
  return activePieces

#one array of 32 pieces (2X for bughouse)
def newBoard(): #or newGame? hmmm
  db = open()
  db.remove({}) #to remove any pieces that may already exist
  
  for x in range(0, 8):
    addPiece("Pawn", "black1", 7, x)
    
  for x in range(0, 8):
    addPiece("Pawn", "white1", 1, x)
    
  # rows and columns are numbered from 0 to 7  (0,0) is the bottom left corner
  addPiece("Rook", "black1", 7, 0)
  addPiece("Rook", "black1", 7, 7)
  addPiece("Rook", "white1", 0, 0)
  addPiece("Rook", "white1", 0, 7)
  
  addPiece("Knight", "black1", 7, 1)
  addPiece("Knight", "black1", 7, 6)
  addPiece("Knight", "white1", 0, 1)
  addPiece("Knight", "white1", 0, 6)
  
  addPiece("Bishop", "black1", 7, 2)
  addPiece("Bishop", "black1", 7, 5)
  addPiece("Bishop", "white1", 0, 2)
  addPiece("Bishop", "white1", 0, 5)
  
  addPiece("King", "black1", 7, 4)
  addPiece("King", "white1", 0, 4)
  
  addPiece("Queen", "black1", 7, 3)
  addPiece("Queen", "white1", 0, 3)
  return True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
  for x in range(0, 8):
    addPiece("Pawn", "black2", 7, x)
    
  for x in range(0, 8):
    addPiece("Pawn", "white2", 1, x)
    
  addPiece("Rook", "black2", 7, 0)
  addPiece("Rook", "black2", 7, 7)
  addPiece("Rook", "white2", 0, 0)
  addPiece("Rook", "white2", 0, 7)
  
  addPiece("Knight", "black2", 7, 1)
  addPiece("Knight", "black2", 7, 6)
  addPiece("Knight", "white2", 0, 1)
  addPiece("Knight", "white2", 0, 6)
  
  addPiece("Bishop", "black2", 7, 2)
  addPiece("Bishop", "black2", 7, 5)
  addPiece("Bishop", "white2", 0, 2)
  addPiece("Bishop", "white2", 0, 5)
  
  addPiece("King", "black2", 7, 4)
  addPiece("King", "white2", 0, 4)
  
  addPiece("Queen", "black2", 7, 3)
  addPiece("Queen", "white2", 0, 3)
  return True
#-------------------------------------------------------------------------------------
def newBoard2(): #or newGame? hmmm (1X board's worth of pieces)
  db = open()
  db.remove({}) #to remove any pieces that may already exist
  
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

#move pools. assumes board is from 1-64 (8x8 square)
knightMoves = [6, 10, 15, 17]
pawnMoves = [7, 8, 9]
kingMoves = [0, 1, 7, 9]

#checkMove returns true if a piece's movement is legal, false otherwise
def checkMove(piece, oPosition, nPosition):
	if piece == "Knight":
		if abs(oPosition - nPosition) in knightMoves:
			return True
		else:
			return False
	if piece == "Pawn":
		if abs(oPosition - nPosition) in pawnMoves:
			return True
		else:
			return False
	if piece == "Rook":
		if abs(oPosition - nPosition) <= 7:
			return True
		elif abs(oPosition - nPosition) % 8 = 0:
			return True
		else:
			return False
	if piece == "Bishop":
		if abs(oPosition - nPosition) % 9 = 0:
			return True
		elif abs(oPosition - nPosition) % 7 = 0:
			return True
		else: 
			return False
	if piece == "Queen": #rook + bishop = queen
		if abs(oPosition - nPosition) <= 7:
			return True
		elif abs(oPosition - nPosition) % 8 = 0:
			return True
		elif abs(oPosition - nPosition) % 9 = 0:
			return True
		elif abs(oPosition - nPosition) % 7 = 0:
			return True
		else: 
			return False
	if piece == "King":
		if abs(oPosition - nPosition) <= 8:
			if abs(oPosition - nPosition) % 8 in kingMoves:
				return True
			else:
				return False
		else:
			return False
