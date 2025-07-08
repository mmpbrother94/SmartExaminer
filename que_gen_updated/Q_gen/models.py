from django.db import models

# Create your models here.
# class generate_question(models.Model):
#         Class = models.CharField(max_length=10)
#         Subject = models.TextField()
#         Exam_Name = models.TextField(max_length=10)
#         Total_Questions = models.IntegerField()
#         duration = models.DurationField()
#         fullmark=models.IntegerField()
#         date=models.DateField()
 # generator/models.py


class UploadedText(models.Model):
    title=models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    class_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    exam_name = models.CharField(max_length=100)
    total_questions = models.IntegerField()
    duration = models.CharField(max_length=50)
    full_marks = models.IntegerField()
     