from django.conf.urls import url, include
from registration_system import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^user_display/$', core_views.UserDisplay.as_view(), name='display')
]


