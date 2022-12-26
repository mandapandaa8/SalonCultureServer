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

        if "myprofile" in request.query_params:
            artist = Artist.objects.filter(user=request.auth.user)
            serializer = ArtistSerializer(
                artist, many=False, context={'request': request})
            return Response(serializer.data)
        else:
            artists = Artist.objects.all()
            serializer = ArtistSerializer(
                artists, many=True, context={'request': request})
            return Response(serializer.data)
        
    def retrieve(self, request, pk):
        """Handle GET requests for single artist

        Returns:
            Response -- JSON serialized artist instance
        """
        # step 1 = get artist matched to pk
        # step 2 = check if req.auth.user.id = artist.user.id
        # step 3 = define dictionary that has username, profile_img, medium, cv
        # step 4 = if True, add my profile key to response dictionary with value = true
        # step 5 = pass dictionary as first argument to Response 

    
        artist = Artist.objects.get(pk=pk)
        if request.auth.user.id == artist.user.id:
            response = {
                "id": artist.id,
                "username": artist.user.username,
                "first_name": artist.user.first_name,
                "last_name": artist.user.last_name,
                "email": artist.user.email,
                "profile_img": artist.profile_img,
                "medium": artist.medium,
                "cv": artist.cv,
                "my_profile": True
            }
        else:
            response = {
                "id": artist.id,
                "username": artist.user.username,
                "first_name": artist.user.first_name,
                "last_name": artist.user.last_name,
                "email": artist.user.email,
                "profile_img": artist.profile_img,
                "medium": artist.medium,
                "cv": artist.cv,
                "my_profile": False
            }
        return Response(response, status=status.HTTP_200_OK)

    def update(self, request, pk):
        """Handle PUT requests for an artist
        
        Returns:
            Response -- Empty body with 204 status code
        """

        artist = Artist.objects.get(pk=pk)
        artist.profile_img = request.data["profile_img"]
        artist.medium = request.data["medium"]
        artist.cv = request.data["cv"]
        artist.save()
        artist.user.username = request.data["username"]
        artist.user.email = request.data["email"]
        artist.user.first_name = request.data["first_name"]
        artist.user.last_name = request.data["last_name"]
        artist.user.save()

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
        depth = 1