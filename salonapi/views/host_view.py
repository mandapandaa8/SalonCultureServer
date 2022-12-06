from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from salonapi.models import Host
from django.contrib.auth.models import User

class HostView(ViewSet):
    def retrieve(self, request, pk):
        host = Host.objects.get(pk=pk)
        serializer = HostSerializer(host)
        return Response(serializer.data)

    def list(self, request):
        hosts = Host.objects.all()
        serializer = HostSerializer(hosts, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        host = Host.objects.get(pk=pk)
        host.user = User.objects.get(pk=request.data["userId"])
        host.profile_img = request.data["profileImg"]
        host.address = request.data["address"]
        host.description = request.data["description"]
        host.save()
        

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