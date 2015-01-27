from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from study_manager.serializers import *


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'appointments': reverse('appointment-list', request=request, format=format),
        'volunteers': reverse('volunteer-list', request=request, format=format),
        'surgeries': reverse('surgery-list', request=request, format=format),
        'gps': reverse('gps-list', request=request, format=format),
    })


class VolunteerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


class SurgeryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Surgery.objects.all()
    serializer_class = SurgerySerializer


class GPViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = GP.objects.all()
    serializer_class = GPSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


def index(request):
    return render(request, 'study_manager/home_page.html')
