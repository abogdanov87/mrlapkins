from rest_framework import generics, permissions, status, filters
from rest_framework_bulk import ListBulkCreateUpdateAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from PIL import Image
import glob, os
from django.conf import settings
from django.db.models import Q, CharField
from django.http import HttpResponse, Http404, JsonResponse


from catalogs.models import (
    Breed, 
)
from .serializers import (
    BreedSerializer, 
)
from .filters import (
    BreedFilter, 
)


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'


class BreedListCreateAPIView(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    filterset_class = BreedFilter

    def get_queryset(self):
        return Breed.objects.all()

    def post(self, request, format=None):
        return Response(self.data, status.HTTP_201_CREATED)


class BreedRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
