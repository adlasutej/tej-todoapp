# -*- encoding: utf-8 -*-
# begin

from flask_sqlalchemy import SQLAlchemy
from tej_todoapp import app
import datetime

db = SQLAlchemy(app)



class MyTodo (db.Model):
    __tablename__ = "my_todo"
    description = db.Column('description', db.Unicode)
    creation_date = db.Column('creation_date', db.Date,default=datetime.datetime.now())
    is_done = db.Column('is_done', db.Boolean,default=False)
    priority_id = db.Column('priority_id', db.Integer, db.ForeignKey('priority.id'))
    id = db.Column('id', db.Integer, primary_key = True)
    category_id = db.Column('category_id', db.Integer, db.ForeignKey('category.id'))

    priority = db.relationship('Priority', foreign_keys=priority_id)
    category = db.relationship('Category', foreign_keys=category_id)

class Category (db.Model):
    __tablename__ = "category"
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.Unicode)

class Priority (db.Model):
    __tablename__ = "priority"
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.Unicode)
    value = db.Column('value', db.Integer)

# end
