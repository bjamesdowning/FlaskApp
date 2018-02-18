#Flask testing

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("homepage.html")

@app.route('/Login', methods=['POST'])
def submit():
	return render_tempalte("login.html")

if __name__ == '__main__':
	app.run()

