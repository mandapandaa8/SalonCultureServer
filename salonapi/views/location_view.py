from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import Location
from django.contrib.auth.models import User

class LocationView(ViewSet):
    def retrieve(self, request, pk):
        location = Location.objects.get(pk=pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def list(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        location = Location.objects.get(pk=pk)
        location.city = request.data["city"]
        location.state = request.data["state"]

        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        location = Location.objects.get(pk=pk)
        location.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class LocationSerializer(serializers.ModelSerializer):
    """JSON serializer for locations
    Arguments:
        serializers
    """
    class Meta:
        model = Location
        fields = ('id', 'city', 'state')