import flask
import flask.ext.sqlalchemy
import flask.ext.restless

# Create Flask application
app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

class Restaurant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode)
	restaurant = db.Column(db.Unicode)
	tables = db.Column(db.Integer)
	street1 = db.Column(db.Unicode)
	street2 = db.Column(db.Unicode)
	city = db.Column(db.Unicode)
	postalcode = db.Column(db.Unicode)

#Create database tables
db.create_all()

#Create Flask-Restless API manager
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Restaurant, methods=['GET', 'POST', 'DELETE', 'PUT'])

app.run("0.0.0.0", debug=True)