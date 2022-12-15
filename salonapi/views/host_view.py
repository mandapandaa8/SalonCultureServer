from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import Host
from django.contrib.auth.models import User

class HostView(ViewSet):
    """Handle requests for single host"""

    def retrieve(self, request, pk):

        host = Host.objects.get(pk=pk)
        if request.auth.user.id == host.user.id:
            response = {
                "id": host.id,
                "username": host.user.username,
                "first_name": host.user.first_name,
                "last_name": host.user.last_name,
                "email": host.user.email,
                "profile_img": host.profile_img,
                "address": host.address,
                "description": host.description,
                "my_profile": True
            }
        else:
            response = {
                "id": host.id,
                "username": host.user.username,
                "first_name": host.user.first_name,
                "last_name": host.user.last_name,
                "email": host.user.email,
                "profile_img": host.profile_img,
                "address": host.address,
                "description": host.description,
                "my_profile": False
            }
        return Response(response, status=status.HTTP_200_OK)
        

    def list(self, request):
        """Handle GET requests to host resource"""
        
        host = Host.objects.all()
        serializer = HostSerializer(host, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        host = Host.objects.get(pk=pk)
        host.profile_img = request.data["profile_img"]
        host.address = request.data["address"]
        host.description = request.data["description"]
        host.save()
        host.user.username = request.data["username"]
        host.user.email = request.data["email"]
        host.user.save()
        

        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        host = Host.objects.get(pk=pk)
        host.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class HostSerializer(serializers.ModelSerializer):
    """JSON serializer for hosts
    Arguments:
        serializers
    """
    class Meta:
        model = Host
        fields = ('id', 'user', 'address', 'description', 'profile_img')
        depth = 1