from datetime import date, datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db


@dataclass
class Exam(db.Model):
   id: int
   name: str
   comment: str
   file:str
   start_time:date
   end_time:date
   end_:date
   type:str
   duration:str
   is_uploaded:bool
   is_submitted:bool
   created_at:datetime
   updated_at:datetime

   __tablename__ = 'Exams'   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   comment = db.Column(db.Text(120), unique=True, nullable=True)
   start_time = db.Column(db.Time(120), unique=True, nullable=True)
   end_time = db.Column(db.Time(120), unique=True, nullable=True)
   type = db.Column(db.Time(120), unique=True, nullable=True)
   couse_unit_id = db.Column(db.Integer, db.ForeignKey('couse_units.id',ondelete='CASCADE'))
   created_at = db.Column(db.DateTime, default=datetime.now())
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<Exam %r>" % self.name

   def tojson(self):
       return self.__dict__
