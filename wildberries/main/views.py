from django.shortcuts import render
from .serializers import CategorySerializers, SubCategorySerializers, SubSubCategorySerializers
from rest_framework import viewsets
from .models import Category, SubCategory, SubSubCategory

# Create your views here.

class CategoryView(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class SubCategoryView(viewsets.ModelViewSet):

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializers


class SubSubCategoryView(viewsets.ModelViewSet):

    queryset = SubSubCategory.objects.all()
    serializer_class = SubSubCategorySerializers