
# class StudentResult(models.Model):
#     id=models.AutoField(primary_key=True)
#     student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
#     subject_id=models.ForeignKey(Subjects,on_delete=models.CASCADE)
#     subject_exam_marks=models.FloatField(default=0)
#     subject_assignment_marks=models.FloatField(default=0)
#     created_at=models.DateField(auto_now_add=True)
#     updated_at=models.DateField(auto_now_add=True)
#     objects=models.Manager()