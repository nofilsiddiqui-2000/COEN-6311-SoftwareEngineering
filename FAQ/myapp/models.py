from django.db import models
from django.contrib.auth.models import User

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()


# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty_of_interest = models.CharField(max_length=50, choices=[
        ('ECE', 'Electrical and Computer Engineering'),
        ('MACS', 'Mathematics and Computer Science'),
        ('INSE', 'Information Systems Engineering'),
        ('Accounting', 'Accounting'),
    ])
    program_of_interest = models.CharField(max_length=50, choices=[
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters'),
        ('Diploma', 'Diploma'),
    ])

    def __str__(self):
        return self.user.username
  