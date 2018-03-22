from django.conf.urls import url, include
from registration_system import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^user_display/$', core_views.UserDisplay.as_view(), name='display'),
    url(r'^logout/$', core_views.logout_view, name='registration_system_logout'),
    url(r'^create_course/$', core_views.CreateCourse.as_view(), name='create_course'),
    url(r'^create_course/prerequisites/(?P<course_id>\d+)/', core_views.CreatePrerequisite.as_view()
        , name='create_prerequisites'),
    url(r'^search_course/$', core_views.UpdateCourse.as_view(), name="search_course"),
    url(r'^create_section/$', core_views.CreateSection.as_view(), name="create_section"),
    url(r'^create_section/time_slot/$', core_views.create_time_slot, name='create_time_slot'),
    url(r'^search_section/$', core_views.UpdateSection.as_view(), name="search_section"),
    url(r'^create_user/$', core_views.CreateUser.as_view(), name="create_user"),
    url(r'^create_user/departments/$', core_views.get_departments, name="create_user_get_departments"),
    url(r'^search_user/$', core_views.UpdateUser.as_view(), name="search_user"),
    url(r'^create_hold/$', core_views.CreateHold.as_view(), name="create_hold"),
    url(r'^create_advising/$', core_views.CreateAdvising.as_view(), name="create_advising"),
    url(r'^change_semester/$', core_views.ChangeSemesterStatus.as_view(), name="change_semester")
]


