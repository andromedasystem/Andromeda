import os, json
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
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
from django.db.models import Q
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import *
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


# TODO: Create Post method to create a course
class CreateSection(LoginRequiredMixin, generic.View):
    template_name = 'registration_system/create_section.html'
    is_admin = False

    def get(self, request, *args, **kwargs):
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        if userprofile:
            if userprofile.has_admin():
                self.is_admin = True
            else:
                redirect('/student_system/')

        departments = Department.objects.all()
        buildings = Building.objects.all()
        semester = Semester.objects.all()
        days = MeetingDays.objects.all()
        time_period = Period.objects.all()
        faculty = []
        for f in Faculty.objects.raw("SELECT u.first_name, u.last_name, f.faculty_id_id "
                                     "FROM registration_system_faculty AS f, auth_user as u, registration_system_userprofile as up "
                                     "WHERE up.user_id = u.id "
                                     "AND up.id = f.faculty_id_id"):
            faculty.append({
                'first_name': f.first_name,
                'last_name': f.last_name,
                'faculty_id': f.faculty_id_id
            })

        if request.is_ajax():
            building_number = request.GET.get('building_number')
            if building_number is not None:
                rooms = Room.objects.filter(bulding_id=building_number)
                rooms_array = []
                for r in rooms:
                    data = {
                        'room_number': r.room_number,
                        'room_type': r.type,
                        'room_capacity': r.capacity
                    }
                    rooms_array.append(data)
                    return HttpResponse(json.dumps(rooms_array), content_type="application/json")
            else:
                department_id = request.GET.get('department_id')
                department_name = request.GET.get('department_name')

                # user = User.objects.filter(Q(username=username) | Q(email=email) | Q(first_name=first_name) |
                #                            Q(last_name=last_name))
                courses = Course.objects.filter(department_id=int(department_id))
                course_array = []
                for c in courses:
                    print(c)
                    data = {
                        'course_id': c.course_id,
                        'department_name': department_name,
                        'department_id': department_id,
                        'course_name': c.name,
                        'course_description': c.description,
                        'course_credits': c.credits
                    }
                    course_array.append(data)
                return HttpResponse(json.dumps(course_array), content_type="application/json")

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_admin': self.is_admin,
                'header_text': 'Create Section'
            },
            to_static_markup=False,
        )
        return render(request, self.template_name, {'rendered': rendered, 'departments': departments,
                                                    'buildings': buildings, 'semesters': semester, 'days': days,
                                                    'time_periods': time_period, 'faculty': faculty})


class UpdateCourse(LoginRequiredMixin, generic.View):
    template_name = 'registration_system/search_course.html'
    is_admin = False

    def get(self, request, *args, **kwargs):
        user = request.user
        userprofile = UserProfile.objects.get(user=user)

        if userprofile:
            if userprofile.has_admin():
                self.is_admin = True
            else:
                redirect('/student_system/')

        if request.is_ajax():
            department_id = request.GET.get('department_id')
            department_name = request.GET.get('department_name')
            # user = User.objects.filter(Q(username=username) | Q(email=email) | Q(first_name=first_name) |
            #                            Q(last_name=last_name))
            courses = Course.objects.filter(department_id=int(department_id))
            course_array = []
            for c in courses:
                print(c)
                data = {
                    'course_id': c.course_id,
                    'department_name': department_name,
                    'department_id': department_id,
                    'course_name': c.name,
                    'course_description': c.description,
                    'course_credits': c.credits
                }
                course_array.append(data)
            return HttpResponse(json.dumps(course_array), content_type="application/json")

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_admin': self.is_admin,
                'header_text': 'Search Course'
            },
            to_static_markup=False,
        )
        departments = Department.objects.all()
        context = {
            'rendered': rendered,
            'departments': departments
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {
            'is_successful': False
        }
        if request.is_ajax():
            course_id = request.POST.get('courseID')
            course_name = request.POST.get('courseName')
            course_description = request.POST.get('course_description')
            course_credits = request.POST.get('course_credits')
            course = Course.objects.get(pk=int(course_id))
            course.name = course_name
            course.description = course_description
            course.credits = course_credits
            course.save()
            data['is_successful'] = True
        else:
            data['is_successful'] = False
        return JsonResponse(data)


class UpdateUser(LoginRequiredMixin, generic.View):
    template_name = 'registration_system/search_user.html'
    is_admin = False

    def get(self, request, *args, **kwargs):
        user = request.user
        userprofile = UserProfile.objects.get(user=user)

        if userprofile:
            if userprofile.has_admin():
                self.is_admin = True
            else:
                redirect('/student_system/')

        if request.is_ajax():
            first_name = request.GET.get('first_name')
            last_name = request.GET.get('last_name')
            email = request.GET.get('email')
            username = request.GET.get('username')
            # user = User.objects.filter(Q(username=username) | Q(email=email) | Q(first_name=first_name) |
            #                            Q(last_name=last_name))
            if username:
                user = User.objects.filter(username=username)
            elif email:
                user = User.objects.filter(email=email)
            elif first_name:
                user = User.objects.filter(first_name=first_name)
            elif last_name:
                user = User.objects.filter(last_name=last_name)
            user_array = []
            for u in user:
                print(u)
                user_profile = UserProfile.objects.get(user_id=u.id)
                data = {
                    'user_id': u.id,
                    'username': u.username,
                    'email': u.email,
                    'first_name': u.first_name,
                    'last_name': u.last_name,
                    'user_type': user_profile.user_type
                }
                user_array.append(data)
            return HttpResponse(json.dumps(user_array), content_type="application/json")

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_admin': self.is_admin,
                'header_text': 'Search User'
            },
            to_static_markup=False,
        )

        context = {
            'rendered': rendered
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {
            'is_successful': False
        }
        if request.is_ajax():
            user_id = request.POST.get('userID')
            user = User.objects.get(pk=int(user_id))
            user.delete()
            data['is_successful'] = True
        else:
            data['is_successful'] = False
        return JsonResponse(data)


# TODO: Create Post Method and create get method for Department RESTful query
class CreateUser(LoginRequiredMixin, generic.View):
    user_form_class = CreateUserParentForm
    user_profile_form_class = CreateUserProfileForm
    student_form_class = CreateStudentForm
    faculty_form_class = CreateFacultyForm
    template_name = 'registration_system/create_user.html'
    is_admin = False

    def get(self, request, *args, **kwargs):
        user = request.user
        userprofile = UserProfile.objects.get(user=user)

        if userprofile:
            if userprofile.has_admin():
                self.is_admin = True
            else:
                redirect('/student_system/')

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_admin': self.is_admin,
                'header_text': 'Create User'
            },
            to_static_markup=False,
        )

        context = {
            'rendered': rendered
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {
            'is_successful': False
        }
        if request.POST:

            user_form = self.user_form_class(request.POST, instance=User())
            user_profile_form = self.user_profile_form_class(request.POST, instance=UserProfile())
            print(user_form.errors)
            print(user_profile_form.errors)
            if user_form.is_valid() and user_profile_form.is_valid():
                username = user_form.cleaned_data['username']
                password = user_form.cleaned_data['password']
                first_name = user_form.cleaned_data['first_name']
                last_name = user_form.cleaned_data['last_name']
                email = user_form.cleaned_data['email']
                user_type = user_profile_form.cleaned_data['user_type']
                user = User.objects.create(username=username, password=password, first_name=first_name,
                                           last_name=last_name, email=email)
                user_profile = user.userprofile
                if user_type == 'A':
                    user_profile.user_type = 'A'
                    user_profile.save()
                    admin = Admin.objects.create(admin_id=user_profile)
                    data['is_successful'] = True
                    print(admin)
                elif user_type == 'R':
                    user_profile.user_type = 'R'
                    user_profile.save()
                    researcher = Researcher.objects.create(researcher_id=user_profile)
                    data['is_successful'] = True
                elif user_type == 'S':
                    student_form = self.student_form_class(request.POST, instance=Student())
                    if student_form.is_valid():
                        date_of_birth = student_form.cleaned_data['date_of_birth']
                        student_type = student_form.cleaned_data['student_type']
                        credits_variable = None
                        if request.POST.get("credits", "") != 0:
                            credits_variable = request.POST.get("credits", "")
                            user_profile.user_type = 'S'
                            user_profile.save()
                            student = Student.objects.create(student_id=user_profile, date_of_birth=date_of_birth,
                                                             student_type=student_type.strip(),
                                                             credits=int(credits_variable))
                        else:
                            user_profile.user_type = 'S'
                            user_profile.save()
                            student = Student.objects.create(student_id=user_profile, date_of_birth=date_of_birth,
                                                             student_type=student_type.strip())
                        data['is_successful'] = True
                elif user_type == 'F':
                    faculty_form = self.faculty_form_class(request.POST, instance=Faculty())
                    if faculty_form.is_valid():
                        department_id = faculty_form.cleaned_data['department_id']
                        faculty_type = faculty_form.cleaned_data['faculty_type']
                        user_profile.user_type = 'F'
                        user_profile.save()
                        faculty = Faculty.objects.create(faculty_id=user_profile, department_id=department_id,
                                                         faculty_type=faculty_type.strip())
                        data['is_successful'] = True
                        print(faculty)

                # data['errors'] = self.user_form_class.errors if self.user_form_class.errors else None
                # data['errors'] = self.user_profile_form_class.errors if self.user_profile_form_class.errors else None
                # data['errors'] = self.faculty_form_class.errors if self.faculty_form_class.errors else None
                # data['errors'] = self.student_form_class.errors if self.student_form_class.errors else None
                return JsonResponse(data)


class CreatePrerequisite(LoginRequiredMixin, generic.View):
    template_name = 'registration_system/create_prerequisite.html'
    is_admin = False

    def get(self, request, course_id, *args, **kwargs):
        user = request.user
        userprofile = UserProfile.objects.get(user=user)

        if userprofile:
            if userprofile.has_admin():
                self.is_admin = True
            else:
                redirect('/student_system/')

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_admin': self.is_admin,
                'header_text': 'Create Prerequisites'
            },
            to_static_markup=False,
        )

        courses = Course.objects.all()
        context = {
            'courses': courses,
            'rendered': rendered,
            'value': course_id
        }
        return render(request, self.template_name, context)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            message ="Ajax"
            course_id = request.POST.get('courseID')
            prerequisites = json.loads(request.POST.get('prerequisites'))
            course = Course.objects.get(pk=int(course_id))
            for p in prerequisites:
                prerequisite_course = Course.objects.get(pk=int(p))
                Prerequisite.objects.create(course_id=course, course_required_id=prerequisite_course)
        else:
            message ="No Ajax"
        return HttpResponse(message)


# TODO: Finish Create Course, create permission_error  view and template
# TODO: Finish create course success view and template, figure out if the way I'm using redirect is optimal.
class CreateCourse(LoginRequiredMixin, generic.View):
    form_class = CreateCourseForm
    template_name ='registration_system/create_course.html'
    is_admin = False

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        user = request.user
        userprofile = UserProfile.objects.get(user=user)
        if userprofile:
            if userprofile.has_admin():
                self.is_admin = True
            else:
                redirect('/student_system/')

        departments = Department.objects.all()

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_admin': self.is_admin,
                'header_text': 'Create Course'
            },
            to_static_markup=False,
        )
        return render(request, self.template_name, {'rendered': rendered, 'form': form, 'departments': departments})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            credits_value = form.cleaned_data['credits']
            department_id = form.cleaned_data['department_id']
            course = Course.objects.create(name=name, description=description, credits=credits_value,
                                           department_id=department_id)
            return redirect('create_prerequisites',  course_id=course.course_id)
        return redirect('/student_system/create_course/')


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


def get_departments(request):
    departments = Department.objects.all()
    department_array = []
    for d in departments:
        data = {
            'department_id': d.department_id,
            'department_name': d.name
        }
        department_array.append(data)
    return HttpResponse(json.dumps(department_array), content_type="application/json")



