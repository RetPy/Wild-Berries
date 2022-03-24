from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductSerializer


class ProductListView(generics.ListAPIView):

    model = Product
    queryset = Product.objects
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductCreateView(generics.CreateAPIView):

    model = Product
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductUpdateView(generics.UpdateAPIView):

    model = Product
    queryset = Product.objects
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductDeleteView(generics.DestroyAPIView):

    model = Product
    queryset = Product.objects
    permission_classes = [IsAuthenticatedOrReadOnly]
