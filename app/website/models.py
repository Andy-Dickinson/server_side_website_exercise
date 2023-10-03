# create database models here
from . import db  # from package import db (SQLAchemy())
from flask_login import UserMixin # module that helps users login
from sqlalchemy.sql import func # gets and formats time and data info


# database to store notes
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000)) # note text 
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # uses id from user db as foreign key - note defining schemas are uppercase, however when referencing use lowercase (as represented by sql)


# defines schema for User database
class User(db.Model, UserMixin):
    # defines columns - id is of Integer type and is the primary key
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note', backref='user') # relationships are defined with uppercase (as per class definition) - note different to defining foreign key. Here this defines a relationship between the notes created by user to the actual user giving them access to only their notes, 'backref' allows you to access the user associated with a note more easily e.g. 'note.user'