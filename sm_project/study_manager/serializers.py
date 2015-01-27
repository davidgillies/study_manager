from django.forms import widgets
from rest_framework import serializers
from study_manager.models import Volunteer, Appointment, Surgery, GP


class VolunteerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Volunteer
        exclude = ("user",)


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment


class SurgerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Surgery


class GPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GP