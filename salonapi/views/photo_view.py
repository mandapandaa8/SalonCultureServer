from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import Photo, User

class PhotoView(ViewSet):
    def retrieve(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    def list(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        photo.user = request.data[User]
        photo.photo_url = request.data["photoURL"]
        photo.caption = request.data["caption"]
        photo.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        photo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class PhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for photos
    Arguments:
        serializers
    """
    class Meta:
        model = Photo
        fields = ('id', 'user', 'photo_url', 'caption')