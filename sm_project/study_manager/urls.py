from study_manager import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # url(r'^$', views.Index.as_view(), name='index'),
    url(r'^$', 'study_manager.views.index', name='index'),
)