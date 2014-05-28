from flask import Flask, render_template, redirect, url_for, session, request, send_from_directory
from flask import jsonify
import db
from utils import User, Pawn, Rook, Knight, Bishop, Queen, King, Room

app = Flask(__name__)
app.secret_key = "asdfghjkl"

black = 1
white = 2
spectator = 3

def auth(func):
	def wrapper(*args):
		if "username" in session:
			return func()
		else:
			return redirect("/login")
	return wrapper

@app.route("/")
def home():
	return render_template("home.html")

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

@app.route("/pieceMoved")
def pieceMoved():
	a = checkMove()
	if a:
		#store position of new piece and return true
	else:
		#put piece back in original position and return false

@app.route("/dosomething")
def something():
	a = request.args.get('a', 0, type=int)
	b = request.args.get('b', 0, type=int)
	return jsonify(result = a + b)

@app.route("/logout")
def logout():
	session.pop("username", None)
	return redirect("/login")

if __name__ == "__main__":
	app.debug = True
	app.run()