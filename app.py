from flask import Flask, render_template, redirect, url_for, session, request, send_from_directory
from flask import jsonify
import db
from utils import User, Pawn, Rook, Knight, Bishop, Queen, King, Room

app = Flask(__name__)
app.secret_key = "asdfghjkl"

#player ID's
black = 1
white = 2
spectator = 3

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

#dunno , just kept this here in case it's needed
def auth(func):
	def wrapper(*args):
		if "username" in session:
			return func()
		else:
			return redirect("/login")
	return wrapper

#homepage, needs to have navigation to board page
@app.route("/")
def home():
	return render_template("home.html")

#not needed, will delete later
@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		username = request.form["username"]
		password = request.form["password"]
		if not username or not password:  
			return redirect("/secret2")
		elif db.login(username, password):
			session["username"] = username
			return redirect("/secret1")
		else :
			return redirect("/secret2")

#pieceMoved should, given the piece, its original position, and its new position, check to see
#if the move is valid. if valid, should return true and save the new position of the piece into the db.
#if not valid, return false and do nothing at all.
#@app.route("/pieceMoved")
#def pieceMoved():
#	a = checkMove()
#	if a:
#		#store position of new piece and return true
#	else:
#		#put piece back in original position and return false

#showBoard should get x and y coor's of all active pieces (meaning not taken/defeated) and show them
@app.route("/showBoard")
def showBoard():
	#placeholder

#updatePiece should be called whenever a piece is taken, moved, or promoted
@app.route("/updatePiece")
def updatePiece():
	#placeholder

#here for reference
@app.route("/dosomething")
def something():
	a = request.args.get('a', 0, type=int)
	b = request.args.get('b', 0, type=int)
	return jsonify(result = a + b)

#logout should remove the ID of the user (1, 2, or 3) so that other people can play/spectate
@app.route("/logout")
def logout():
	session.pop("username", None)
	return redirect("/login")

if __name__ == "__main__":
	app.debug = True
	app.run()
