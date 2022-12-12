from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import Event, Accommodation, Host, Location

class EventView(ViewSet):
    def retrieve(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request):
        new_event = Event()
        new_event.host = Host.objects.get(pk=request.data["hostId"])
        new_event.date = request.data["date"]
        new_event.time = request.data["time"]
        new_event.accommodation = Accommodation.objects.get(pk=request.data["accommodationId"])
        new_event.capacity = request.data["capacity"]
        new_event.location = Location.objects.get(pk=request.data["locationId"])
        new_event.save()

        serializer = EventSerializer(new_event)

        return Response(serializer.data)

    def update(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.host = Host.objects.get(pk=request.data["hostId"])
        event.date = request.data["date"]
        event.time = request.data["time"]
        event.accommodation = Accommodation.objects.get(pk=request.data["accommodationId"])
        event.capacity = request.data["capacity"]
        event.location = Location.objects.get(pk=request.data["locationId"])
        event.save()

    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    Arguments:
        serializers
    """
    class Meta:
        model = Event
        fields = ('id', 'host', 'date', 'time', 'accommodation', 'capacity', 'location')
