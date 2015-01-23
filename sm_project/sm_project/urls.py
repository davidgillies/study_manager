from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'mrc_dashboard.views.index', name='home'),
    url(r'^study_manager/', include('study_manager.urls'),
        name='study_manager'),
)
