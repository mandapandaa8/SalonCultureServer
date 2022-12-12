from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from salonapi.models import Artist, Host


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
        request -- The full HTTP request object
    '''
    username = request.data["username"]
    password = request.data["password"]

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)

    # If authentication was successful, log the user in
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True, 
            'token': token.key
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = {'valid': False}
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''
    account_type = request.data.get("account_type", None)
    first_name = request.data.get("first_name", None)
    last_name = request.data.get("last_name", None)
    username = request.data.get("username", None)
    password = request.data.get("password", None)
    email = request.data.get("email", None)

    if account_type is not None \
        and first_name is not None \
        and last_name is not None \
        and username is not None \
        and password is not None \
        and email is not None:

        if account_type == "artist":
            medium = request.data.get("medium", None)
            if medium is None:
                return Response(
                    {'message': 'Medium is a required field for artists'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            cv = request.data.get("cv", None)
            if cv is None:
                return Response(
                    {'message': 'CV is a required field for artists'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            profile_img = request.data.get("profile_img", None)
            if profile_img is None:
                return Response(
                    {'message': 'Profile image is a required field for artists'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

        elif account_type == "host":
            address = request.data.get("address", None)
            if address is None:
                return Response(
                    {'message': 'Address is a required field for hosts'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            profile_img = request.data.get("profile_img", None)
            if profile_img is None:
                return Response(
                    {'message': 'Profile image is a required field for hosts'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            description = request.data.get("description", None)
            if description is None:
                return Response(
                    {'message': 'Description is a required field for hosts'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

        else:
            return Response(
                {'message': 'Invalid account type. Valid values are \'artist\' or \'host\''}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Create a new user by invoking the `create_user` helper method
            # on Django's built-in User model
            new_user = User.objects.create_user(
                username = request.data["username"],
                is_staff = request.data["is_staff"],
                password = request.data["password"],
                email = request.data["email"],
                first_name = request.data["first_name"],
                last_name = request.data["last_name"]
            )

        except IntegrityError:
            return Response(
                {'message': 'An account with this username already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        account = None

        if account_type == "artist":
            account = Artist.objects.create(
                user = new_user,
                profile_img = request.data["profile_img"],
                medium = request.data["medium"],
                cv = request.data["cv"]
            )
        elif account_type == "host":
            account = Host.objects.create(
                user = new_user,
                profile_img = request.data["profile_img"],
                address = request.data["address"],
                description = request.data["description"]
            )

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=account.user)
        # Return the token to the client
        data = { 'token': token.key }
        return Response(data)

    return Response({'message': 'You must provide all fields to register'}, status=status.HTTP_400_BAD_REQUEST)
