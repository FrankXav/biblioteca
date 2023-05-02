from rest_framework import filters
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import render

from .serializers import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

class LibrosList(generics.ListAPIView):
    serializer_class = LibrosSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects