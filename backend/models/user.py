from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db
from flask_login import UserMixin


@dataclass
class User(UserMixin,db.Model):
   id: int
   first_name:str
   last_name:str
   email: str
   contact: str
   password: str
   created_at:datetime
   updated_at:datetime
   __tablename__ = 'users'   
  
   id = db.Column(db.Integer, primary_key=True,autoincrement=True)
   first_name = db.Column(db.String(50), index=True, unique=True,nullable=False)
   last_name = db.Column(db.String(50), index=True, unique=True,nullable=False)
   email = db.Column(db.String(150), unique = True, nullable=False)
   contact = db.Column(db.String(150), unique = True, nullable=False)
   password = db.Column(db.String(150))
   created_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)
   updated_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

   def __repr__(self):
        return "<User %r>" % self.email
