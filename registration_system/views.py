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


class ChangeSemesterStatus(LoginRequiredMixin, generic.View):
    template_name = 'registration_system/change_semester.html'
    is_admin = False

    def get(self, request, *args, **kwargs):
        user = request.user
        userprofile = UserProfile.objects.get(user=user)

        if userprofile:
            if userprofile.has_admin():
                self.is_admin = True
            else:
                redirect('/student_system/')

        semesters = Semester.objects.all()

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_admin': self.is_admin,
                'header_text': 'Create Advising'
            },
            to_static_markup=False,
        )
        context = {
            'rendered': rendered,
            'semesters': semesters
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {
            'is_successful': False
        }
        if request.is_ajax():
            semester_id = request.POST.get('semester_id')
            status = request.POST.get('status')
            semester = Semester.objects.get(pk=int(semester_id))
            semester.status = status
            semester.save()
            data['is_successful'] = True
        else:
            data['is_successful'] = False
        return JsonResponse(data)


class CreateAdvising(LoginRequiredMixin, generic.View):
    template_name = 'registration_system/create_advising.html'
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
            # user = User.objects.filter(Q(username=username) | Q(email=email) | Q(first_name=first_name) |
            #                            Q(last_name=last_name))
            user = User.objects.get(first_name=first_name, last_name=last_name)

            is_advised = True
            try:
                student = Student.objects.get(pk=int(user.userprofile.student.student_id_id))
                advising = Advising.objects.get(student_id=student)
            except Advising.DoesNotExist:
                is_advised = False

            faculty = []
            for f in Faculty.objects.raw("SELECT u.first_name, u.last_name, f.faculty_id_id "
                                         "FROM registration_system_faculty AS f, auth_user as u, registration_system_userprofile as up "
                                         "WHERE up.user_id = u.id "
                                         "AND up.id = f.faculty_id_id"):
                faculty.append({
                    'first_name': f.first_name,
                    'last_name': f.last_name,
                    'full_name': f.first_name + " " + f.last_name,
                    'faculty_id': f.faculty_id_id
                })

            data = {
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'isAdvised': is_advised,
                'faculty_array': faculty
            }

            return HttpResponse(json.dumps(data), content_type="application/json")

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_admin': self.is_admin,
                'header_text': 'Create Advising'
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
            faculty_id = request.POST.get('faculty')
            faculty = Faculty.objects.get(pk=int(faculty_id))
            # = request.POST.get('hold')
            is_update = request.POST.get('isUpdate')
            student = Student.objects.get(student_id__user_id=user_id)
            if is_update is not None:
                # TODO: Update advising
                advising = Advising.objects.get(student_id=student)
                advising.faculty_id = faculty
                advising.save()
                data['is_successful'] = True
                return JsonResponse(data)
            advising = Advising.objects.create(faculty_id=faculty, student_id=student)
            data['is_successful'] = True
        else:
            data['is_successful'] = False
        return JsonResponse(data)


class ViewHold(LoginRequiredMixin, generic.View):
    template_name = 'registration_system/view_hold.html'
    is_student = False

    def get(self, request, *args, **kwargs):
        user = request.user
        userprofile = UserProfile.objects.get(user=user)

        if userprofile:
            if userprofile.has_student():
                self.is_student = True
            else:
                redirect('/student_system/')
        hold = None
        try:
            student = Student.objects.get(pk=int(user.userprofile.student.student_id_id))
            hold = StudentHold.objects.get(student_id=student)
        except StudentHold.DoesNotExist:
            hold = None

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_student': self.is_student,
                'header_text': 'View Hold'
            },
            to_static_markup=False,
        )

        context = {
            'rendered': rendered,
            'holds': hold
        }

        return render(request, self.template_name, context)


class ViewAdvising(LoginRequiredMixin, generic.View):
    template_name = 'registration_system/view_adviser.html'
    is_student = False

    def get(self, request, *args, **kwargs):
        user = request.user
        userprofile = UserProfile.objects.get(user=user)

        if userprofile:
            if userprofile.has_student():
                self.is_student = True
            else:
                redirect('/student_system/')
        advising = None
        faculty_name = None
        try:
            student = Student.objects.get(pk=int(user.userprofile.student.student_id_id))
            advising = Advising.objects.get(student_id=student)
            faculty_name = advising.faculty_id.faculty_id.user.first_name + ' ' + advising.faculty_id.faculty_id.user.last_name
        except Advising.DoesNotExist:
            advising = None
            faculty_name = None

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_student': self.is_student,
                'header_text': 'View Adviser'
            },
            to_static_markup=False,
        )

        context = {
            'rendered': rendered,
            'advising': advising,
            'faculty_name': faculty_name

        }

        return render(request, self.template_name, context)


class CreateHold(LoginRequiredMixin, generic.View):
    template_name = 'registration_system/create_hold.html'
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
            # user = User.objects.filter(Q(username=username) | Q(email=email) | Q(first_name=first_name) |
            #                            Q(last_name=last_name))
            user = User.objects.get(first_name=first_name, last_name=last_name)

            is_held = False
            try:
                student = Student.objects.get(pk=int(user.userprofile.student.student_id_id))
                hold = StudentHold.objects.get(student_id=student)
                is_held = True
            except StudentHold.DoesNotExist:
                is_held = False

            data = {
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'isHeld': is_held
            }

            return HttpResponse(json.dumps(data), content_type="application/json")

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_admin': self.is_admin,
                'header_text': 'Create Hold'
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
            hold = request.POST.get('hold')
            is_remove = request.POST.get('isRemove')
            user = User.objects.get(pk=int(user_id))
            if is_remove is not None:
                student = Student.objects.get(pk=int(user.userprofile.student.student_id_id))
                student_hold = StudentHold.objects.get(student_id=student)
                student_hold.delete()
                data['is_successful'] = True
                return JsonResponse(data)
            hold = Hold.objects.create(name=hold)

            student_id = user.userprofile.student.student_id_id
            student = Student.objects.get(pk=int(student_id))
            student_hold = StudentHold.objects.create(student_id=student, hold_id=hold)
            data['is_successful'] = True
        else:
            data['is_successful'] = False
        return JsonResponse(data)


class UpdateSection(LoginRequiredMixin, generic.View):
    template_name = 'registration_system/search_section.html'
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
            course_id = request.GET.get('course_id')
            days_id = request.GET.get('days_id')
            faculty_id = request.GET.get('faculty_id')
            section = None
            print(department_id)
            if department_id is not None:
                section = Section.objects.filter(course_id__department_id_id=int(department_id))
            elif course_id is not None:
                section = Section.objects.filter(course_id=int(course_id))
            elif days_id is not None:
                section = Section.objects.filter(time_slot_id__days_id=int(days_id))
            elif faculty_id is not None:
                section = Section.objects.filter(faculty_id=int(faculty_id))

            faculty = []
            for f in Faculty.objects.raw("SELECT u.first_name, u.last_name, f.faculty_id_id "
                                         "FROM registration_system_faculty AS f, auth_user as u, registration_system_userprofile as up "
                                         "WHERE up.user_id = u.id "
                                         "AND up.id = f.faculty_id_id"):
                faculty.append({
                    'first_name': f.first_name,
                    'last_name': f.last_name,
                    'full_name': f.first_name + " " + f.last_name,
                    'faculty_id': f.faculty_id_id
                })
            departments = []
            for d in Department.objects.all():
                departments.append({
                    'department_id': d.department_id,
                    'department_name': d.name
                })
            time_periods = []
            for t in Period.objects.all():
                time_periods.append({
                    'time_period_id': t.period_id,
                    'time_range': t.start_time.strftime('%H:%M %p') + ' ' + t.end_time.strftime('%H:%M %p')
                })
            meeting_days = []
            for m in MeetingDays.objects.all():
                meeting_days.append({
                    'days_id': m.days_id,
                    'day_1': m.day_1,
                    'day_2': m.day_2,
                    'day_range': m.day_1 + " " + m.day_2
                })
            buildings = []
            for b in Building.objects.all():
                buildings.append({
                    'building_id': b.building_id,
                    'building_name': b.name
                })
            rooms = []
            for arrgh in Room.objects.all():
                rooms.append({
                    'rooms_id': arrgh.room_id,
                    'room_number': arrgh.room_number
                })

            section_array = []
            for s in section:
                print(s)
                print("here\n")
                data = {
                    'faculty_array': faculty,
                    'departments_array': departments,
                    'time_periods_array': time_periods,
                    'meeting_days_array': meeting_days,
                    'buildings_array': buildings,
                    'rooms_array': rooms,
                    'section_id': s.section_id,
                    'course_id': s.course_id.course_id,
                    'course_department': s.course_id.department_id.name,
                    'course_name': s.course_id.name,
                    'faculty_id': s.faculty_id.faculty_id_id,
                    'faculty_name': s.faculty_id.faculty_id.user.first_name + " " + s.faculty_id.faculty_id.user.last_name,
                    'credits': s.course_id.credits,
                    'seats_taken': s.seats_taken,
                    'seating_capacity': s.room_id.capacity,
                    'time_slot_id': s.time_slot_id.time_slot_id,
                    'time_period_id': s.time_slot_id.period_id.period_id,
                    'time_period_range': s.time_slot_id.period_id.start_time.strftime('%H:%M %p')
                                         + " " + s.time_slot_id.period_id.end_time.strftime('%H:%M %p'),
                    'meeting_days_id': s.time_slot_id.days_id.days_id,
                    'meeting_days': s.time_slot_id.days_id.day_1 + s.time_slot_id.days_id.day_2,
                    'building_id': s.room_id.building_id.building_id,
                    'building_name': s.room_id.building_id.name,
                    'room_id': s.room_id.room_id,
                    'room_number': s.room_id.room_number
                }
                section_array.append(data)

            return HttpResponse(json.dumps(section_array), content_type="application/json")

        rendered = render_component(
            os.path.join(os.getcwd(), 'registration_system', 'static',
                         'registration_system', 'js', 'nav-holder.jsx'),
            {
                'is_admin': self.is_admin,
                'header_text': 'Update Section'
            },
            to_static_markup=False,
        )
        departments = Department.objects.all()
        days = MeetingDays.objects.all()
        course = Course.objects.all()
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

        context = {
            'rendered': rendered,
            'departments': departments,
            'days': days,
            'faculty': faculty,
            'courses': course
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {
            'is_successful': False
        }
        if request.is_ajax():
            faculty_id = request.POST.get('faculty')
            faculty = Faculty.objects.get(pk=int(faculty_id))
            time_period = request.POST.get('time_period')
            days = request.POST.get('days')
            time_slot = TimeSlot.objects.get(days_id=int(days), period_id=int(time_period))
            building_id = request.POST.get('building')
            building = Building.objects.get(pk=int(building_id))
            room_id = request.POST.get('room')
            room = Room.objects.get(pk=int(room_id))
            section_id = request.POST.get('section_id')
            section = Section.objects.get(pk=int(section_id))
            section.faculty_id = faculty
            section.time_slot_id = time_slot
            section.building_id = building
            section.room_id = room
            section.save()
            data['is_successful'] = True
        else:
            data['is_successful'] = False
        return JsonResponse(data)


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
            building_number = request.GET.get('building_id')
            if building_number is not None:
                rooms = Room.objects.filter(building_id__building_id=int(building_number))
                rooms_array = []
                for r in rooms:
                    data = {
                        'room_id': r.room_id,
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

    def post(self, request, *args, **kwargs):
        data = {
            'is_successful': False
        }
        if request.is_ajax():
            department = request.POST.get('department')
            course_id = request.POST.get('course')
            course = Course.objects.get(pk=int(course_id))
            faculty_id = request.POST.get('faculty')
            faculty = Faculty.objects.get(pk=int(faculty_id))
            building_id = request.POST.get('building')
            building = Building.objects.get(pk=int(building_id))
            room_id = request.POST.get('room')
            room = Room.objects.get(pk=int(room_id))
            semester_id = request.POST.get('semester')
            semester = Semester.objects.get(pk=int(semester_id))
            days_id = request.POST.get('days')
            days = MeetingDays.objects.get(pk=int(days_id))
            time_period_id = request.POST.get('time_period')
            time_period = Period.objects.get(pk=int(time_period_id))
            time_slot = None
            try:
                time_slot = TimeSlot.objects.get(days_id=days, period_id=time_period)
            except TimeSlot.DoesNotExist:
                time_slot = TimeSlot.objects.create(days_id=days, period_id=time_period)
            section = Section.objects.create(course_id=course, time_slot_id=time_slot,
                                             faculty_id=faculty, semester_id=semester, room_id=room)
            data['is_successful'] = True
        else:
            data['is_successful'] = False
        return JsonResponse(data)


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
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
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
                        if request.POST.get("credits") != 0:
                            credits_variable = request.POST.get("credits")
                            user_profile.user_type = 'S'
                            user_profile.save()
                            student = Student.objects.create(student_id=user_profile, date_of_birth=date_of_birth,
                                                             student_type=student_type.strip())
                            if student.student_type == 'F':
                                student.fulltimestudent.credits = int(credits_variable)
                                student.fulltimestudent.save()
                            else:
                                student.parttimestudent.credits = int(credits_variable)
                                student.parttimestudent.save()
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
            message = "Ajax"
            course_id = request.POST.get('courseID')
            prerequisites = json.loads(request.POST.get('prerequisites'))
            course = Course.objects.get(pk=int(course_id))
            for p in prerequisites:
                prerequisite_course = Course.objects.get(pk=int(p))
                Prerequisite.objects.create(course_id=course, course_required_id=prerequisite_course)
        else:
            message = "No Ajax"
        return HttpResponse(message)


# TODO: Finish Create Course, create permission_error  view and template
# TODO: Finish create course success view and template, figure out if the way I'm using redirect is optimal.
class CreateCourse(LoginRequiredMixin, generic.View):
    form_class = CreateCourseForm
    template_name = 'registration_system/create_course.html'
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
            return redirect('create_prerequisites', course_id=course.course_id)
        return redirect('/student_system/create_course/')


class UserDisplay(LoginRequiredMixin, generic.View):
    template_name = 'registration_system/user_display.html'
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
        is_student = self.is_full_time_student or self.is_part_time_student

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
                'is_researcher': self.is_researcher,
                'is_student': is_student,
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


def create_time_slot(request):
    data = {
        'is_successful': False
    }
    if request.is_ajax():
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        Period.objects.create(start_time=start_time, end_time=end_time)
        data['is_successful'] = True
    else:
        data['is_successful'] = False
    return JsonResponse(data)
