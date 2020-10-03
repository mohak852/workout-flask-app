from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:new@localhost/workout_final'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password_hash = db.Column(db.Unicode)
    units = db.Column(db.String) 
    workouts = db.relationship('Workout', backref='user', lazy='dynamic')
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    notes = db.Column(db.Text)
    bodyWeight = db.Column(db.Numeric)
    Excercises = db.relationship('Exercise', backref="workout", lazy='dynamic')
class Exercises(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    order = db.Column(db.Integer, unique=True)
    excercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
    sets = db.relationship('Set', backref='exercise', lazy='dynamic')
class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer,unique=True)
    weight = db.Column(db.Numeric)
    reps = db.Column(db.Integer)
    excercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))




# if __name__ == "__main":
#     manager.run()
