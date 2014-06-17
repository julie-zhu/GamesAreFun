from flask import Flask, render_template, redirect, url_for, session, request, send_from_directory
from flask import jsonify
import json
import db

app = Flask(__name__)
app.secret_key = "asdfghjkl"

#room capacity
players = [0,0,0,0]
counter = 0

@app.route("/")
def home():
	return render_template("home.html", piece = "piece")

#give the ID of the player
@app.route("/giveID")
def giveID():
	counter = 0
	for x in players:
		if x == 0:
			players[x] = 1
			return jsonify(str(counter + 1 * 10))
		else:
			counter += 1
			
#updateBoard returns the current position of all the pieces
@app.route("/updateBoard")
def update():
	boardData = db.boardStatus()
	return jsonify(boardData)

#updatePiece should be called whenever a piece is taken, moved, or promoted
@app.route("/updatePiece")
def updatePiece(row, FEN):
	db.updateBoard(row, FEN)

@app.route("/newBoard")
def newGame():
	db.newGame2()

#here for reference
@app.route("/dosomething")
def something():
	a = request.args.get('a', 0, type=int)
	b = request.args.get('b', 0, type=int)
	return jsonify(result = a + b)

#logout should empty out a slot in the players list for someone else to join
@app.route("/logout")
def logout():
	for x in players:
		if x == 1:
			players[x] = 0

if __name__ == "__main__":
	app.debug = True
	app.run()
