from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Product, Brand
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

class HomeView(TemplateView):
    template_name = "home.html"

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    lookup_field = 'slug'
    serializer_class = ProductSerializer

    #queryset = Product.objects.select_related('productline')
    #serializer_class = ProductSerializer

    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r"category/(?P<category>\w+)/all",url_name="all",)
    def list_product_by_category(self, request, category=None):
        queryset = self.get_queryset().filter(category__name=category)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

