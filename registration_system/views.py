import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from react.render import render_component
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
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
        os.path.join(os.getcwd(), 'registration_system', 'static', 'registration_system', 'js', 'Test.jsx'),
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


class UserDisplay(LoginRequiredMixin, generic.View):
    template_name ='registration_system/user_display.html'
    is_part_time_student = False
    is_full_time_student = False
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
                if student.has_part_time_student():
                    self.is_part_time_student = True
            elif userprofile.has_admin():
                self.is_admin = True
            elif userprofile.has_researcher():
                self.is_researcher = True

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
                    'is_researcher': self.is_researcher
                },
                to_static_markup=False,
        )
        return render(request, self.template_name, {'rendered': rendered, 'user': user})



