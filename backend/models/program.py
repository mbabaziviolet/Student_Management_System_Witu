from datetime import date, datetime
from dataclasses import dataclass
from backend.db import db


@dataclass
#inheritance or creating  a new model instance
class Program(db.Model):
   id: int
   name: str
   description: str
   start_date: date
   end_date: date
   duration: str
   status:str
   created_at:datetime
   updated_at:datetime

   __tablename__ = 'programs'   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(255),unique=True, nullable=False)
   description = db.Column(db.Text(120),  nullable=True)
   start_date = db.Column(db.Date(), nullable=False)
   duration = db.Column(db.String(), nullable=False)
   end_date = db.Column(db.Date(), nullable=False)
   status = db.Column(db.String(), nullable=False,default="Closed")
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<Program %r>" % self.name

  