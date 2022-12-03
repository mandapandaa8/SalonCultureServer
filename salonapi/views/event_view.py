from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import Event

class EventView(ViewSet):
    def retrieve(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.host_id = request.data["hostId"]
        event.date = request.data["date"]
        event.time = request.data["time"]
        event.accommodation_id = request.data["accommodationId"]
        event.capacity = request.data["capacity"]
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
        fields = ('id', 'host_id', 'date', 'time', 'accommodation_id', 'capacity')
