from rest_framework import viewsets
from .models import Trip
from rest_framework.decorators import action
from rest_framework.response import Response
from .fetch import fetch_trips
from rest_framework import serializers

# Create your views here.
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    @action(detail=False, methods=['post']) 
    def fetch(self,request):
        fetch_trips()
        return Response({"message": "Trips fetched successfully."})
    


