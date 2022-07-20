from datetime import date, datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db


@dataclass
class Application(db.Model):
   id: int
   name: str
   uace_file:str
   uace_file:str
   start_date:date
   deadline_date:date
   opened_date:date
   is_uploaded:bool
   is_submitted:bool
   created_at:datetime
   updated_at:datetime
   status:str 

   __tablename__ = 'Applications'   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   uace_file = db.Column(db.Text(120), unique=True, nullable=True)
   uce_file = db.Column(db.Text(120), unique=True, nullable=True)
   status = db.Column(db.Text(120), unique=True, nullable=True)
   deadline_date = db.Column(db.Text(120), unique=True, nullable=True)
   opened_date = db.Column(db.Text(120), unique=True, nullable=True)
   intake_type = db.Column(db.Text(120), unique=True, nullable=True)
   learning_schedule = db.Column(db.Text(120), unique=True, nullable=True)
   heard_us = db.Column(db.Text(120), unique=True, nullable=True)
   created_at = db.Column(db.DateTime, default=datetime.now())
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<Assignment %r>" % self.name

   def tojson(self):
       return self.__dict__
