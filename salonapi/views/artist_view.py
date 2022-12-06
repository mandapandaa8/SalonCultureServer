from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import Artist
from django.contrib.auth.models import User

class ArtistView(ViewSet):
    """Salon Culture Artist View"""

    def list(self, request):
        """Handle GET requests to artists resource

        Returns:
            Response -- JSON serialized list of artists
        """
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handle GET requests for single artist

        Returns:
            Response -- JSON serialized artist instance
        """

        artist = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data, status.HTTP_200_OK)

    def update(self, request, pk):
        """Handle PUT requests for an artist
        
        Returns:
            Response -- Empty body with 204 status code
        """

        artist = Artist.objects.get(pk=pk)
        artist.user = request.data[User]
        artist.profile_img = request.data["profileImg"]
        artist.medium = request.data["medium"]
        artist.cv = request.data["cv"]
        artist.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests for a single artist

        Returns:
            Response -- 200, 404, or 500 status code
        """
        
        artist = Artist.objects.get(pk=pk)
        artist.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class ArtistSerializer(serializers.ModelSerializer):
    """JSON serializer for artists"""

    class Meta:
        model = Artist
        fields = ('id', 'user', 'medium', 'cv', 'profile_img')