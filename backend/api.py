import flask
import flask.ext.sqlalchemy
import flask.ext.restless

# Create Flask application
app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

class Table(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	num_seats = db.Column(db.Integer)
	is_booked = db.Column(db.Boolean)
#	date_booked = db.Column(db.Date)
#	time_booked = db.Column(db.Time)
#	image = db.Column(db.Unicode)

	def __init__(self, num_seats, is_booked):
		self.num_seats = num_seats
		self.is_booked = is_booked


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Unicode)
	email = db.Column(db.Unicode)
	table_booked = db.Column(db.Integer)
	time_booked = db.Column(db.Time)
	image = db.Column(db.Unicode)

	def __init__(self, username, email, table_booked, time_booked, image):
		self.username = username
		self.email = email
		self.table_booked = table_booked
		self.time_booked = time_booked
		self.image = image

	def __repr__(self):
		return '<User %r>' % self.username

@app.route('/')
def hello_world():
	return "Hello World"

@app.route('/seed')
def seed():
	for i in range(4):
		table = Table(4, False)
		db.session.add(table)
	db.session.commit()
	return "Database seeded"

@app.route('/booktable', methods=['POST', 'GET'])
def booktable():
	tableid = flask.request.form['tableid']
	table = Table.query.filter_by(id=tableid).first()
	table.is_booked = True
	db.session.add(table)
	db.session.commit()
	return "Your reservation has been made."

#Method to list whether tables free or not free
#Time stamps, address fields

if __name__ == '__main__':
	#Create database tables
	db.create_all()

	#Create Flask-Restless API manager
	manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
	manager.create_api(User, methods=['GET', 'POST', 'DELETE', 'PUT'])
	manager.create_api(Table, methods=['GET', 'POST', 'DELETE', 'PUT'])


	app.run("0.0.0.0", debug=True)