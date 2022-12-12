from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import ArtistPhoto, Artist

class ArtistPhotoView(ViewSet):
    def retrieve(self, request, pk):
        artist_photo = ArtistPhoto.objects.get(pk=pk)
        serializer = PhotoSerializer(artist_photo)
        return Response(serializer.data)

    def list(self, request):
        artist_photos = ArtistPhoto.objects.all()
        serializer = PhotoSerializer(artist_photos, many=True)
        return Response(serializer.data)

    def create(self, request):
        new_artist_photo = ArtistPhoto()
        new_artist_photo.artist = Artist.objects.get(pk=request.data["artistId"])
        new_artist_photo.photo_url = request.data["photoURL"]
        new_artist_photo.caption = request.data["caption"]
        new_artist_photo.save()

        serializer = PhotoSerializer(new_artist_photo)

        return Response(serializer.data)

    def update(self, request, pk):
        artist_photo = ArtistPhoto.objects.get(pk=pk)
        artist_photo.artist = Artist.objects.get(pk=request.data["artistId"])
        artist_photo.photo_url = request.data["photoURL"]
        artist_photo.caption = request.data["caption"]
        artist_photo.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        artist_photo = ArtistPhoto.objects.get(pk=pk)
        artist_photo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class PhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for photos
    Arguments:
        serializers
    """
    class Meta:
        model = ArtistPhoto
        fields = ('id', 'artist', 'photo_url', 'caption')