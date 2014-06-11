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

#showBoard should return all the pieces on the board
@app.route("/showBoard")
def showBoard():
	return jsonify(findActivePieces())

#updatePiece should be called whenever a piece is taken, moved, or promoted
@app.route("/updatePiece")
def updatePiece():
	refreshPiece(piece, color, x, y)

@app.route("/newBoard")
def newGame():
	newBoard()

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
