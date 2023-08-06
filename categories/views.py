from django.shortcuts import render
from .serializers import CategorySerializer, CategoryListSerializer
from rest_framework import generics
from .models import Category

# Create your views here.
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    
class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class CategoryEdit(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDelete(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer