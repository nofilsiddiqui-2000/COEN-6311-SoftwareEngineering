# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    FACULTY_CHOICES = [
        ('ECE', 'Electrical and Computer Engineering'),
        ('MACS', 'Mathematics and Computer Science'),
        ('INSE', 'Information Systems Engineering'),
        ('Accounting', 'Accounting'),
    ]
    PROGRAM_CHOICES = [
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters'),
        ('Diploma', 'Diploma'),
    ]
    faculty_of_interest = forms.ChoiceField(choices=FACULTY_CHOICES, required=True)
    program_of_interest = forms.ChoiceField(choices=PROGRAM_CHOICES, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "faculty_of_interest", "program_of_interest")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    'faculty_of_interest': self.cleaned_data["faculty_of_interest"],
                    'program_of_interest': self.cleaned_data["program_of_interest"]
                }
            )
        return user
