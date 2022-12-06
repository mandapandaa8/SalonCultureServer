"""salonculture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from salonapi.views import register_user, login_user
from salonapi.views import ArtistView, AccommodationView, CommentView, EventView, HostView, LocationView, ArtistPhotoView, HostPhotoView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'artists', ArtistView, 'artist')
router.register(r'accommodations', AccommodationView, 'accommodation')
router.register(r'comments', CommentView, 'comment')
router.register(r'events', EventView, 'event')
router.register(r'hosts', HostView, 'host')
router.register(r'locations', LocationView, 'location')
router.register(r'artistphotos', ArtistPhotoView, 'artistphoto')
router.register(r'hostphotos', HostPhotoView, 'hostphoto')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
