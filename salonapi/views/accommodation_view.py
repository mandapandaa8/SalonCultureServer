from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import Accommodation

class AccommodationView(ViewSet):
    """Salon view for Accommodations"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Accommodation

        Returns:
            Response -- JSON serialized Accommodation instance
        """

        accommodation = Accommodation.objects.get(pk=pk)
        serializer = AccommodationSerializer(accommodation)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to Accommodations resource

        Returns:
            Response -- JSON serialized list of Accommodations
        """

        accommodations = Accommodation.objects.order_by('accommodation_name').all()
        serializer = AccommodationSerializer(accommodations, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Accommodation instance
        """

        new_accommodation = Accommodation()
        new_accommodation.accommodation_name = request.data["accommodationName"]
        new_accommodation.save()

        serializer = AccommodationSerializer(new_accommodation)

        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for an Accommodation

        Returns:
            Response -- Empty body with 204 status code
        """

        accommodation = Accommodation.objects.get(pk=pk)
        accommodation.accommodation_name = request.data["accommodationName"]
        accommodation.save()

        return Response( status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single Accommodation

        Returns:
            Response -- 200, 404, or 500 status code
        """

        try:
            accommodation = Accommodation.objects.get(pk=pk)
            accommodation.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Accommodation.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AccommodationSerializer(serializers.ModelSerializer):
    """JSON serializer for Accommodations

    Arguments:
        serializers
    """

    class Meta:
        model = Accommodation
        fields = ('id', 'accommodation_name')