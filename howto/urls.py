from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webpage.urls', namespace='webpage')),
    url(r'^blog/', include('staticblog.urls', namespace='staticblog'))
]
