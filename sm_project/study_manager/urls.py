from study_manager import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'volunteers', views.VolunteerViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'surgeries', views.SurgeryViewSet)
router.register(r'gps', views.GPViewSet)

urlpatterns = patterns('',
    url(r'^$', 'study_manager.views.index', name='index'),
    url(r'^api/', include(router.urls)),
)
