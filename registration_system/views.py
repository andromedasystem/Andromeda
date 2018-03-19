import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from react.render import render_component
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateCourseForm
# Instead of using signals in views to create child models
# Just create the Instance of the parent class and an instance of the child class
# point the child's foreign key reference to the parent class. have to fo for Faculty and Student models


# Create your views here.
# @login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/student_system/")


def home(request):
    # return render(request, 'registration_system/index.html')
    rendered = render_component(
        os.path.join(os.getcwd(), 'registration_system', 'static', 'registration_system', 'js', 'intro-page.jsx'),
        {
            'test': 'REALLY LONG full test',
        },
        to_static_markup=False,
    )
    print(request.user)
    if request.user:
        user = request.user
    else:
        user = False
    # print(rendered)
    return render(request, 'registration_system/index.html', {'rendered': rendered, 'user': user})


# TODO: Finish Create Course, create permission_error  view and template
# TODO: Finish create course success view and template, figure out if the way I'm using redirect is optimal.
class CreateCourse(LoginRequiredMixin, generic.View):
    form_class = CreateCourseForm
    template_name ='registration_system/user_display.html'
    is_admin = False

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        if userprofile:
            if userprofile.has_admin():
                self.is_admin = True
            else:
                # redirect('registration_system/permissions_error/')
                pass

        departments = []
        for d in Department.objects.all():
            departments.append({
                'value': d.department_id,
                'name': d.name
            })

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'create-course-form.jsx'),
            {
                'is_admin': self.is_admin,
                'departments': departments,
                'url': '/student_system/create_course/'
            },
            to_static_markup=False,
        )
        return render(request, self.template_name, {'rendered': rendered, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            redirect('registration_system/success')
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            credits_value = form.cleaned_data['credits']
            department_id = form.cleaned_data['department_id']
            Course.objects.create(name=name, description=description, credits=credits_value, department_id=department_id)
            return redirect('student_system/create_course/success/')
        return redirect('student_system/create_course/')


class UserDisplay(LoginRequiredMixin, generic.View):
    template_name ='registration_system/user_display.html'
    is_part_time_student = False
    is_full_time_student = False
    is_part_time_faculty = False
    is_full_time_faculty = False
    is_faculty = False
    is_admin = False
    is_researcher = False

    def get(self, request):
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        if userprofile:
            if userprofile.has_student():
                student = Student.objects.get(student_id=userprofile)
                if student.has_full_time_student():
                    self.is_full_time_student = True
                elif student.has_part_time_student():
                    self.is_part_time_student = True
            elif userprofile.has_admin():
                self.is_admin = True
            elif userprofile.has_researcher():
                self.is_researcher = True
            elif userprofile.has_faculty():
                faculty = Faculty.objects.get(faculty_id=userprofile)
                print(faculty)
                self.is_faculty = True

        rendered = render_component(
                os.path.join(os.getcwd(), 'registration_system', 'static',
                             'registration_system', 'js', 'user-display.jsx'),
                {
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'is_admin': self.is_admin,
                    'is_full_time_student': self.is_full_time_student,
                    'is_part_time_student': self.is_part_time_student,
                    'is_faculty': self.is_faculty,
                    'is_researcher': self.is_researcher
                },
                to_static_markup=False,
        )
        return render(request, self.template_name, {'rendered': rendered, 'user': user})



