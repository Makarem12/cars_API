from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializer import carsSerializer
from .models import Car

class carsList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class= carsSerializer

class carDetails(generics.RetrieveUpdateDestroyAPIView):
        queryset = Car.objects.all()
        serializer_class= carsSerializer