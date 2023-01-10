from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import Event, Accommodation, Host, Artist
from rest_framework.decorators import action


class EventView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single event"""

        event = Event.objects.get(pk=pk)
        if request.auth.user.id == event.host.user.id:
            attendees = [artist.user.username for artist in event.attendees.all()]
            response = {
                "id": event.id,
                "host": event.host.id,
                "name": event.name,
                "date": event.date,
                "time": event.time,
                "accommodation_id": event.accommodation.id,
                "accommodation_name": event.accommodation.accommodation_name,
                "details": event.details,
                "capacity": event.capacity,
                "username": event.host.user.username,
                "attendees": attendees,
                "my_event": True
            }
        else:
            attendees = [artist.user.username for artist in event.attendees.all()]
            response = {
                "id": event.id,
                "host": event.host.id,
                "name": event.name,
                "date": event.date,
                "time": event.time,
                "accommodation_id": event.accommodation.id,
                "accommodation_name": event.accommodation.accommodation_name,
                "username": event.host.user.username,
                "details": event.details,
                "capacity": event.capacity,
                "attendees": attendees,
                "my_event": False
            }
        return Response(response, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get all event types

        Returns:
            Response -- JSON serialized list of event types
        """
        if request.auth.user.is_staff:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)
        else:
            artist = Artist.objects.get(user=request.auth.user)
            events = Event.objects.all()
            # Set the `joined` property on every event
            for event in events:
                # Check to see if the artist is in the attendees list on the event
                event.joined = artist in event.attendees.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        """Post request for a artist to sign up for an event"""

        artist = Artist.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.add(artist)
        return Response({'message': 'Artist added'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def leave(self, request, pk):
        """DELETE request for a artist to leave an event"""

        artist = Artist.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.attendees.remove(artist)
        return Response({'message': 'Artist has left event'}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST operations"""
        # Uses the token passed in the `Authorization` header
        new_event = Event()
        new_event.host = Host.objects.get(user=request.auth.user.id)
        new_event.name = request.data["name"]
        new_event.date = request.data["date"]
        new_event.time = request.data["time"]
        new_event.details = request.data["details"]
        new_event.accommodation = Accommodation.objects.get(
            pk=request.data["accommodationId"])
        new_event.capacity = request.data["capacity"]
        new_event.save()

        serializer = EventSerializer(new_event)

        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for an event"""

        event = Event.objects.get(pk=pk)
        event.host = Host.objects.get(user=request.auth.user.id)
        event.name = request.data["name"]
        event.date = request.data["date"]
        event.time = request.data["time"]
        event.details = request.data["details"]
        event.accommodation = Accommodation.objects.get(
            pk=request.data["accommodation"])
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
        fields = ('id', 'host', 'name', 'date', 'time', 'details',
                  'accommodation', 'capacity', 'attendees', 'joined', 'attendee_count')
        depth = 3
