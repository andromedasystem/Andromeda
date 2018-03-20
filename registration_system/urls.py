from django.conf.urls import url, include
from registration_system import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^user_display/$', core_views.UserDisplay.as_view(), name='display'),
    url(r'^logout/$', core_views.logout_view, name='registration_system_logout'),
    url(r'^create_course/$', core_views.CreateCourse.as_view(), name='create_course'),
    url(r'^create_course/prerequisites/(?P<course_id>\d+)/', core_views.CreatePrerequisite.as_view()
        , name='create_prerequisites'),
    url(r'^create_user/$', core_views.CreateUser.as_view(), name="create_user")
]


