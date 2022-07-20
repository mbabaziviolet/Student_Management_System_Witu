# from datetime import date, datetime
# from email.policy import default
# from flask_sqlalchemy import SQLAlchemy
# from dataclasses import dataclass
# db = SQLAlchemy()


# @dataclass
# class StudentAssignment(db.Model):
#    id: int
#    student_id: str
#    assignment_id: str
#    created_at:datetime
#    updated_at:datetime

#    __tablename__ = 'student_assignments'   
#    id = db.Column(db.Integer, primary_key=True)
#    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id',ondelete='CASCADE'))
#    student_id = db.Column(db.Integer, db.ForeignKey('studen.id',ondelete='CASCADE'))
#    created_at = db.Column(db.DateTime, default=datetime.now())
#    created_at = db.Column(db.DateTime, default=datetime.now())
#    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
   

#    def __repr__(self):
#         return "<StudentAssignment %r>" % self.id

#    def tojson(self):
#        return self.__dict__
