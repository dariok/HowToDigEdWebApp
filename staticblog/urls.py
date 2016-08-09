from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^(?P<slug>[\w./-]+)/$', views.render_static_page, name='render_static_page'),
    #url(r'^(?P<slug>[\w./-]+)/$', views.page, name='page'),
)
