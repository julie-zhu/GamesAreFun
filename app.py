from flask import Flask, render_template, redirect, url_for, session, request, send_from_directory
from flask import jsonify
import db

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
