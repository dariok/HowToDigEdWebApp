from django.conf.urls import url, include
from . import views

urlpatterns = [
url(r'^$', views.start_view, name="start"),
url(r'^login/$', views.user_login, name='user_login'),
url(r'^accounts/login/$', views.user_login, name='user_login'),
url(r'^logout/$', views.user_logout, name='user_logout'),
]