from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'credits', 'department_id']


class CreateUserParentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'username']


class CreateUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_type']


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_type', 'date_of_birth']


class CreateFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['faculty_type', 'department_id']
