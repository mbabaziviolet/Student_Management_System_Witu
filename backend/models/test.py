from datetime import date, datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db


@dataclass
class test(db.Model):
   id: int
   name: str
   description: str
   start_time:str
   is_uploaded:bool
   is_submitted:bool
   type:str
   created_at:datetime
   updated_at:datetime

   __tablename__ = 'tests'   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   comment = db.Column(db.Text(120), unique=True, nullable=True)
   course_unit_id = db.Column(db.Integer, db.ForeignKey('course_units.id',ondelete='CASCADE'))
   created_at = db.Column(db.DateTime, default=datetime.now())
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<test %r>" % self.name

   def tojson(self):
       return self.__dict__
