from django.urls import path
from .views import ProductCreate, ProductList, ProductDelete, ProductEdit

urlpatterns = [
    path('create', ProductCreate.as_view()),
    path('list', ProductList.as_view()),
    path('edit/<int:pk>', ProductEdit.as_view()),
    path('delete/<int:pk>', ProductDelete.as_view()),
]