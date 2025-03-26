from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    due_date = models.DateField()
    due_time = models.TimeField()
    completed = models.BooleanField()
    