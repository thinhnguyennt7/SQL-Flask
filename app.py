from flask import Flask, render_template, redirect, session, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/register.db'
db = SQLAlchemy(app)


class userdata(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False)
	password = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return str(self.id) + ', ' + self.username + ', ' + str(self.password) + ''

dataUser = userdata.query.all()
userss = []
newuserdata = userdata(username='vngs', password=1111)
for data in dataUser:
	userss.append(data.username)

if (newuserdata.username not in userss):
	db.session.add(newuserdata)
	db.session.commit()


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
	check = False
	if request.method == 'POST':
		theusername = request.form['username']
		thepassword = request.form['password']
		for i in dataUser:
			if (i.username == theusername) and (i.password == int(thepassword)):
				check = True

		if (check):
			return redirect("/table")
		else:
			return redirect("/failure")


@app.route("/register", methods=["GET"])
def signin():
	if request.method == "GET":
		return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
	if request.method == "POST":
		theusername = request.form['username']
		thepassword = request.form['password']
		if theusername not in userss:
			newUser = userdata(username=theusername, password=thepassword)
			db.session.add(newUser)
			db.session.commit()
			return render_template("thanks.html")
	return render_template("sorry.html")


@app.route("/table")
def table():
	return render_template("table.html", data=dataUser)


@app.route("/logined")
def logined():
	return render_template("logined.html")


@app.route("/failure")
def failure():
	return render_template("failure.html")


# Run server
app.run(debug=True,host='0.0.0.0', port=5000)