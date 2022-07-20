from datetime import date, datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from backend import db


@dataclass
class CourseUnit(db.Model):
   id: int
   title: str
   file: str
   description: str
   created_at:datetime
   updated_at:datetime
   deleted_at:datetime
   posted_at:datetime

   __tablename__ = 'CourseUnits'   
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(80), nullable=False)
   file = db.Column(db.String(80), nullable=False)
   description = db.Column(db.Text(120), unique=True, nullable=True)
   programe_id = db.Column(db.Integer, db.ForeignKey('programs.id',ondelete='CASCADE'))
#    tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id',ondelete='CASCADE'))
#    student_id = db.Column(db.Integer, db.ForeignKey('students.id',ondelete='CASCADE'))
#    time_table_id = db.Column(db.Integer, db.ForeignKey('time_tables.id',ondelete='CASCADE'))
   created_at = db.Column(db.DateTime, default=datetime.now())
   deleted_at = db.Column(db.DateTime, default=datetime.now())
   updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   posted_at = db.Column(db.DateTime, onupdate=datetime.now())
   

   def __repr__(self):
        return "<CourseUnit %r>" % self.name

   def tojson(self):
       return self.__dict__
