from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^(?P<slug>[\w./-]+)/$', views.markdown, name='markdown'),
    #url(r'^(?P<slug>[\w./-]+)/$', views.page, name='page'),
)
