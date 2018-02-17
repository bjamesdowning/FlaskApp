#Flask testing

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("homepage.html")

@app.route('/submit', methods=['POST'])
def submit():
	return 'You entered: {}'.format(request.form['text'])

if __name__ == '__main__':
	app.run()

