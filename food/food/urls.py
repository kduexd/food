from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^area/', include('area.urls', namespace='area')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^.*', include('main.urls')),
]
