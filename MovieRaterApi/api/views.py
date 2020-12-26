
from rest_framework import viewsets
from .models import Movie,Rating
from django.contrib.auth.models import User
from .serializers import MovieSerializer,RatingSerializer,UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .paginations import MyOffsetPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    #authentication_classes=(TokenAuthentication, )
    #permission_classes=(IsAuthenticated,)

class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    pagination_class = MyOffsetPagination
    #authentication_classes=(TokenAuthentication, )
    #permission_classes=(IsAuthenticated,)
    
class RatingViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer
    pagination_class = MyOffsetPagination
    #authentication_classes=(TokenAuthentication, )
    #permission_classes=(IsAuthenticated,)