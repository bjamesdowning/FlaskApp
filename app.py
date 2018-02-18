#Flask testing

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("homepage.html")

@app.route('/login', methods=['POST','GET'])
def login():
	return render_template("login.html")

if __name__ == '__main__':
	app.run()

