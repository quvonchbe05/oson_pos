from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    Register,
    UserMe,
    UserList,
    UserUpdate, 
    UserDelete,
    UserDetailView,
)


urlpatterns = [
    path('login', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('register', Register.as_view()),
    path('user/me', UserMe.as_view()),
    path('user/list', UserList.as_view()),
    path('user/edit/<int:pk>', UserUpdate.as_view()),
    path('user/delete/<int:pk>', UserDelete.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
]