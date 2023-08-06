from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    UserEditSerializer,
    UserListSerializer,
    UserDetailViewSerializer,
)
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    
class UserMe(APIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        user = JWTAuthentication().authenticate(request)
        if user:
            return Response({
                'id': user[0].id,
                'username': user[0].username,
                'email': user[0].email,
                'first_name': user[0].first_name,
                'last_name': user[0].last_name,
                'is_superuser': user[0].is_superuser,
            })
        else:
            return Response("Пользователь не найден!")
        
        
class UserList(generics.ListAPIView):
    # authentication_classes = [JWTAuthentication, ]
    # permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    
class UserUpdate(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserEditSerializer
    
class UserDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAdminUser, IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserDetailViewSerializer
    
class UserDelete(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAdminUser, IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserSerializer