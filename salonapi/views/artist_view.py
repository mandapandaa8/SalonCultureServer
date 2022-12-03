from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import Artist
from django.contrib.auth.models import User

class ArtistView(ViewSet):
    def retrieve(self, request, pk):
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    def list(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        artist = Artist.objects.get(pk=pk)
        artist.user_id = request.data[User]
        artist.medium = request.data["medium"]
        artist.cv = request.data["cv"]
        artist.profile_img = request.data["profileImg"]
        artist.location_id = request.data["locationId"]
        artist.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        artist = Artist.objects.get(pk=pk)
        artist.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class ArtistSerializer(serializers.ModelSerializer):
    """JSON serializer for artists
    Arguments:
        serializers
    """
    class Meta:
        model = Artist
        fields = ('id', 'user_id', 'medium', 'cv', 'profile_img', 'location_id')