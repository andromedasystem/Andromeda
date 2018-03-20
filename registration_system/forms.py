from django import forms
from .models import *
from django.core.validators import MaxValueValidator, MinValueValidator


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'credits', 'department_id']


