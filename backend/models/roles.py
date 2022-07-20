from datetime import date, datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db

@dataclass
class Role(db.Model):
   id: int
   name: str
   created_at:datetime
   updated_at:datetime

   __tablename__ = 'Roles'   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(80), nullable=False)
   created_at = db.Column(db.DateTime, default=datetime.now())
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<Role %r>" % self.name

   def tojson(self):
       return self.__dict__
