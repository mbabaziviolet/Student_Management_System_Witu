from datetime import date, datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db

@dataclass
class Attendance(db.Model):
    id=db.Column(primary_key=True)
    course_unit=db.Column(db.Integer, db.ForeignKey('attendances.id',ondelete='CASCADE'))
    attendance_date=db.Column(db.DateTime, onupdate=datetime.now())
 
   