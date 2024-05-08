from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Movie_serializer
from .models import Moviedata
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Movie_view_set(LoginRequiredMixin,viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = Movie_serializer
    

class Action_movie_view(LoginRequiredMixin,viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = Movie_serializer
    
    
class Comedy_movie_view(LoginRequiredMixin,viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class = Movie_serializer