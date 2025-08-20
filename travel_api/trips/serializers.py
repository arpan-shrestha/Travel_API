from rest_framework import serializers
from .models import Trip, Activities

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        field = "__all__"

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        field = "__all__"