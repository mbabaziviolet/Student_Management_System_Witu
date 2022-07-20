from datetime import date, datetime
from dataclasses import dataclass
from backend.db import db


@dataclass
#inheritance or creating  a new model instance
class Course(db.Model):
   id: int
   name: str
   description: str
   duration: str
   created_at:datetime
   updated_at:datetime

   __tablename__ = 'courses'   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(255),unique=True, nullable=False)
   description = db.Column(db.Text(120),  nullable=True)
   duration = db.Column(db.String(), nullable=False)
   created_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<Course %r>" % self.name

 