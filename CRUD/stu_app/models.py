from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    enrollment_date = models.DateField()