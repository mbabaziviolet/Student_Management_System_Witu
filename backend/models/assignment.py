from datetime import date, datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db


@dataclass
class Assignment(db.Model):
   id: int
   name: str
   description: str
   file:str
   start_date:date
   deadline:date
   is_uploaded:bool
   is_submitted:bool
   created_at:datetime
   updated_at:datetime

   __tablename__ = 'Assignments'   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   description = db.Column(db.Text(120), unique=True, nullable=True)
   programe_id = db.Column(db.Integer, db.ForeignKey('programs.id',ondelete='CASCADE'))
   created_at = db.Column(db.DateTime, default=datetime.now())
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<Assignment %r>" % self.name

   def tojson(self):
       return self.__dict__
