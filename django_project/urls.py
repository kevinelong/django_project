from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings  # New Import
from django.conf.urls.static import static  # New Import
import myapp.views

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'django_project_17.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', myapp.views.main),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^myapp/', include('myapp.urls')),  # ADD THIS NEW TUPLE!
                       )

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )

