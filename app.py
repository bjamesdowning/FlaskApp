#Flask testing

from flask import Flask, request, render_template
from dbconnect import Database
import pymongo

app = Flask(__name__)

@app.route('/')
def homepage():
	conn = Database()
	conn.initialize()
	home = "Homepage"
	return render_template("homepage.html", home=home)

@app.route('/author/<authors_last_name>')
def author(authors_last_name):
	return render_template(authors_last_name + '.html')

@app.route('/login')
def login_form():
	return render_template("login_form.html")

@app.route('/login/auth', methods = ["POST"])
def login_auth():
	return render_template("login_auth.html")

if __name__ == '__main__':
	app.run()
