from rest_framework import viewsets
from .models import Trip, Activities
from .serializers import TripSerializer, ActivitiesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .fetch import fetch_trips, fetch_activities
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated]) 
    def fetch(self,request):
        fetch_trips()
        return Response({"message": "Trips fetched successfully."})
    

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = "__all__"
        
class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def fetch(self,request):
        fetch_activities()
        return Response(
            {'message':'Activities fetched successfully.'}
        )