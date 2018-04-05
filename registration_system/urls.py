from django.conf.urls import url, include
from registration_system import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^user_display/$', core_views.UserDisplay.as_view(), name='display'),
    url(r'^logout/$', core_views.logout_view, name='registration_system_logout'),
    url(r'^declare_major/$', core_views.DeclareMajor.as_view(), name='declare_major'),
    url(r'^declare_minor/$', core_views.DeclareMinor.as_view(), name='declare_minor'),
    url(r'^student/view_student_schedule/$', core_views.StudentViewSchedule.as_view(),
        name='student_view_student_schedule'),
    url(r'^view_student_schedule/$', core_views.ViewStudentSchedule.as_view(), name='view_student_schedule'),
    url(r'^view_faculty_schedule/$', core_views.ViewFacultySchedule.as_view(), name='view_faculty_schedule'),
    url(r'^student/view_student_transcript/$', core_views.StudentViewStudentTranscript.as_view(),
        name='student_view_student_transcript'),
    url(r'^create_course/$', core_views.CreateCourse.as_view(), name='create_course'),
    url(r'^create_course/prerequisites/(?P<course_id>\d+)/', core_views.CreatePrerequisite.as_view()
        , name='create_prerequisites'),
    url(r'^search_course/$', core_views.UpdateCourse.as_view(), name="search_course"),
    url(r'^register_course/$', core_views.RegisterCourse.as_view(), name='register_course'),
    url(r'^drop_course/$', core_views.DropCourse.as_view(), name='drop_course'),
    url(r'^create_section/$', core_views.CreateSection.as_view(), name="create_section"),
    url(r'^create_section/time_slot/$', core_views.create_time_slot, name='create_time_slot'),
    url(r'^search_section/$', core_views.UpdateSection.as_view(), name="search_section"),
    url(r'^create_user/$', core_views.CreateUser.as_view(), name="create_user"),
    url(r'^create_user/departments/$', core_views.get_departments, name="create_user_get_departments"),
    url(r'^search_user/$', core_views.UpdateUser.as_view(), name="search_user"),
    url(r'^create_hold/$', core_views.CreateHold.as_view(), name="create_hold"),
    url(r'^view_hold/$', core_views.ViewHold.as_view(), name="view_hold"),
    url(r'^create_advising/$', core_views.CreateAdvising.as_view(), name="create_advising"),
    url(r'^view_advising/$', core_views.ViewAdvising.as_view(), name="view_advising"),
    url(r'^view_advisees/$', core_views.ViewAdvisees.as_view(), name="view_advisees"),
    url(r'^submit_grades/$', core_views.SubmitGrades.as_view(), name="submit_grades"),
    url(r'^change_semester/$', core_views.ChangeSemesterStatus.as_view(), name="change_semester"),
    url(r'^master_schedule/$', core_views.MasterScheduleView.as_view(), name="master_schedule"),
    url(r'^student_system_api/get_general_data/$', core_views.get_master_schedule_input_data, name="ms_get_general_data"),
    url(r'^student_system_api/get_schedule_data/(?P<attribute_flag>[\w\-]+)/(?P<search_value>[\w\-]+)/$',
        core_views.get_master_schedule_search_data, name='ms_get_schedule_data')
]


