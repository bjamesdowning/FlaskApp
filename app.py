#Flask testing

from flask import Flask, request, render_template
import pymongo
from dbconnect import Database


app = Flask(__name__)

@app.route('/')
def homepage():
	home = "Homepage"
	return render_template("homepage.html", home=home)

@app.route('/author/<authors_last_name>')
def author(authors_last_name):
	return render_template(authors_last_name + '.html')

@app.route('/query/<scope>', methods=["POST"])
def query(scope):
	conn = Database()
	conn.initialize()
	if scope == 'find':
		find = conn.find()
		return render_template('db_results.html',find=find)
	elif scope == 'find_one':
		find = conn.find_one()
		return render_template('db_results.html', find=find)

@app.route('/insert', methods=['POST'])
def insert():
	key = request.form['key']
	value = request.form['value']
	conn = Database()
	conn.initialize()
	conn.insert(key, value)
	return 'Success'


@app.route('/login')
def login_form():
	return render_template("login_form.html")

@app.route('/login/auth', methods = ["POST"])
def login_auth():
	return render_template("login_auth.html")

if __name__ == '__main__':
	app.run()
