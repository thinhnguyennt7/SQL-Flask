from flask import Flask, render_template, redirect, session, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/register.db'
db = SQLAlchemy(app)


class userdata(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False)
	password = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return str(self.id) + ', ' + self.username + ', ' + str(self.password) + '||'


# newuserdata = userdata(username='tnntech', password=1111)
# Add new data to database and commit
# db.session.add(newuserdata)
# db.session.commit()

dataUser = userdata.query.all()


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
			return redirect("/logined")
		else:
			return redirect("/failure")


@app.route("/logined")
def logined():
	return render_template("logined.html")


@app.route("/failure")
def failure():
	return render_template("failure.html")


# Run server
app.run(debug=True,host='0.0.0.0', port=5000)