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
    Catalog, 
    User, 
)
from .serializers import (
    CatalogSerializer, 
    UserSerializer, 
)
from .filters import (
    CatalogFilter, 
)


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'


class CatalogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    filterset_class = CatalogFilter

    def get_queryset(self):
        return Catalog.objects.all()

    def post(self, request, format=None):
        return Response(self.data, status.HTTP_201_CREATED)


class CatalogRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class MeAPIView(APIView):
    queryset = User.objects.all()

    def get(self, request, format=None):
        me = request.user
        serializer = UserSerializer(me)
        return Response(serializer.data)


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
