from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import HostPhoto, Host


class HostPhotoView(ViewSet):
    def retrieve(self, request, pk):
        host_photo = HostPhoto.objects.get(pk=pk)
        serializer = PhotoSerializer(host_photo)
        return Response(serializer.data)

    def list(self, request):
        host_photos = HostPhoto.objects.all()
        serializer = PhotoSerializer(host_photos, many=True)
        return Response(serializer.data)

    def create(self, request):
        new_host_photo = HostPhoto()
        new_host_photo.host = Host.objects.get(pk=request.data["hostId"])
        new_host_photo.photo_url = request.data["photoURL"]
        new_host_photo.caption = request.data["caption"]
        new_host_photo.save()

        serializer = PhotoSerializer(new_host_photo)

        return Response(serializer.data)

    def update(self, request, pk):
        host_photo = HostPhoto.objects.get(pk=pk)
        host_photo.host = Host.objects.get(pk=request.data["hostId"])
        host_photo.photo_url = request.data["photoURL"]
        host_photo.caption = request.data["caption"]
        host_photo.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        host_photo = HostPhoto.objects.get(pk=pk)
        host_photo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class PhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for photos
    Arguments:
        serializers
    """
    class Meta:
        model = HostPhoto
        fields = ('id', 'host', 'photo_url', 'caption')