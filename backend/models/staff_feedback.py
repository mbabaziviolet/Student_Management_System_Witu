# class FeedBackStaffs(models.Model):
#     id = models.AutoField(primary_key=True)
#     staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
#     feedback = models.TextField()
#     feedback_reply=models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     objects = models.Manager()