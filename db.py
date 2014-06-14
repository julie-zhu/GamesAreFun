from pymongo import MongoClient

def open():
  client = MongoClient()
  db = client.boards
  return db
  
def newGame():
	db = open()
	db.remove({})
	db.insert({'row': 1, 'FEN': "rnbqkbnr"})
	db.insert({'row': 2, 'FEN': "pppppppp"})
	db.insert({'row': 3, 'FEN': "8"})
	db.insert({'row': 4, 'FEN': "8"})
	db.insert({'row': 5, 'FEN': "8"})
	db.insert({'row': 6, 'FEN': "8"})
	db.insert({'row': 7, 'FEN': "PPPPPPPP"})
	db.insert({'row': 8, 'FEN': "RNBQKBNR"})
	
def newGame2():
	db = open()
	db.remove({})
	db.insert({'row': 1, 'FEN': "rnbqkbnr"})
	db.insert({'row': 2, 'FEN': "pppppppp"})
	db.insert({'row': 3, 'FEN': "8"})
	db.insert({'row': 4, 'FEN': "8"})
	db.insert({'row': 5, 'FEN': "8"})
	db.insert({'row': 6, 'FEN': "8"})
	db.insert({'row': 7, 'FEN': "PPPPPPPP"})
	db.insert({'row': 8, 'FEN': "RNBQKBNR"})
	db.insert({'row': 16, 'FEN': "rnbqkbnr"})
	db.insert({'row': 15, 'FEN': "pppppppp"})
	db.insert({'row': 14, 'FEN': "8"})
	db.insert({'row': 13, 'FEN': "8"})
	db.insert({'row': 12, 'FEN': "8"})
	db.insert({'row': 11, 'FEN': "8"})
	db.insert({'row': 10, 'FEN': "PPPPPPPP"})
	db.insert({'row': 9, 'FEN': "RNBQKBNR"})
	
def updateBoard(row, FEN):
	db = open()
	rowNum = db.find_one({'row': row}, fields={'_id': False})
	db.update({'row': row}, {'$set':{'FEN':FEN}})

def boardStatus():
	db = open()
	fenString1 = ""
	fenString2 = ""
	for x in range(0,8):
		dbFenString1 = db.find_one({'row': x+1}, fields={'_id': False}).getField('FEN')
		fenString1 += dbFenString1
		if x != 7:
			fenString += "/"
	for x in range(8,16):
		dbFenString2 = db.find_one({'row': x+1}, fields={'_id': False)}.getField('FEN')
		fenString2 += dbFenString2
		if x != 15:
			fenString += "/"
	ret = [fenString1, fenString2]
	return ret
	
#~~~~~~~extra stuff~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
	
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
		elif abs(oPosition - nPosition) % 8 == 0:
			return True
		else:
			return False
	if piece == "Bishop":
		if abs(oPosition - nPosition) % 9 == 0:
			return True
		elif abs(oPosition - nPosition) % 7 == 0:
			return True
		else: 
			return False
	if piece == "Queen": #rook + bishop = queen
		if abs(oPosition - nPosition) <= 7:
			return True
		elif abs(oPosition - nPosition) % 8 == 0:
			return True
		elif abs(oPosition - nPosition) % 9 == 0:
			return True
		elif abs(oPosition - nPosition) % 7 == 0:
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
